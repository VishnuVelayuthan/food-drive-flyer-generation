import xlrd

name_of_sheet = "LAHSTeams.xlsx"

excel_book = xlrd.open_workbook(name_of_sheet)
excel_sheet = xlrd.open_sheet_by_name("Sheet1")

print(excel_sheet.cell(12, 5).value)