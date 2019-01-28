Robotic ARM on Hikey 970
=============================
This project contains demo code to interface and run Robotic Arm on Hikey 970. 

Hardware required:
------------------

  * Hikey 970
  * U-Arm Swift Pro

Pre-requisites for Hikey970:
----------------------------
For this project to run you need to flash Lebian 9 with u-Arm support.
Please downolad it from this link - https://www.dropbox.com/s/ushxts1u2fs0djv/hikey970-lebian-9-uArm.tar.gz?dl=0

Steps for the Motion Detection Demo:
------------------------------------
To run Run a demo of this project please follow these steps.
We assume that you have already installed the pre-requisites before following these steps

Step 1 : Cloning the Project
----------------------------
on Hikey970 run command to clone this project
```
$ git clone https://github.com/shunyaos/roboArmDemo.git
```
Step 2: Connect the Robotic Arm
----------------------------------
Connect the Robotic Arm to Hikey970
And power on.

Step 3: Setup
----------------------------------
Run these commands
```
$ cd roboArmDemo
$ ./setup.sh
```
Step 4: Starting the Demo on Hikey970
-------------------------------------
Run the Demo program
```
$ python3 pick-place.py
```
As soon as you run the code your Robotic Arm should move.
