# Robotic ARM Demo on Shunya OS

This project contains demo code to interface and run Robotic Arm on a
board with Shunya OS.

## Hardware required:

  - SBC with Shunya OS
  - U-Arm Swift Pro

## Software required:

  - git

To install git you can use the following command:

    $ sudo opkg install git

## Steps for running the Motion Detection Demo:

To run Run a demo of this project please follow these steps. We assume
that you have already installed the pre-requisites before following
these steps

## Step 1 : Cloning the Project

On Shunya OS run command to clone this project

    $ git clone https://github.com/shunyaos/roboArmDemo.git

## Step 2: Connect the Robotic Arm

Connect the Robotic Arm to the board with Shunya OS and power on the
robotic arm.

## Step 3: Setup

Run these commands

    $ cd roboArmDemo
    $ ./setup.sh

## Step 4: Starting the Demo

Run the Demo program

    $ python3 pick-place.py

As soon as you run the code your Robotic Arm should move.
