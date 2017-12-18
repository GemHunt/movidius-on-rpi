# movidius-on-rpi
**I documented this install afterwards, it’s not great, but it’s a great start for another install:**
* The best source of information is the forum: https://ncsforum.movidius.com/

* I downloaded 2017-09-07 Raspbian Stretch and wrote a 32GB card with Win32DiskImager.
* Turned on the RPi camera and SSH
* Change the local to “Chicago”
* Changed the keyboard to US  (Must!) 
* Change the password
* mkdir workspace
  (Required to because the example programs are hardcoded to use this dir) 
* cd workspace
* With the movidius repo installs when something did not work I tried again using sudo

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

**These apps worked great:**
* apps/hello_ncs_py
* apps/birds
* apps/MultiStick_GoogLeNet

**I was unsuccessful at getting the stream examples up with a USB webcam:**
* /apps/stream_infer
* /apps/stream_ty_gn
* /apps/stream_ty_gn_threaded
* I tried installing gstreamer with no effect 
* I tried 3 times to run “make opencv”:(1-2 hours): https://github.com/movidius/ncappzoo/tree/master/apps/stream_ty_gn_threaded

**Next Steps for me:**
* The RPi is just a better camera than USB because it uses the GPU. This looks easy to get up and running with the NCS. I might write this and send movidius/ncappzoo a pull request. 

**Next Rebuild for me:**
* Document everything! 
* Should have used 8GB SD Card and or resized the SD Card image: http://www.aoakley.com/articles/2015-10-09-resizing-sd-images.php
* Wait? I am guessing Movidius will make this better and hopefully better RPi Examples. All the TensorFlow API stuff will not work in the examples because TensorFlow can’t be installed. Really there is no need to be running API type stuff on the RPi. 

