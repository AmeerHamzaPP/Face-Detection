import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Output.avi', fourcc,20.0,(640,480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame(stream end?).Exiting.....")
        break
    out.write(frame)
    cv.imshow("Press ESC key to terminate the Window",frame)
    key = cv.waitKey(1)
    if key == 27:
        break  

cap.release()
out.release()
cv.destroyAllWindows()