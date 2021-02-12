import pyautogui

pyautogui.sleep(3)  # 3초 대기
# print(pyautogui.position())

# 마우스 클릭
# pyautogui.click(1036, 29, duration=1)  # 1초 간 해당 좌표로 이동 후 마우스 클릭

# pyautogui.mouseDown()
# pyautogui.mouseUp()
# 위의 두 함수를 합친 함수가 pyautogui.click()임
# Drag & Drop 할 때 이 두개를 이용함

# pyautogui.doubleClick()

# doubleClick과 같은 동작을 하는 명령문. 매크로 할 때 이거 한 500으로 넣으면 개꿀
# pyautogui.click(clicks=2)

# pyautogui.moveTo(1036, 623)
# 동작이 너무 빨라 어떤 행동이 안 될때는 duration을 이용해 시간텀을 준다.
# pyautogui.drag(200, 0, duration=0.5)  # 현재 위치 기준으로 x 200만큼 y 0만큼 드래그

pyautogui.scroll(300)  # 양수이면 위로, 음수이면 아래로 300만큼 스크롤
