A quick example of classifying images with the Pi Camera and NCS. 

**How to use:**
* git clone https://github.com/GemHunt/movidius-on-rpi
* pip install imutils

**server.py captures from the camera and serves them via a socket:**
* python server.py

**image-classifier.py infers them using the movidius NCS**
* python3 image-classifier.py 
* Do notice that this is Python3 and the server is in python2
* This can be run on a different computer by changing host value in the script

**The offical site, by far, has the best information and samples:**
* http://picamera.readthedocs.io/en/release-1.13/recipes2.html?highlight=jpg#rapid-capture-and-streaming
