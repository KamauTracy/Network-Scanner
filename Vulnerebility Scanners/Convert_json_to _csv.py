import os
import json
import csv

# Folder containing your JSON files
folder_path = "CVE LIST V5"

# Function to convert a JSON file to a CSV file
def json_to_csv(json_file, csv_file):
    try:
        # Open and load the JSON file
        with open(json_file, 'r') as jf:
            data = json.load(jf)
        
        # Determine the structure of the JSON data
        if isinstance(data, dict):  # Single dictionary
            data = [data]  # Convert to list of one dictionary        
        if isinstance(data, list) and len(data) > 0:

            # Extract headers from the first dictionary
            headers = data[0].keys()
            
            # Write CSV file
            with open(csv_file, 'w', newline='', encoding='utf-8') as cf:
                writer = csv.DictWriter(cf, fieldnames=headers)
                writer.writeheader()  # Write the header row
                writer.writerows(data)  # Write the data rows
            print(f"Converted {json_file} to {csv_file}")
        else:
            print(f"Skipping {json_file} - Not a valid JSON array or dictionary")
    except Exception as e:
        print(f"Error processing {json_file}: {e}")

# Loop through all JSON files in the folder
for file in os.listdir(folder_path):
    if file.endswith(".json"):
        json_file = os.path.join(folder_path, file)
        csv_file = os.path.join(folder_path, f"formatted_{file.replace('.json', '.csv')}")
        json_to_csv(json_file, csv_file)


