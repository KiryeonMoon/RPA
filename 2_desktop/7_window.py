import pyautogui

fw = pyautogui.getActiveWindow()  # 현재 활성화된 창 정보를 가져옴
print(fw.title)
print(fw.size)
print(fw.left, fw.top, fw.right, fw.bottom)
pyautogui.click(fw.left + 25, fw.top + 20)

# 눈에 보이는 것부터 안보이는 모든 활성화된 윈도우 다 가져오기
for w in pyautogui.getAllWindows():
    print(w)

# 어떤 제목을 포함하는 윈도우만 가져옥
for w in pyautogui.getWindowsWithTitle():
