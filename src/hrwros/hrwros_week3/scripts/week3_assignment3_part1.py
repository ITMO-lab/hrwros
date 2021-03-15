#!/usr/bin/env python
import rospy
import sys
# Brings in the SimpleActionClient
import actionlib
from actionlib_msgs.msg import GoalStatus

# Brings in the messages used by the MoveBase action, including the
# goal message and the result message.
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseActionResult

if __name__ == '__main__':
    # Initialize a ROS Node
    rospy.init_node('move_turtlebot')

    # Create a SimpleActionClient for the move_base action server.
    turtlebot_navigation_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    # Wait until the move_base action server becomes available.
    rospy.loginfo("Waiting for move_base action server to come up...")
    turtlebot_navigation_client.wait_for_server()
    rospy.loginfo("move_base action server is available...")

    # Creates a goal to send to the action server.
    turtlebot_robot1_goal = MoveBaseGoal()

    # Construct the target pose for the turtlebot in the "map" frame.
    turtlebot_robot1_goal.target_pose.header.stamp = rospy.Time.now()
    turtlebot_robot1_goal.target_pose.header.frame_id = "map"
    turtlebot_robot1_goal.target_pose.header.seq = 1
    turtlebot_robot1_goal.target_pose.pose.position.x = <Add-first-goal-Position-X>
    turtlebot_robot1_goal.target_pose.pose.position.y = <Add-first-goal-Position-Y>
    turtlebot_robot1_goal.target_pose.pose.position.z = 0.0
    turtlebot_robot1_goal.target_pose.pose.orientation.x = 0.0
    turtlebot_robot1_goal.target_pose.pose.orientation.y = 0.0
    turtlebot_robot1_goal.target_pose.pose.orientation.z = 0.0
    turtlebot_robot1_goal.target_pose.pose.orientation.w = 1.0

    # Send the goal to the action server.
    try:
        turtlebot_navigation_client.send_goal(turtlebot_robot1_goal)
        rospy.loginfo("Goal sent to move_base action server.")
        rospy.loginfo("Goal position x: %s  y: %s", turtlebot_robot1_goal.target_pose.pose.position.x, turtlebot_robot1_goal.target_pose.pose.position.y)

        # Wait for the server to finish performing the action.
        turtlebot_navigation_client.wait_for_result()

        # Display a log message depending on the navigation result.
        navigation_result_status = turtlebot_navigation_client.get_state()
        if GoalStatus.SUCCEEDED != navigation_result_status:
            rospy.logerr('Navigation to the desired goal failed :( -- Sorry, try again!)')
        else:
            rospy.loginfo('Hooray! Successfully reached the desired goal!')

    except rospy.ROSInterruptException:
        rospy.loginfo("Interrupt received to stop ROS node.")
