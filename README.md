Robotic ARM on Hikey 970
=============================
Motion detection on Hikey-960 allows user to detect motion at any remote location. It also sends images back to the user if a motion is detected with the help of MQTT.

Hardware required:
------------------

  * Hikey 960
  * USB Video Camera
  * PC

Pre-requisites for Hikey960:
----------------------------
This project has these software pre-requisites to run on Hikey960

  * paho-mqtt
  * python3
  * python3-pip
  * OpenCV on python3
  
Except for OpenCV on python3 all the other pre-requisites can be installed by running these commands

```
$ sudo apt-get update
$ sudo apt install python3-dev python3-pip
$ pip3 install imutils paho-mqtt
```

Pre-requisites for PC/Laptop:
-----------------------------
This project has these software pre-requisites to run on PC/Laptop.

  * paho-mqtt
  * python3
  * python3-pip
  
All the pre-requisites can be installed by running these commands

```
$ sudo apt-get update
$ sudo apt install python3-dev python3-pip
$ pip3 install paho-mqtt
```

Steps for the Motion Detection Demo:
------------------------------------
To run Run a demo of this project please follow these steps.
We assume that you have already installed the pre-requisites before following these steps

Step 1 : Cloning the Project
----------------------------
on PC/Laptop run command to clone this project
```
$ git clone https://github.com/shunyaos/motion_detection.git
```
on Hikey960 run command to clone this project
```
$ git clone https://github.com/shunyaos/motion_detection.git
```
Step 2: Starting MQTT on PC/Laptop
----------------------------------
Run the mqtt_client_demo.py present in the pc folder
```
$ cd motion_detection/pc
$ python3 mqtt_client_demo.py
```
Step 3: Starting the Demo on Hikey960
-------------------------------------
Run the Demo program
```
$ python3 motion_detector.py
```
As soon as you run the code the first frame is taken as frame of reference. 
As any motion is detected from the first frame of reference it captures an image and sends it back to the user through MQTT.
