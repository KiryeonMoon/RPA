# pyautogui는 영문과 숫자만 지원하므로 한글 자동 작성은 안된다.
# 한글 입력 안 되는 문제를 해결하려면 pyperclip 패키지 설치
import pyperclip  # 어떤 문장을 클립보드에 집어넣는 패키지
import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0]  # 메모장 1개 띄운 상태
w.activate()  # 창 활성화

pyautogui.write("kiryeon ")  # 내용 작성
# 내용작성에서는 시간 텀 줄 때 duration 말고 interval 사용
# 글자 한 칸 한 칸 간극이므로 너무 값을 크게 하면 이상함
pyautogui.write("wants to see you Naong ", interval=0.1)

# 리스트 형태로도 입력 가능
# 화살표의 경우 right/left 등 우리가 아는 영문으로 입력
pyautogui.write(["t", "e", "s", "t", "left",
                 "left", "right", "l", "a", "enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번, 1 a 순서대로 적고 enter

# 특수문자
# shift키 누른 상태에서 숫자 4 입력하고 shift키 뗀다.
# pyautogui.keyDown("shift")
# pyautogui.press("4")  # 눌렀다 떼는 동작
# pyautogui.keyUp("shift")

# 조합기 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")  # press "a"
# pyautogui.keyUp("ctrl")  # Ctrl + A 구현

# 조합기 위에처럼 쓰기 힘드니까 있는 간단한 방법
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# Ctrl 누르고 Alt 누르고 Shift 누르고 A 누르고 A 떼고 Shift 떼고 Alt 떼고 Ctrl 떼는 순서

# # "문기련" 글자를 클립보드에 저장
# pyperclip.copy("문기련")
# # 이 문장을 그대로 붙여넣기하면 한글 쓰는 효과를 낼 수 있는 셈!!
# pyautogui.hotkey("ctrl", "v")


def my_write(text):  # 위에처럼 매번 복붙 두 줄로 쓰기 귀찮다면 아예 함수로 만들면 된다.
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


my_write("문기련짱짱맨")
