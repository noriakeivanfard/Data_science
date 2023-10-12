import cv2

image = cv2.imread(r"c:\Users\ImanHamrah\Desktop\sad_face.jpg")
image = cv2.resize(image,(300,500))
image = cv2.rectangle(image, (200,75),(90,150),(0, 0, 0), (5))
image = image[75:200,75:205]
cv2.imwrite(r"c:\Users\ImanHamrah\Desktop\sad_face.jpg", image)
cv2.imshow("sad_face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
