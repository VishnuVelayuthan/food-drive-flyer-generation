import openpyxl
import GraphicDesigner
from pathlib import Path

name_of_sheet = "LAHSTeams.xlsx"

excel_book = openpyxl.load_workbook(Path("", name_of_sheet))
excel_sheet = excel_book.active 

print(excel_sheet["E12"].value)

