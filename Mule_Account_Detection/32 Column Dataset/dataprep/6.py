import pandas as pd
import os

# Define file names
input_file = 'base_less_cols.csv'
half1_file = 'base_less_cols_half1.csv'
half2_file = 'base_less_cols_half2.csv'

# Path to your archive folder
archive_path = '../archive/'

# Read the base_less_cols.csv file
df = pd.read_csv(os.path.join(archive_path, input_file))

# Split the data into two halves based on "Account_Number"
df_half1 = df[df['Account_Number'] <= 500000]
df_half2 = df[df['Account_Number'] > 500000]

# Save the two halves into separate .csv files
df_half1.to_csv(os.path.join(archive_path, half1_file), index=False)
df_half2.to_csv(os.path.join(archive_path, half2_file), index=False)

print("base_less_cols.csv has been divided into base_less_cols_half1.csv and base_less_cols_half2.csv and saved in the archive folder.")