import socket                   # Import socket module
from imutils.video.pivideostream import PiVideoStream
import imutils
from picamera import PiCamera
import time
import cv2
import pickle


port = 33333                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = ''
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
vs = PiVideoStream(resolution=(160, 120), framerate=90).start()
time.sleep(2.0)

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    #data = conn.recv(1024)
    #print('Server received', repr(data))
    #if repr(data) == 'stop':
        #break
   
    frame = vs.read()
    #frame = imutils.resize(frame, width=400)
    #png_image = cv2.imencode('.jpg', frame)[1].tostring()
    data = pickle.dumps(frame)
    conn.send(data)
    
    #loaded_frame = pickle.loads(str(data))
    #cv2.imshow("Frame", loaded_frame)
    #key = cv2.waitKey(0) & 0xFF
    
    print('Done sending. Bytes:' + str(len(data)))
    #conn.send('Thank you for connecting')
    conn.close()
vs.stop()
