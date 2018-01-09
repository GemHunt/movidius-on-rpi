# movidius-on-rpi

**MORP:  Movidius On Raspberry Pi**
This repo about using Movidius neural compute sticks(NCS) on the Raspberry Pi.

It is the ongoing result of a series Meetups I have been hosting for Chicago Area Embedded Deep Learning:
https://www.meetup.com/Chicago-Area-Embedded-Deep-Learning


**As of 12/19/17 Movidius is saying you can have the NCS or TensorFlow, but not both:**
* [Build directions for a microSD card image for a Raspberry Pi with a Movidius Neural Compute Stick(NCS).](build.md)
* [Build directions for a microSD card image with Raspberry Pi with Tensorflow](tensorflow_build.md)

**Slides from a very short demo I gave:**
* [Movidius NCS on RPi Demo.pdf](movidius_ncs_on_rpi_demo.pdf)
* [Movidius NCS on RPi Demo.pptx](movidius_ncs_on_rpi_demo.pptx)

**FAQ:**
**What are the Movidius links?:**
* https://ncsforum.movidius.com/
* https://github.com/movidius/ncappzoo
* https://github.com/movidius/ncsdk

**What hardwhere do I need to get into this?**
* Really you need a Ubuntu 14.04 PC, RPi, and NCS.

**What does it do?**
* Infers(runs the computational graph) a Tensorflow or caffe model.

**What are some NCS+RPI pros and cons?**
* **Pros:**
* Power usage(2 Watts NCS+RPI)
* Size and wieght 
* It's the first ASIC out so there is nothing to compare it to at this point
* It's true edge device (no internet needed & appliance like) 
* RPI is very popular
* 15x quicker than RPI along on Deep Learning inferance.
* **Cons:**
* First one out: so limited support & could have much more power
* You can't access the Myraid 2 VPU with all the computer vision functionality
* Cost is high for what your getting (It's less than one thread on a CPU) 
* If power and size are not an issue an old PC is more cost effective and easier to use. 


**How does the NCS compare to the Google AIY Vision Kit?**
* https://aiyprojects.withgoogle.com/vision#list-of-materials
* Not sure yet, I ordered three of them
* The Google AIY Vision kit is a hat/bonnet that sits on top of a RPi Zero

**More FAQ's to Come


Thanks!
Paul Krush
630-830-6640


