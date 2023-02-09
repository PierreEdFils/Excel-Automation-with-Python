import os

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

for month in months:

    file_name = f"{month}.xlsx"
    if os.path.isfile(file_name):
        new_file_name= "carsales " + file_name
        os.rename(file_name,new_file_name)
    else:
        print(f"File {file_name} not found")
   
