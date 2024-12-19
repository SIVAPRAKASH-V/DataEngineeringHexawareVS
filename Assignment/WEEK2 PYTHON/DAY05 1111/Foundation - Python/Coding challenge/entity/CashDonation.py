from datetime import datetime
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.donation import Donation

class CashDonation(Donation):
    def __init__(self, donor_name: str, amount: float, donation_date: datetime):
        super().__init__(donor_name, amount)
        self.donation_date = donation_date

    def record_donation(self):
        return f"Cash donation recorded: {self.donor_name} donated ${self.amount} on {self.donation_date}"
