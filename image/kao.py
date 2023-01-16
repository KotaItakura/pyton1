import cv2

img_path = "image\kaoga.jpg"
img_path = "/Users/itakurakota/Desktop/python lesson/image/kaoga.jpg"

img = cv2.imread(img_path)

print(img.shape)

cv2.imshow("img", img)
cv2.waitKey(0)