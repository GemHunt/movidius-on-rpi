import socket                   # Import socket module
from imutils.video.pivideostream import PiVideoStream
import imutils
from picamera import PiCamera
import time
import pickle

port = 33333                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = ''
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
vs = PiVideoStream(resolution=(320,240), framerate=90).start()
time.sleep(2.0)

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    frame = vs.read()
    data = pickle.dumps(frame)
    conn.send(data)
    print('Done sending image capture. Bytes:' + str(len(data)))
    conn.close()
vs.stop()
