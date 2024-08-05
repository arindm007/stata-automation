# after creation of csv just run this script to 
# generate stata commands of rename and assigning values to label variable

import pandas as pd
import os

# Load the CSV file
file_path = 'E:\ohm^-1\stata\merged_output.csv'  # Update this path
df = pd.read_csv(file_path)

# Initialize an empty list to store the commands
commands = []

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    xlsx_column = row['XLXS_COLUMN'].split()[0]
    stata_name = row['Stata_Name']
    stata_label = row['Stata_Label']
    
    # Create the rename and label variable commands
    rename_command = f"rename {xlsx_column} {stata_name}"
    label_command = f"label variable {stata_name} \"{stata_label}\""
    
    # Add the commands to the list
    commands.append(rename_command)
    commands.append(label_command)

# Join the commands into a single string with newline characters
commands_string = "\n".join(commands)

# Save the commands to a text file
output_file_path = 'E:\ohm^-1\stata\stata_commands.txt'  # Update this path
with open(output_file_path, 'w',encoding='utf-8') as file:
    file.write(commands_string)

# Open the directory containing the output file
directory = os.path.dirname(output_file_path)
os.startfile(directory)
