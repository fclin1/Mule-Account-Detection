import pandas as pd
import os

# Define file names for the variants
variant_files = ['Variant I.csv', 'Variant II.csv', 'Variant III.csv', 'Variant IV.csv', 'Variant V.csv']
combined_file = 'All_Variants_Combined.csv'

# Path to your archive folder
archive_path = '../archive/'

# List to hold individual dataframes
dfs = []

# Read each variant file and append to the list
for file in variant_files:
    df = pd.read_csv(os.path.join(archive_path, file))
    dfs.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Reset the "Account_Number" column to range from 1 to 5,000,000
combined_df['Account_Number'] = range(1, len(combined_df) + 1)

# Save the combined dataframe to a new .csv file in the archive folder
combined_df.to_csv(os.path.join(archive_path, combined_file), index=False)

print("All variant files have been combined into All_Variants_Combined.csv with updated Account_Number and saved in the archive folder.")