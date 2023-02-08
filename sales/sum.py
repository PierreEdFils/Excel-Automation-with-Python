from openpyxl import load_workbook
import os

for month  in ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']:
    file_name = f"{month}.xlsx"
    if os.path.isfile(file_name):

         # Load the workbook
        wb =load_workbook(file_name)
        sheet = wb.active

        # Apply the SUM formula to J2 to J1001
        sheet["J1002"] = "=SUM(J2:J1001)"

        # Apply the AVERAGE formula to H2 to H1001
        sheet["H1002"] = "=AVERAGE(H2:H1001)"
        # Save the workbook
        wb.save(file_name)
        
    else :
        print(f"File {file_name} not found")

    
