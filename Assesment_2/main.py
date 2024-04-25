import json

# File path to the JSON file
file_path = 'ex5.json'

# Load JSON data from the file
with open(file_path, 'r') as file:
    ex5 = json.load(file)

# Check the type of ex5 and handle accordingly
if isinstance(ex5, dict):
    # If ex5 is a dictionary, access the 'donuts' list from it
    donuts = ex5.get('donuts', [])
elif isinstance(ex5, list):
    # If ex5 is a list, assume it contains dictionaries and handle each one
    donuts = ex5
else:
    # Unexpected structure
    print("Unexpected structure in the JSON file. Please verify the JSON data.")
    exit(1)

# Iterate through the donuts list and add the batter if necessary
for donut in donuts:
    if donut.get('name') == 'Old Fashioned':
        # Add a new batter named 'Tea' to the donut's batters list
        new_batter = {
            'id': '1005',
            'type': 'Tea'
        }
        donut['batters']['batter'].append(new_batter)

# Write the updated JSON data back to the file
with open(file_path, 'w') as file:
    json.dump(ex5, file, indent=4)

print("Updated ex5.json with the new batter 'Tea' for donut 'Old Fashioned'.")