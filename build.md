# movidius-on-rpi
Build Directions for a microSD card image for a Raspberry Pi with a Movidius Nuerual Compute Stick(NCS). 

**I documented this install afterwards, it’s not great, but a starting place:**
* The best source of information is the forum: https://ncsforum.movidius.com/
* This is an excellent forum comment: https://ncsforum.movidius.com/discussion/comment/1393#Comment_1393
* I downloaded 2017-09-07 Raspbian Stretch and wrote a 32GB card with Win32DiskImager
* Turned on the RPi camera and SSH
* Change the local to “Chicago”
* Changed the keyboard to US  (Must!) 
* Change the root password
* mkdir workspace (Required to because some of the example programs are hardcoded to use this dir) 
* cd workspace

**I followed 12/6/2017 Release:**
* git clone https://github.com/movidius/ncsdk
* Make install
* Make examples

**I followed 12/13/2017 Release:**
* Git clone https://github.com/movidius/ncappzoo
* Make all
* Make run

**I installed scikit-image to run apps/MultiStick_GoogLeNet**
* Sudo pip install scikit-image 
* (Took 3-5 hours) (There has to be a better way!) 

**These apps work great:**
* apps/hello_ncs_py
* apps/birds
* apps/MultiStick_GoogLeNet

**I am guessing it took 6-8 hours to get to this point.**

**I was unsuccessful at getting the stream examples up with a USB webcam:**
* /apps/stream_infer
* /apps/stream_ty_gn
* /apps/stream_ty_gn_threaded
* I tried installing gstreamer with no effect 
* I tried 3 times to run “make opencv”:(1-2 hours): https://github.com/movidius/ncappzoo/tree/master/apps/stream_ty_gn_threaded

**Tips:**
* The examples are in Python3, so you will get errors sometimes if you type python and not python3
* Check if you online. If you lose your internet connection the during install sometimes it's not easy to to understand this was the issue. 


**Questionable Tips:**
* "Questionable" as I am not sure if these are a good ideas or not...

* Check out Adrian Rosebrock's says about swap space in a TensorFlow install: https://www.pyimagesearch.com/2017/12/18/keras-deep-learning-raspberry-pi
* With the movidius repo installs when something did not work I tried again using sudo


**Next steps for me on this build:**
* The RPi is just a better camera than USB because it uses the GPU. This looks easy to get up and running with the NCS. I might write this and send movidius/ncappzoo a pull request. 
* Try a more complex pipeline with OpenCV functions and NCS inference
* Try a USB webcam through other methods
* Find out if Python 2.7 or 3.4 or both are needed? 


**Next Rebuild for me:**
* Document everything! 
* Should have used 8GB SD Card and or resized the SD Card image: http://www.aoakley.com/articles/2015-10-09-resizing-sd-images.php
* Wait? I am hoping Movidius will seperate ARM/RPi/inferance-only examples this better and hopefully write better RPi Examples. All the TensorFlow API stuff will not work in the examples because TensorFlow can’t be installed. Is there a need to be running API type stuff(compliling the network/profiling) on the RPi?
