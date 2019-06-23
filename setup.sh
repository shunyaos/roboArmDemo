#!/bin/bash

# install u-Arm python SDK
# install instructions are given on the uArm-Python-SDK Repository

git clone https://github.com/uArm-Developer/uArm-Python-SDK.git
cd uArm-Python-SDK
sudo python3 setup.py install 


if [ -e /dev/ttyACM0 ];
then

	sudo chmod 777 /dev/ttyACM0
else
	echo "WARNING : "
	echo "You may not have connected u-Arm to the device."
	echo "Please connect the device and Run command "
	echo "sudo chmod 777 /dev/ttyACM0 "
fi
