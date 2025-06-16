import pandas as pd
import os

# Define the file names
base_file = 'Base.csv'
new_file = 'base_less_cols.csv'

# Low-priority columns to remove
columns_to_remove = [
    'housing_status', 'phone_home_valid', 'phone_mobile_valid',
    'bank_months_count', 'has_other_cards', 'proposed_credit_limit',
    'source', 'device_os', 'device_fraud_count'
]

# Path to your archive folder
archive_path = '../archive/'

# Read the original Base.csv file
df = pd.read_csv(os.path.join(archive_path, base_file))

# Drop the low-priority columns
df_less_cols = df.drop(columns=columns_to_remove)

# Save the new dataframe to a .csv file
df_less_cols.to_csv(os.path.join(archive_path, new_file), index=False)

print("Low-priority columns have been removed from Base.csv and saved as base_less_cols.csv in the archive folder.")