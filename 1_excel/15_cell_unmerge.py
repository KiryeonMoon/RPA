from openpyxl import load_workbook
wb = load_workbook("Sample_merge.xlsx")
ws = wb.active

# B2:D2 병합된 셀을 해제
ws.unmerge_cells("B2:D2")

wb.save("Sample_unmerge.xlsx")
