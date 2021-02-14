import pyautogui

size = pyautogui.size()  # 현재 화면의 스크린 사이즈를 가져옴
print(size)  # 가로, 세로 크기를 알 수 있다.
# size[0] = width
# size[1] = height
# desktop 자동화의 경우, 윈도우에서 제공하는 오브젝트 정보가 아닌 이미지 기반 처리
# 클릭하려는 부분에 대해 이미지를 따 와서 파일로 저장하고 그 이미지를 화면에서 찾아서 처리하는 방식
