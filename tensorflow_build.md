Build directions for a microSD card image for a Raspberry Pi with movidius.
As of 12/19/17 Movidius is saying you can have the NCS or movidius, but not both. 

**RPi TensorFlow Install:**
** I followed: https://github.com/samjabrahams/tensorflow-on-raspberry-pi**
* Except:
* I made sure I used 3/2/2017 release (Download dated 3/3/2017) 
* I used Win32DiskImager to make it(not NOOBs, because Noobs updated it.) 
* I downloaded 2017-09-07 Raspbian Stretch and wrote a 32GB card with Win32DiskImager
* Turned on the RPi camera and SSH
* Change the local to “Chicago”
* Changed the keyboard to US  (Must!) 
* Change the root password
* I only installed Python 2.7 Steps, not 3.4

**Test the Install:**
https://www.tensorflow.org/install/install_linux#ValidateYourInstallation


**My Next Steps:**
* I am going to keep going and install Keras: 
* Adrian Rosebrock's guide looks great:
https://www.pyimagesearch.com/2017/12/18/keras-deep-learning-raspberry-pi/







