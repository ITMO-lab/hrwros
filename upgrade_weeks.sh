#!/bin/bash

while ! ping -c 1 -W 1 courses.edx.org
do 
    echo Trying to connect with courses.edx.org...
    sleep 1
done

rm -rf downloads
mkdir downloads
cd downloads
wget https://courses.edx.org/assets/courseware/v1/005dcd7316857c65b775f2618a75614f/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/hrwros_week1_v09.zip
wget https://courses.edx.org/assets/courseware/v1/763028299eb0d9a54a69e01365c37e60/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/hrwros_week2_v09.zip
wget https://courses.edx.org/assets/courseware/v1/046c201166c8a9b100c94dbb224f5144/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/hrwros_week3_v09.zip
wget https://courses.edx.org/assets/courseware/v1/efd240b812bd55cd0029c63ee736a9ee/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/hrwros_week4_v09.zip
wget https://courses.edx.org/assets/courseware/v1/f9e8041ff40aa1bbb85fe196741af99e/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/hrwros_week5_v09.zip
wget https://courses.edx.org/assets/courseware/v1/3d1a3ea65d1a167ddca724896c37b586/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/hrwros_week6_v09.zip
unzip -o hrwros_week1*.zip
unzip -o hrwros_week2*.zip
unzip -o hrwros_week3*.zip
unzip -o hrwros_week4*.zip
unzip -o hrwros_week5*.zip
unzip -o hrwros_week6*.zip
rm -rf *.zip
rm -rf ../src/hrwros*
mkdir -p ../src/hrwros
mv * ../src/hrwros/
cd ..
rm -rf downloads

