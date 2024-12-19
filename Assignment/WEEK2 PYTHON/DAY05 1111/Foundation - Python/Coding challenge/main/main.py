import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.Payshelter_impl import PetShelter_impl
from dao.IUser import IUser
from dao.IDonator import IDonator
from dao.IParticipants import IParticipants
from exception.AdoptionException import AdoptionException
from exception.InsufficientFundsException import InsufficientFundsException
from exception.InvalidPetAgeException import InvalidPetAgeException
from exception.NullReferenceException import NullReferenceException
from util.DBConnection import dbConnection
from entity.PetShelter import PetShelter


def main_menu():
    dbconnection = dbConnection()
    try:
        dbconnection.open()
        print("--Database Is Connected:--")
    except Exception as e:
        print(e)
    try:
        print("*" * 20)
        print("PetPals")
        print("*" * 20)
        print("Welcome to Petpals")
        print("*"* 20)
        while True:
            print("\nMenu:")
            print("1. Add Pet")
            print("2. List Available Pets")
            print("3. Record Cash Donation")
            print("4. PArticipate in events")
            print("5. Adopt a Pet")
            print("6. List the Donations")
            print("0. Exit")
            ch = int(input("Enter choice: "))
            if ch == 1:
                u = IUser()
                u.add_pet()
            elif ch == 2:
                u = IUser()
                u.display_pet_listings()
            elif ch == 3:
                d=IDonator()
                d.record_cash_donation()
            elif ch == 4:
                p=IParticipants()
                p.manage_adoption_events()
            elif ch == 5:
                pet_name = input("Enter the name of the pet to adopt: ")
                u=IUser()
                try:
                    u.adopt_pet(pet_name)  
                except AdoptionException as e:
                    print(e)
            elif ch==6:
                d=IDonator()
                d.display_donations()
            elif ch==0:
                break
            else:
                print("Invalid choice")

    except AdoptionException as e:
        print(e)
    except InsufficientFundsException as e:
        print(e)
    except InvalidPetAgeException as e:
        print(e)
    except NullReferenceException as e:
        print(e)
    finally:
        dbconnection.close()
        print("Thankyou for visiting Petpals!")
        print("--Connection Is Closed:--")


if __name__ == "__main__":
    main_menu()
