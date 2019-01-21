#!/bin/bash

sudo insmod /lib/modules/cdc-acm.ko
sudo chmod 777 /dev/ttyACM0
