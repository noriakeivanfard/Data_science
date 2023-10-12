import cv2
import cvzone

image_1 = cv2.imread("img/happy_face.jpg")
image_1 = cv2.resize(image_1, (300,500))
image_2 = cv2.imread("img/angry_face.png",cv2.IMREAD_UNCHANGED)
image_2 = cv2.resize(image_2, (170, 90))
img = image_1[50:500,50:500]
image_1[50:500,50:500] = cvzone.overlayPNG(img, image_2)
cv2.imwrite(r"c:\Users\Shirin\Desktop\change_face_3.jpg", image_1)
cv2.imshow("angry_face",image_1)
cv2.waitKey(0) 

