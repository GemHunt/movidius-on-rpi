# client.py
import socket                   # Import socket module
import time
import cv2
import cPickle as pickle

while True:
    start_time = time.time()
    s = socket.socket()             # Create a socket object
    #host = socket.gethostname()     # Get local machine name
    host = 'rpi1'
    port = 33333
    s.connect((host, port))
    s.send("Hello server!")
    #with open('received.jpg', 'wb') as f:
    data = []

    print '1 in %s seconds' % (time.time() - start_time,)
    never_ran = True
    while True:
        buffer = s.recv(4096)
        data.append(buffer)
        if never_ran:
            print '1.1 in %s seconds' % (time.time() - start_time,)
        never_ran = False
        if not buffer:
            break
    print '2 in %s seconds' % (time.time() - start_time,)

    joined_data = b"".join(data)          # Make the final message
    print '3 in %s seconds' % (time.time() - start_time,)

    s.close()
    frame = pickle.loads(str(joined_data))
    print '4 in %s seconds' % (time.time() - start_time,)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    print '5 in %s seconds' % (time.time() - start_time,)



