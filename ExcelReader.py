import openpyxl
import GraphicDesigner
from pathlib import Path

# print(excel_sheet["E12"].value)

name_of_sheet = "LAHSTeams.xlsx"

# Arrays to iterate for specific use case
cols_to_iter = ["B", "C", "E"]
rows_to_iter = range(2, 82)

# array of data 
data_arr = ["room_name", "teacher_name", "donation_link"]

if __name__ == "__main__":
    # using pyxl to access the xlsx file 
    excel_book = openpyxl.load_workbook(Path("", name_of_sheet))
    excel_sheet = excel_book.active 

    for row_num in rows_to_iter:

        for arr_index, col_letter in enumerate(cols_to_iter):
            cell = col_letter + str(row_num) # this is the cell location like "E3"
            data_arr[arr_index] = excel_sheet[cell].value
        
        room_name = data_arr[0]
        teacher_name = data_arr[1]
        donation_link = data_arr[2]

        # calling the graphic designer function
        GraphicDesigner.make_flyer(room_name, teacher_name, donation_link)




