import pandas as pd
import os

# Define file names
files = ['Base.csv', 'Variant I.csv', 'Variant II.csv', 'Variant III.csv', 'Variant IV.csv', 'Variant V.csv']

# Path to your archive folder where the .csv files are located
archive_path = '../archive/'

# Create account numbers
account_numbers = list(range(1, 1000001))

# Process each file
for file in files:
    # Read the CSV file
    df = pd.read_csv(os.path.join(archive_path, file))
    
    # Add the "Account_Number" column
    df['Account_Number'] = account_numbers
    
    # Overwrite the old file with the modified data
    df.to_csv(os.path.join(archive_path, file), index=False)

print("All files have been updated and replaced in the archive folder.")