from openpyxl import Workbook

# 엑셀 통합시트(워크북)을 열고, 거기서 시트를 하나 켠 상황
wb = Workbook()  # 새 워크북 : 엑셀 통합시트 하나 켠 상황
ws = wb.active  # 현재 활성화된 시트를 가져오는 명령

ws.title = "BirmanSheet"  # sheet의 이름 변경
wb.save("sample.xlsx")
wb.close()
