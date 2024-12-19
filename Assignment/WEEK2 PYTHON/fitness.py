import datetime

class FitnessTracker:
    def __init__(self):
        self.activity_data = {}
        self.daily_goals = {"steps": 10000, "distance": 5, "calories": 2000}  # Default goals

    def log_activity(self):
        date = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            return

        steps = int(input("Enter the number of steps: "))
        distance = float(input("Enter the distance walked (km): "))
        calories = float(input("Enter the calories burned: "))

        self.activity_data[date] = {"steps": steps, "distance": distance, "calories": calories}
        print(f"Activity for {date} logged successfully.")

    def set_daily_goals(self):
        print("Set your daily goals:")
        self.daily_goals["steps"] = int(input("Enter your daily steps goal: "))
        self.daily_goals["distance"] = float(input("Enter your daily distance goal (km): "))
        self.daily_goals["calories"] = float(input("Enter your daily calories goal: "))
        print("Daily goals updated successfully.")

    def monitor_progress(self):
        if not self.activity_data:
            print("No activity data logged yet.")
            return

        date = input("Enter the date (YYYY-MM-DD) to check progress: ")
        if date not in self.activity_data:
            print(f"No data found for {date}.")
            return

        data = self.activity_data[date]
        print(f"\nProgress for {date}:")
        for metric in ["steps", "distance", "calories"]:
            progress = data[metric] / self.daily_goals[metric] * 100
            print(f"{metric.capitalize()}: {data[metric]} (Goal: {self.daily_goals[metric]}) - {progress:.2f}% achieved.")

    def generate_reports(self):
        if not self.activity_data:
            print("No activity data logged yet.")
            return

        print("\nGenerating reports...")
        weekly_report = {}
        for date, data in self.activity_data.items():
            week_number = datetime.datetime.strptime(date, "%Y-%m-%d").isocalendar()[1]
            if week_number not in weekly_report:
                weekly_report[week_number] = {"steps": 0, "distance": 0, "calories": 0, "days": 0}

            for key in ["steps", "distance", "calories"]:
                weekly_report[week_number][key] += data[key]
            weekly_report[week_number]["days"] += 1

        for week, summary in weekly_report.items():
            print(f"\nWeek {week}:")
            for key in ["steps", "distance", "calories"]:
                avg = summary[key] / summary["days"]
                print(f"  Average {key}: {avg:.2f}")

        print("\nTrends:")
        for key in ["steps", "distance", "calories"]:
            trends = [data[key] for date, data in sorted(self.activity_data.items())]
            trend = "increasing" if all(trends[i] <= trends[i + 1] for i in range(len(trends) - 1)) else "decreasing"
            print(f"  {key.capitalize()} trend: {trend}")

    def menu(self):
        while True:
            print("\nFitness Tracker Menu:")
            print("1. Log Activity")
            print("2. Set Daily Goals")
            print("3. Monitor Progress")
            print("4. Generate Reports")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.log_activity()
            elif choice == "2":
                self.set_daily_goals()
            elif choice == "3":
                self.monitor_progress()
            elif choice == "4":
                self.generate_reports()
            elif choice == "5":
                print("Exiting Fitness Tracker. Stay healthy!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = FitnessTracker()
    tracker.menu()
