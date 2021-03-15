#!/bin/bash

while ! ping -c 1 -W 1 google.com
do 
    echo Trying to connect Ethernet \(google.com\)...
    sleep 1
done

sudo apt update -y
sudo apt upgrade -y

sudo apt install -y ros-melodic-desktop-full

sudo apt install -y ros-melodic-ompl libglew-dev ros-melodic-eigenpy ros-melodic-tf2-geometry-msgs ros-melodic-moveit-msgs ros-melodic-random-numbers ros-melodic-eigen-stl-containers ros-melodic-navigation ros-melodic-rosparam-shortcuts ros-melodic-geometric-shapes ros-melodic-object-recognition-msgs ros-melodic-srdfdom ros-melodic-moveit ros-melodic-octomap-msgs ros-melodic-warehouse-ros

# sudo apt-get purge -y libgazebo9-dev
# sudo apt-get install -y libgazebo9-dev
# sudo apt install -y ros-melodic-desktop-full


