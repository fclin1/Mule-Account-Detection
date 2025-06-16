import pandas as pd
import os

# Define file names
base_file = 'Base.csv'
half1_file = 'Base_half1.csv'
half2_file = 'Base_half2.csv'

# Path to your archive folder where the .csv file is located
archive_path = '../archive/'

# Read the original Base.csv file
df = pd.read_csv(os.path.join(archive_path, base_file))

# Split the data into two halves based on "Account_Number"
df_half1 = df[df['Account_Number'] <= 500000]
df_half2 = df[df['Account_Number'] > 500000]

# Save the two halves into separate .csv files
df_half1.to_csv(os.path.join(archive_path, half1_file), index=False)
df_half2.to_csv(os.path.join(archive_path, half2_file), index=False)

print("Base.csv has been divided into Base_half1.csv and Base_half2.csv and saved in the archive folder.")