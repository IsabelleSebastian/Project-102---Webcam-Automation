import cv2

def Takescreen():
    vcobject = cv2.VideoCapture(0)

    result = True
    while (result):
        ret, frame = vcobject.read()

        cv2.imwrite("newImage.png" , frame)
        result = False

    vcobject.release()
    cv2.destroyAllWindows()


Takescreen()



