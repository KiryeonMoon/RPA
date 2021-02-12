from openpyxl import load_workbook
wb = load_workbook("Sample.xlsx")
ws = wb.active

# 8번째 줄에 있는 7번 학생 데이터 삭제
# ws.delete_rows(8)

# 8번째 줄에 있는 7번 학생으로부터 세 줄 삭제
# ws.delete_rows(8, 3)

# 2번째 열에 있는 B 삭제
# ws.delete_cols(2)

# 2번째 열로부터 총 2개 열 삭제
ws.delete_cols(2, 2)

wb.save("Sample_delete_rows.xlsx")
