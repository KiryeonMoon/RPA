# 스크린샷 찍기
import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png")  # 파일로 저장됨

# pyautogui.mouseInfo()

pixel = pyautogui.pixel(980, 15)  # 해당 좌표의 픽셀 한 개를 가져옴
print(pixel)  # 해당 위치 픽셀의 rgb를 찍어줌

# 이 위치의 좌표를 클릭하려는 곳이 진짜 내가 클릭하려는 좌표와 똑같은지 pixel로 비교 가능
# print(pyautogui.pixelMatchesColor(980, 15, (33, 33, 33)))
print(pyautogui.pixelMatchesColor(980, 15, pixel))
