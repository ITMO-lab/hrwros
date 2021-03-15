#!/usr/bin/env python
## Node to drive the turtlebot in circles.


import rospy
from geometry_msgs.msg import Twist

rospy.init_node('drive_turtlebot_circle')
pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
rate = rospy.Rate(2)
move = Twist()
move.linear.x = 0.2 #Move the robot with a linear velocity in the x axis
move.angular.z = 0.5 #Move the with an angular velocity in the z axis

while not rospy.is_shutdown():
  pub.publish(move)
  rate.sleep()
