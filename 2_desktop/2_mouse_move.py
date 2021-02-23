import pyautogui

# 마우스 이동

# 절대좌표 기준으로(왼쪽상단이 0,0) 움직이도록 설정
pyautogui.moveTo(200, 100)  # 지정 위치로 마우스를 이동 (가로x, 세로y)
pyautogui.moveTo(500, 700, duration=1)  # 5초동안 100, 200 위치로 이동
pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(200, 200, duration=0.25)
pyautogui.moveTo(300, 300, duration=0.25)
pyautogui.moveTo(400, 400, duration=0.25)
pyautogui.moveTo(500, 500, duration=0.25)


# 상대좌표 기준으로(현재위치가 0,0) 움직이도록 설정
pyautogui.moveTo(100, 100, duration=0.25)
print(pyautogui.position())  # point(x,y)
pyautogui.move(100, 100, duration=0.25)
print(pyautogui.position())  # point(x,y)
pyautogui.move(100, 100, duration=0.25)
print(pyautogui.position())  # point(x,y)

p = pyautogui.position()
print(p[0], p[1])  # x, y
print(p.x, p.y)  # x, y
