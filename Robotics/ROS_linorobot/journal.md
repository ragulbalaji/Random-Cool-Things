LinoRobot Solo Speed Run
===
#### Ragul Balaji August 2019

Credits to:
- [Original Linorobot repository](https://github.com/linorobot/linorobot/)
- [SOAR Linorobot repository](https://github.com/sutd-robotics/soar-linorobot/)

## Installing an Operating System

I will be using [Ubuntu MATE 18.04.2](https://ubuntu-mate.org/blog/ubuntu-mate-bionic-final-release/) for the aarch32 RPi 3B+. Download and etch it onto a sufficiently large SD card.

Connect to monitor, keyboard & mouse then boot! Continue with basic setup of the Pi. Including some network connectivity.

## Enabling SSH

`sudo systemctl enable ssh` DOES NOT WORK properly. Instead a `sudo dpkg-reconfigure openssh-server` should do the trick. Now we `ip addr` get the IP and connect to it from another machine.