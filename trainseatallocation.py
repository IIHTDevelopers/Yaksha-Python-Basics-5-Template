import unittest
import numpy as np
import pandas as pd

# Railway Reservation System

# Preset data for the Railway Reservation System
seat_numbers = np.array([101, 102, 103, 104, 105])  # Seat numbers
ticket_prices = np.array([250, 300, 400, 350, 500])  # Ticket prices for each seat
availability = np.array([True, False, True, False, True])  # Availability status (True means available)
passenger_names = ["John", "Alice", "Bob", "Emma", "David"]  # Reserved passenger names

# Create a DataFrame to manage reservations
df = pd.DataFrame({
    'Seat Number': seat_numbers,
    'Passenger Name': passenger_names,
    'Ticket Price': ticket_prices,
    'Availability': availability
})

# Function 1: Find the total waiting list (count passengers with unavailable seats)
def total_waiting_list(df):
    """
    TODO: Count the number of passengers whose seats are unavailable.
    """
    pass  # Replace with logic to count unavailable seats

# Function 2: Find the highest ticket price
def highest_ticket_price(df):
    """
    TODO: Identify the seat with the highest ticket price.
    Use df['Ticket Price'].max() to find the maximum value.
    """
    pass  # Replace with logic to find the highest ticket price and seat number

# Function 3: Find the number of available seats
def available_seats(df):
    """
    TODO: Count the number of seats marked as available (Availability == True).
    """
    pass  # Replace with logic to count available seats

# Main Execution
def main():
    """
    TODO: Execute all functions and display results.
    - Find total waiting list
    - Find the highest ticket price
    - Find the number of available seats
    """
    pass  # Replace with function calls and print statements

if __name__ == "__main__":
    main()
