# /car_inventory.py

import json

# Sample dataset with 5 cars
car_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2021, "price": 565000},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2020, "price": 22000},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2022, "price": 30000},
    {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2019, "price": 20000},
    {"id": 5, "make": "Nissan", "model": "Altima", "year": 2023, "price": 28000}
]

# Function 1: Search cars by budget
def search_by_budget(inventory, max_price):
    """
    TODO: Find and return cars that are within the given budget.
    Use list comprehension to filter cars based on price.
    """
    pass  # Replace with filtering logic and return the list

# Function 2: Save inventory to a file
def save_inventory(inventory, filename="car_inventory.json"):
    """
    TODO: Save the car inventory as a JSON file.
    Use json.dump() with indent=4 for readability.
    """
    pass  # Replace with logic to save the inventory to a JSON file

# Main Execution
def main():
    """
    TODO: Call search_by_budget and save_inventory functions.
    - Search for cars under a certain price
    - Save the inventory to a file
    """
    pass  # Replace with function calls and print statements

if __name__ == "__main__":
    main()
