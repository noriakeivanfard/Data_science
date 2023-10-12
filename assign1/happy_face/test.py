import cv2

image = cv2.imread(r"c:\Users\ImanHamrah\Desktop\happy face.jpg")
image = cv2.resize(image,(300,500))
image = cv2.rectangle(image, (200,50),(117,130),(0, 0, 0), (5))
image = image[50:200,50:205]
cv2.imwrite(r"c:\Users\ImanHamrah\Desktop\happyface.jpg", image)
cv2.imshow("happy_face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
