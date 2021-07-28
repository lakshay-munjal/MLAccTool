import cv2
# import os
# from fastai.vision import *


import subprocess

def doThis(pred):
    if pred.obj == 'V':
        subprocess.call(["C:\\Program Files (x86)\\Steam\\steam.exe"])
    # elif pred == 'W':
        #todo
    # elif pred == 'A':
        #todo
        
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    

    c = cv2.waitKey(3000)
    if c == 27:
        break
    # path = os.path.dirname(os.path.abspath(__file__))
    # learn = load_learner(path)
    cv2.imwrite('test1.jpg',frame)
    img = open_image('./test1.jpg')
    pred_class,index,prob = learn.predict(img)
    # print(pred_class, prob)
    #cv2.putText(frame, "Prob = {0:.4f}".format(torch.max(prob).item()), (380, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    print(pred_class)
    print(torch.max(prob).item())
    cv2.imshow('Input', frame)
    if torch.max(prob).item() > 0.9:  
          doThis(pred_class)


cap.release()
cv2.destroyAllWindows()

