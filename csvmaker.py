# creates the CSV file named merged_output where i have applied the preprocessing of removing matras and symbols and leading intergers
# moreover if integer in between is present then its preserved


# preprocessing is done by preprocess.py


import pandas as pd
from preprocess import remove_matras_and_replace  # Import the function

# Load the .dta file
dta_file = r'data\Unemployment_Baseline_Parents_2_Data.dta'
itr = pd.read_stata(dta_file, iterator=True)

# Extract the variable labels
variable_labels = itr.variable_labels()

# Create a DataFrame from the dictionary
dta_df = pd.DataFrame(list(variable_labels.items()), columns=['Stata_Name', 'Stata_Label'])

# Load the Excel file
file_path = r'data\Unemployment_Baseline_Parents_2_Data.xlsx'  # Update this with the path to your Excel file

# Read the Excel file and treat the first row as header
excel_df = pd.read_excel(file_path, header=None)

# Extract the first row (which contains the column names)
column_names = excel_df.iloc[0].tolist()

# Create a new DataFrame with the column names under 'XLXS_COLUMN'
first_row_df = pd.DataFrame(column_names, columns=['XLXS_COLUMN'])

# Apply the preprocessing function to the 'XLXS_COLUMN'
first_row_df['XLXS_COLUMN'] = first_row_df['XLXS_COLUMN'].apply(remove_matras_and_replace)

# Merge the two DataFrames, ensuring XLXS_COLUMN is the first column
merged_df = pd.concat([first_row_df, dta_df], axis=1)

# Save the merged DataFrame as a CSV file
merged_df.to_csv('merged_output.csv', index=False)
