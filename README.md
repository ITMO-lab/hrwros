# Hello (Real) World with ROS – Robot Operating System

This is the `/src` file for the course: [Hello (Real) World with ROS – Robot Operating System](https://learning.edx.org/course/course-v1:DelftX+ROS1x+1T2020/home). All the course created ROS package and programming assignment are included.



### Course Outline

- Week 1: ROS Essentials: ROS basic concept ex: rostopic, rosservice, rosaction, launch files 
- Week 2: Build your own robot environment: how to write urdf and how to use simulation tools(gazebo)
- Week 3: Autonomous Navigation: Using gmapping package to create virtue map and navigate turtlebot in simulation environment 
- Week 4: Manipulation: Familiar with [moveit](https://moveit.ros.org/) and manipulation system 
- Week 5: Robot Vision: Play with logistical camera and `/tf` rostopic
- Week 6: Final Project: Using FlexBE to design a behavior system and integrate with previous work



### Installing supported OS - Ubuntu 18.04

Download from [official site] (https://releases.ubuntu.com/18.04/) Desktop image:

https://releases.ubuntu.com/18.04/ubuntu-18.04.5-desktop-amd64.iso 

Then write to a free USB drive using [balenaEtcher](https://www.balena.io/etcher/)

You have to download, install, enjoy Ubuntu. There are a lot of manuals about installation process of Ubuntu on the Internet, so I will not focus on this.



### Installation hrwros_ws

You have to upgrade your system.

```bash
sudo apt update -y
sudo apt upgrade -y

# (Optional) You have to reboot system if kernel was updated.
sudo reboot
```

First step of working with ROS Melodic is installing ROS Melodic (if it is installed then skip this part):

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update -y
sudo apt install -y ros-melodic-desktop-full

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc

sudo apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install -y python-rosdep

sudo rosdep init
rosdep update

# You must reboot system because kernel has just updated.
sudo reboot
```

Second step is cloning catkin workspace.

```bash
CATKIN_WS=~/catkin_workspaces/hrwros_ws # If you want another name or path fell free to replace this environment variable

git clone https://github.com/AquilaUAV/hrwros_ws.git ${CATKIN_WS}
cd ${CATKIN_WS}

# bash upgrade_weeks.sh (Optional) You can upgrade course sources

bash install.sh

catkin_make
echo "source ${CATKIN_WS}/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```



### 2. Installation   



```bash


# You will then need to reboot your system because kernel has just updated.
sudo reboot
```

