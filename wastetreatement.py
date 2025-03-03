# Smart Waste Management System

# Preset waste data (Location, Waste Type, Weight in kg)
waste_data = [
    ("Zone A", "Organic", 120),
    ("Zone B", "Plastic", 80),
    ("Zone C", "Electronic", 45),
    ("Zone D", "Metal", 60),
    ("Zone E", "Organic", 95)
]


# Function 1: Calculate total waste by type
def calculate_total_waste_by_type(data):
    """
    TODO: Iterate through the data and sum up the total weight for each waste type.
    Store results in a dictionary where the key is the waste type and the value is the total weight.
    """
    waste_summary = {}  # Dictionary to store waste type totals

    pass  # Replace with logic to calculate total waste by type

    return waste_summary  # Return the summary instead of printing it


# Function 2: Identify unique waste zones
def unique_waste_zones(data):
    """
    TODO: Extract and return a set of unique waste zones from the data.
    """
    zones = set()  # Set to store unique zones

    pass  # Replace with logic to extract unique zones

    return zones  # Return the unique zones instead of printing them


# Function 3: Find heaviest waste location
def find_heaviest_location(data):
    """
    TODO: Identify the location with the heaviest waste recorded.
    Use max() to find the location with the highest weight.
    Return the location and its weight.
    """
    heaviest_zone = None  # Placeholder for heaviest location

    pass  # Replace with logic to find the heaviest waste location

    return heaviest_zone  # Return the heaviest zone and its weight


# Main Execution
def main():
    """
    TODO: Execute all functions and display results.
    - Calculate total waste by type
    - Identify unique waste zones
    - Find the heaviest waste location
    """
    pass  # Replace with function calls and print statements


if __name__ == "__main__":
    main()
