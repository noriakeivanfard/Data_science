import cv2
import cvzone

img = cv2.imread("img/happy_face.jpg")
h, w, _ = img.shape
img_r = cv2.resize(img, (300,400))

# change face 
face2 = cv2.imread("img/sad_face.png",cv2.IMREAD_UNCHANGED)
face2 = cv2.resize(face2, (180, 60))
face = img_r[50:500,50:500]
img_r[50:500,50:500] = cvzone.overlayPNG(face, face2)
cv2.imwrite(r"c:\Users\Shirin\Desktop\change_face.jpg", img_r)
cv2.imshow(None, img_r)
cv2.waitKey(0) 

