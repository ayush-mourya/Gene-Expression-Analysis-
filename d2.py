import os
import csv

def remove_last_line_from_csv(file_path):
    # Read the CSV file and store its content in a list
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        lines = list(reader)
    
    # Write all lines except the last one to a temporary file
    with open(file_path + '.tmp', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines[:-1])
    
    # Replace the original file with the temporary file
    os.replace(file_path + '.tmp', file_path)

# Directory containing CSV files
folder_path = r"C:\Users\Yasser\Desktop\PB\NORMAL_CSV"  # Update with the path to your folder

# Iterate through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):  # Process only CSV files
        file_path = os.path.join(folder_path, file_name)
        remove_last_line_from_csv(file_path)
        print(f"Last line removed from '{file_name}'.")

print("All files processed.")
