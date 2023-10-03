from openpyxl import load_workbook

wb = load_workbook(filename = "../data/sample.xlsx")

sheet_ranges = wb["New Title"]
print(sheet_ranges['A2'].value)