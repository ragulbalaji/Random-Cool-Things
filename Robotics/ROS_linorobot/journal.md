LinoRobot Solo Speed Run
===
#### Ragul Balaji August 2019

Credits to:
- [Original Linorobot repository](https://github.com/linorobot/linorobot/)
- [SOAR Linorobot repository](https://github.com/sutd-robotics/soar-linorobot/)

## Installing an Operating System

I will be using [Ubuntu MATE 18.04.2](https://ubuntu-mate.org/blog/ubuntu-mate-bionic-final-release/) for the aarch32 RPi 3B+. Download and etch it onto a sufficiently large SD card.

Connect to monitor, keyboard & mouse then boot! Continue with basic setup of the Pi, including some network connectivity.

## Enabling SSH

`sudo systemctl enable ssh` DOES NOT WORK properly.

Instead a `sudo dpkg-reconfigure openssh-server` should do the trick. Now we `ip addr` get the IP and connect over SSH from another machine.

## Making our OS feel like home

I got some decor for the system:
- ZSH
- [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/)
- tmux
- htop
- git
- curl
- pip & pip3

```
sudo apt install zsh tmux htop git curl python-pip python3-pip
```

## Installing ROS

Follow http://wiki.ros.org/melodic/Installation/Ubuntu to get ROS installed.
- Setup your sources.list
- Set up your keys
- Update repos then `sudo apt install ros-melodic-ros-base`
- Initialize rosdep
- Environment setup (I'm using zsh so `/opt/ros/melodic/setup.zsh`)
- Get Dependencies for building packages

## Getting LinoRobot

We are building a 2 wheel drive bot with a RPLIDAR so:
```
git clone https://github.com/linorobot/lino_install
cd lino_install
./install 2wd rplidar
```

An error occurs `E: Unable to locate package python-gudev`
So we get the armhf binary deb from https://launchpad.net/ubuntu/+source/python-gudev

```
wget https://launchpad.net/ubuntu/+archive/primary/+files/python-gudev_147.2-3_armhf.deb
sudo dpkg -i python-gudev_147.2-3_armhf.deb
sudo apt install -f
```
Comment out these ANNOYING lines in the install script
```
# sudo easy_install pip
```
then run `./install 2wd rplidar` again