import cv2 

face_cascade = cv2.CascadeClassifier(r'c:\Users\Shirin\Downloads\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
print(cv2.CascadeClassifier.empty(face_cascade))
while True: 
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in image:
        emoji = cv2.imread('image/emoji.png')
        emoji = cv2.resize(emoji, (w, h))
        img[y:y+h, x:x+w] = emoji
        
    cv2.imshow('video', img)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()