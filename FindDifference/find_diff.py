import cv2
import os
import time
import pyautogui
from PIL import ImageChops

# 왼쪽이미지 시작좌표 0,24
# 오른쪽 이미지 시작좌표 963,24

# 이미지 크기
# width 956, height 763

while True:
    result = pyautogui.confirm('틀린 그림 찾기', buttons=['시작', '종료'])
    if result == '종료':
        break
    width, height = 957, 763
    y_pos = 24

    src = pyautogui.screenshot(region=(0, y_pos, width, height))
    # src.save("src.jpg")

    dest = pyautogui.screenshot(region=(964, y_pos, width, height))
    # dest.save("dest.jpg")

    diff = ImageChops.difference(src, dest)
    diff.save('diff.jpg')

    # 파일 생성 대기
    while not os.path.exists('diff.jpg'):
        time.sleep(1)

    # src_img = cv2.imread("src.jpg")
    # dest_img = cv2.imread("dest.jpg")
    diff_img = cv2.imread("diff.jpg")

    gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
    gray = (gray > 15) * gray
    contours, _ = cv2.findContours(
        gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    COLOR = (0, 200, 0)
    for cnt in contours:
        if cv2.contourArea(cnt) > 100:
            x, y, width, height = cv2.boundingRect(cnt)
            # cv2.rectangle(src_img, (x, y), (x + width, y + height), COLOR, 2)
            # cv2.rectangle(dest_img, (x, y), (x + width, y + height), COLOR, 2)
            # cv2.rectangle(diff_img, (x, y), (x + width, y + height), COLOR, 2)

            to_x = x + (width // 2)
            to_y = y + (height // 2) + y_pos
            pyautogui.moveTo(to_x, to_y, duration=0.3)
            pyautogui.click(to_x, to_y)

    # cv2.imshow("src", src_img)
    # cv2.imshow("dest", dest_img)
    # cv2.imshow("diff", diff_img)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
