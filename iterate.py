import pandas as pd
import os

# directory containing all excel files
directory = '.'

# new output folder name
output_folder = 'Output'

# check if output folder exists, if not create one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# iterate through all excel files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(directory, filename)
        df = pd.read_excel(file_path)
        
        # replace the specified strings
        df = df.replace({"electronic accessories": "electronic equipment",
                         "Home and lifestyle": "lifestyle"})
        
        # save the modified file in the output folder
        df.to_excel(os.path.join(output_folder, filename), index=False)