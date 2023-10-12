import cv2

image = cv2.imread(r"c:\Users\ImanHamrah\Desktop\surprise_face.jpg")
image = cv2.resize(image,(300,500))
image = cv2.rectangle(image, (190,80),(90,180),(0, 0, 0), (5))
image = image[75:200,75:205]
cv2.imwrite(r"c:\Users\ImanHamrah\Desktop\surprise_face.jpg", image)
cv2.imshow("surprise face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
