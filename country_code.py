import pandas as pd

for file in ["phone-number","phone-number_2"]:
    # Load the first CSV file into a DataFrame
    df = pd.read_csv(file+".csv")

    # Add the country code as a string prefix in the "phone" column
    df["phone"] = "+91" + df["phone"].astype(str)

    # Save the modified DataFrame back to the first CSV file
    df.to_csv(file+".csv", index=False)      