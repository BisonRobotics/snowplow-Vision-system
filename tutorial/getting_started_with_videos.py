import cv2

cap = cv2.VideoCapture(0)

#Saving the video - video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#file name, file type, fps, file size
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print (cap.isOpened())
#continuously capture frames
#If the video is open
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        #property id parameter - https://www.youtube.com/redirect?q=https%3A%2F%2Fdocs.opencv.org%2F4.0.0%2Fd4%2Fd15%2Fgroup__videoio__flags__base.html%23gaeb8dd9c89c10a5c63c139bf7c4f5704d&event=video_description&v=-RtVZsCvXAQ&redir_token=h6tcK4S58-A5_m5yQNY1kGVermR8MTU3MTU5Mzg4OUAxNTcxNTA3NDg5
        print (cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print (cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        #grey image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        #break from loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#release the resources
cap.release()
out.release()
cv2.destroyAllWindows()