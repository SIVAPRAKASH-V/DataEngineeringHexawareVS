import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.donation import Donation


class ItemDonation(Donation):
    def __init__(self, donor_name: str, item_type: str):
        super().__init__(donor_name, 0)  # Amount is irrelevant for item donations
        self.item_type = item_type

    def record_donation(self):
        return f"Item donation recorded: {self.donor_name} donated {self.item_type}"
