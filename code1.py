import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Directory containing all CSV files
directory = r'C:\Users\Yasser\Desktop\PB\Cancer_CSV'

# Dictionary to store DataFrames for each person
data_dict = {}

# Iterate over each CSV file in the directory
index=1
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        
        
        # Read CSV file into a DataFrame
        df = pd.read_csv(file_path,skiprows=1, header=None, names=['ID_REF', 'VALUE', 'ABS_CALL', 'DETECTION P-VALUE'])
        
        # Add DataFrame to dictionary with person ID as key
        data_dict[index] = df
        index+=1

# Access data for a specific person (for example, person with ID '100'):


# Display data for person 100
print(data_dict[1])




import pandas as pd
import os

# Directory containing all CSV files
directory = r'C:\Users\Yasser\Desktop\PB\Cancer_csv'

# List to store DataFrames for each person
dfs = []

# List to store 'ID_REF' columns for each person
id_refs = []

# Iterate over each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        
        # Read CSV file into a DataFrame
        df = pd.read_csv(file_path, skiprows=1, header=None, names=['ID_REF', 'VALUE', 'ABS_CALL', 'DETECTION P-VALUE'])
        
        # Remove specified columns 'ABS_CALL' and 'DETECTION P-VALUE'
        df.drop(columns=['ABS_CALL', 'DETECTION P-VALUE'], inplace=True)
        
        # Store 'ID_REF' column only once
        if not id_refs:
            id_refs.append(df['ID_REF'])
        
        # Store 'VALUE' column
        dfs.append(df['VALUE'])

# Concatenate 'VALUE' columns from all DataFrames into a single DataFrame
concatenated_df = pd.concat(dfs, axis=1)

# Concatenate 'ID_REF' column with 'VALUE' DataFrame
final_df = pd.concat([id_refs[0], concatenated_df], axis=1)

# Display the final DataFrame
print(final_df)
print(final_df.head)
