import pandas as pd
import os

# Define file names
base_file = 'Base.csv'
base_99_file = 'base_99_%.csv'
base_1_file = 'base_1_%.csv'

# Path to your archive folder where the .csv file is located
archive_path = '../archive/'

# Read the original Base.csv file
df = pd.read_csv(os.path.join(archive_path, base_file))

# Split the data into two parts based on "Account_Number"
df_base_99 = df[df['Account_Number'] <= 990000]
df_base_1 = df[df['Account_Number'] > 990000]

# Save the two parts into separate .csv files
df_base_99.to_csv(os.path.join(archive_path, base_99_file), index=False)
df_base_1.to_csv(os.path.join(archive_path, base_1_file), index=False)

print("Base.csv has been divided into base_99_%.csv and base_1_%.csv and saved in the archive folder.")