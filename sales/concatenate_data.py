import pandas as pd

# List to store the dataframes
df_list = []

# Loop through the 12 files
for month  in ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']:
    # # Use str.zfill() to format the month number with leading zeros
    # month_str = str(i).zfill(2)
    file_name = f"{month}.xlsx"
    df = pd.read_excel(file_name)
    df_list.append(df)

# Concatenate the dataframes
result = pd.concat(df_list)

# Write the result to a new excel file
result.to_excel(r"concatenated_data.xlsx")
