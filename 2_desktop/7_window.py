import pyautogui
import time

# fw = pyautogui.getActiveWindow()  # 현재 활성화된 창 정보를 가져옴
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left + 25, fw.top + 20)

# 눈에 보이는 것부터 안보이는 모든 활성화된 윈도우 다 가져오기
# for w in pyautogui.getAllWindows():
#     print(w)

# 어떤 제목을 포함하는 윈도우만 가져오기
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:  # 현재 해당 윈도우 활성화(맨 앞으로 가져오기)가 되어있지 않았다면
    w.activate()  # 활성화(맨 앞으로 화면을 가져온다.)

time.sleep(2)
if w.isMaximized == False:  # 현재 최대화되지 않았다면
    w.maximize()  # 최대화

# if w.isMinimized == False: # 현재 최소화되지 않았다면
#     w.minimize # 최소화

time.sleep(2)
w.restore()  # 화면 원복

w.close()  # 윈도우 닫기
