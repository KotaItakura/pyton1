import cv2

img_path = "image//kaoga.jpg"

img = cv2.imread(img_path)

# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# 上のリンクの内容をコピーしてxmlファイルを作成する
face_cascade_path = "image/copy.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)
# ↑機械学習でいうモデル

# グレー画像を作成
src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#　検出
faces = face_cascade.detectMultiScale(src_gray)
face = faces[0]

cv2.rectangle(img,
              pt1=(face[0], face[1]), #左上の座標
              pt2=(face[2], face[3]), #右下の座標
              color=(255, 255, 0),
              thickness=3,
              lineType=cv2.LINE_4,
              shift=0)

cv2.imshow('rectangle', img)
cv2.waitKey(0)