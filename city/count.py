import pandas as pd

# Load the excel file
df = pd.read_excel("concatenated_data.xlsx")

# Count the number of occurrences of each payment method
payment_counts = df['Payment'].value_counts()

# Create a new dataframe with payment method and their count
payment_df = pd.DataFrame({'Payment Method': payment_counts.index, 'Count': payment_counts.values})

# Save the dataframe as a new excel file with a new sheet named "count"
with pd.ExcelWriter("count.xlsx") as writer:
    payment_df.to_excel(writer, sheet_name='count', index=False)
