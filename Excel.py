import openpyxl

book = openpyxl.load_workbook('LiCl_Logbook.xlsx')

sheet = book.active

a3 = sheet.cell(row=5, column=5)

print(type(a3.value))

2780

3300