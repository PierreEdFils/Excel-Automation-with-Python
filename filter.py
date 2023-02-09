import pandas as pd
import os

# Load the data from "concatenated_data.xlsx"
df = pd.read_excel("concatenated_data.xlsx")

# Filter data for female gender
df = df[df['Gender'] == 'Female']

# Create a folder for each city, if it doesn't already exist
if not os.path.exists("city"):
    os.mkdir("city")

# Group the data by the unique values in the City column
for city , group in df.groupby("City"):
    # extract the data from the column A:R
    group = group.iloc[:,:18]
    
    # Save the data to a new excel file
    group.to_excel(f"city/{city}.xlsx", index=False)

