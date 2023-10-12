import cv2

image = cv2.imread(r"c:\Users\ImanHamrah\Desktop\angry_face.jpg")
image = cv2.resize(image,(300,500))
image = cv2.rectangle(image, (185,50),(100,130),(0, 0, 0), (5))
image = image[50:200,50:205]
cv2.imwrite(r"c:\Users\ImanHamrah\Desktop\angry_face.jpg", image)
cv2.imshow("angry_face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
