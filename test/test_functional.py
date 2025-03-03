import unittest
import sys
import os

# Adjusting the path to import TestUtils for Yaksha Assertions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from wastetreatement import (
    calculate_total_waste_by_type,
    unique_waste_zones,
    find_heaviest_location
)

class TestSmartWasteManagementSystem(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils for Yaksha assertions
        self.test_obj = TestUtils()

        # Sample data for testing
        self.waste_data = [
            ("Zone A", "Organic", 120),
            ("Zone B", "Plastic", 80),
            ("Zone C", "Electronic", 45),
            ("Zone D", "Metal", 60),
            ("Zone E", "Organic", 95)
        ]

        self.expected_waste_summary = {
            "Organic": 215,
            "Plastic": 80,
            "Electronic": 45,
            "Metal": 60
        }

        self.expected_zones = {"Zone A", "Zone B", "Zone C", "Zone D", "Zone E"}
        self.expected_heaviest_zone = ("Zone A", 120)

    def test_calculate_total_waste_by_type(self):
        """
        Test case for calculate_total_waste_by_type() function.
        """
        try:
            result = calculate_total_waste_by_type(self.waste_data)
            expected_result = self.expected_waste_summary
            if result == expected_result:
                self.test_obj.yakshaAssert("TestCalculateTotalWasteByType", True, "functional")
                print("TestCalculateTotalWasteByType = Passed")
            else:
                self.test_obj.yakshaAssert("TestCalculateTotalWasteByType", False, "functional")
                print("TestCalculateTotalWasteByType = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateTotalWasteByType", False, "functional")
            print(f"TestCalculateTotalWasteByType = Failed ")

    def test_unique_waste_zones(self):
        """
        Test case for unique_waste_zones() function.
        """
        try:
            result = unique_waste_zones(self.waste_data)
            if result == self.expected_zones:
                self.test_obj.yakshaAssert("TestUniqueWasteZones", True, "functional")
                print("TestUniqueWasteZones = Passed")
            else:
                self.test_obj.yakshaAssert("TestUniqueWasteZones", False, "functional")
                print("TestUniqueWasteZones = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestUniqueWasteZones", False, "functional")
            print(f"TestUniqueWasteZones = Failed ")

    def test_find_heaviest_location(self):
        """
        Test case for find_heaviest_location() function.
        """
        try:
            result = find_heaviest_location(self.waste_data)
            if result == self.expected_heaviest_zone:
                self.test_obj.yakshaAssert("TestFindHeaviestLocation", True, "functional")
                print("TestFindHeaviestLocation = Passed")
            else:
                self.test_obj.yakshaAssert("TestFindHeaviestLocation", False, "functional")
                print("TestFindHeaviestLocation = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestFindHeaviestLocation", False, "functional")
            print(f"TestFindHeaviestLocation = Failed ")

if __name__ == '__main__':
    unittest.main()

import unittest
import os
import json
from car import search_by_budget, save_inventory

class TestCarInventorySystem(unittest.TestCase):
    def setUp(self):
        """
        Setting up the test data before running tests.
        """
        # Initialize TestUtils for Yaksha assertions
        self.test_obj = TestUtils()
        
        # Sample car inventory for testing
        self.car_inventory = [
            {"id": 1, "make": "Toyota", "model": "Camry", "year": 2021, "price": 565000},
            {"id": 2, "make": "Honda", "model": "Civic", "year": 2020, "price": 22000},
            {"id": 3, "make": "Ford", "model": "Mustang", "year": 2022, "price": 30000},
            {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2019, "price": 20000},
            {"id": 5, "make": "Nissan", "model": "Altima", "year": 2023, "price": 28000}
        ]
        
        # Expected results
        self.expected_budget_25000 = [
            {"id": 2, "make": "Honda", "model": "Civic", "year": 2020, "price": 22000},
            {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2019, "price": 20000}
        ]
        
        self.test_filename = "test_car_inventory.json"
    
    def tearDown(self):
        """
        Clean up after tests.
        """
        # Remove test file if it exists
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
    
    def test_search_by_budget(self):
        """
        Test case for search_by_budget() function.
        """
        try:
            result = search_by_budget(self.car_inventory, 25000)
            expected_result = self.expected_budget_25000
            
            # Sort both lists by id to ensure consistent comparison
            result_sorted = sorted(result, key=lambda x: x['id'])
            expected_sorted = sorted(expected_result, key=lambda x: x['id'])
            
            if result_sorted == expected_sorted:
                self.test_obj.yakshaAssert("TestSearchByBudget", True, "functional")
                print("TestSearchByBudget = Passed")
            else:
                self.test_obj.yakshaAssert("TestSearchByBudget", False, "functional")
                print("TestSearchByBudget = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestSearchByBudget", False, "functional")
            print(f"TestSearchByBudget = Failed ")
    
    def test_save_inventory(self):
        """
        Test case for save_inventory() function.
        """
        try:
            # Save inventory to test file
            result_filename = save_inventory(self.car_inventory, self.test_filename)
            
            # Check if file exists
            file_exists = os.path.exists(result_filename)
            
            # Read the saved file and check contents
            with open(result_filename, 'r') as file:
                saved_data = json.load(file)
            
            data_matches = saved_data == self.car_inventory
            
            if file_exists and data_matches and result_filename == self.test_filename:
                self.test_obj.yakshaAssert("TestSaveInventory", True, "functional")
                print("TestSaveInventory = Passed")
            else:
                self.test_obj.yakshaAssert("TestSaveInventory", False, "functional")
                print("TestSaveInventory = Failed")
                if not file_exists:
                    print("File was not created")
                if not data_matches:
                    print("Saved data does not match input data")

                if result_filename != self.test_filename:
                    print(f"Expected filename: {self.test_filename}, Actual: {result_filename}")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSaveInventory", False, "functional")
            print(f"TestSaveInventory = Failed ")

if __name__ == '__main__':
    unittest.main()


import unittest
import numpy as np
import pandas as pd

from trainseatallocation import *

from test.TestUtils import TestUtils

class TestTrainSeatAllocation(unittest.TestCase):

        # Initialize TestUtils for Yaksha assertions


    def setUp(self):
        """
        Setting up the test data before running tests.
        """
        self.test_obj = TestUtils()
        # Preset data for Train Seat Allocation
        self.seat_numbers = np.array([101, 102, 103, 104, 105])  # Seat numbers
        self.ticket_prices = np.array([250, 300, 400, 350, 500])  # Ticket prices for each seat
        self.availability = np.array([True, False, True, False, True])  # Availability status (True means available)
        self.passenger_names = ["John", "Alice", "Bob", "Emma", "David"]  # Reserved passenger names

        # Create a DataFrame to manage reservations
        self.df = pd.DataFrame({
            'Seat Number': self.seat_numbers,
            'Passenger Name': self.passenger_names,
            'Ticket Price': self.ticket_prices,
            'Availability': self.availability
        })

        # Expected Results
        self.expected_waiting_list_count = 2
        self.expected_highest_ticket_price = 500
        self.expected_highest_ticket_seat = 105
        self.expected_available_seats_count = 3



    def test_highest_ticket_price(self):
        """
        Test case for highest_ticket_price() function.
        """
        try:
            result_price, result_seat = highest_ticket_price(self.df)
            if result_price == self.expected_highest_ticket_price and result_seat == self.expected_highest_ticket_seat:
                self.test_obj.yakshaAssert("TestHighestTicketPrice", True, "functional")
                print("TestHighestTicketPrice = Passed")
            else:
                self.test_obj.yakshaAssert("TestHighestTicketPrice", False, "functional")
                print("TestHighestTicketPrice = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestHighestTicketPrice", False, "functional")
            print(f"TestHighestTicketPrice = Failed")

    def test_available_seats(self):
        """
        Test case for available_seats() function.
        """
        try:
            result = available_seats(self.df)
            expected_result = self.expected_available_seats_count
            if result == expected_result:
                self.test_obj.yakshaAssert("TestAvailableSeats", True, "functional")
                print("TestAvailableSeats = Passed")
            else:
                self.test_obj.yakshaAssert("TestAvailableSeats", False, "functional")
                print("TestAvailableSeats = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestAvailableSeats", False, "functional")
            print(f"TestAvailableSeats = Failed ")


if __name__ == '__main__':
    unittest.main()
