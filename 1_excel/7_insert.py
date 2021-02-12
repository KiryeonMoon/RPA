from openpyxl import load_workbook
wb = load_workbook("Sample.xlsx")
ws = wb.active

# 8번째 줄이 비워짐
# ws.insert_rows(8)

# 8번째 줄부터 5개 줄이 비워짐
# ws.insert_rows(8, 5)

# B번째 새로운 열 추가
# ws.insert_cols(2)

# B열부터 3개 열 추가
ws.insert_cols(2, 3)

wb.save("Sample_insert_cols.xlsx")
