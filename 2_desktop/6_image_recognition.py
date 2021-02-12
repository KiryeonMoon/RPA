# pyautogui의 핵심. 자동화 대상 영역을 이미지로 만들고
# 구동할 때는 그 이미지를 전체 화면 내에서 찾는 방식으로 동작함
import pyautogui
import time
import sys  # 프로그램 종료를위해 필요
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon, duration=0.5)


# for i in pyautogui.locateAllOnScreen("checkBox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkBox.png")
# pyautogui.click(checkbox)


########## 속도 개선방법 ###########
# 1. GrayScale : 여러 색이 들어가 있는 이미지를 흑백전환하고 비교 : 30%정도 속도 개선 가능
# 주의 : 정확도가 조금 떨어질 수도..
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정 : 지정 범위 내에서만 검색
# trash_icon = pyautogui.locateOnScreen(
#     "trash_icon.png", region=(1015, 818, 1914-1015, 1027-818))
# pyautogui.moveTo(trash_icon, duration=0.25)

# 3. 정확도 조정
# confidence의 기본은 0.999(99.9%)
# run_btn = pyautogui.locateOnScreen("run_button.png", confidence=0.9)  # 90%
# pyautogui.moveTo(run_btn)
#####################################

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 해당 대상이 뜰 때 까지 while문을 통해 무한대기
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안만 기다리기(Time Out)
timeout = 10  # 10초 대기
# start = time.time()  # 시작시간
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()  # 종료시간
#     if end - start > timeout:  # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()  # 프로그램 종료

# pyautogui.click(file_menu_notepad)


def find_target(img_file, timeout):
    start = time.time()  # 시작시간
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()  # 종료시간
        if end - start > timeout:  # 지정한 10초를 초과하면
            break
    return target


def my_click(img_file, timeout=10):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(
            f"[Timeout {timeout}s] Target not found ({img_file}) Terminate program.")
        sys.exit()


my_click("file_menu_notepad.png", 10)
