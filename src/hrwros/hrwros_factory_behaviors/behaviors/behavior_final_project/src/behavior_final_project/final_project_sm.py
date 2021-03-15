#!/usr/bin/env python
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

import roslib; roslib.load_manifest('behavior_final_project')
from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from hrwros_factory_states.srdf_state_to_moveit import SrdfStateToMoveit
from hrwros_factory_states.compute_grasp_state import ComputeGraspState
from hrwros_factory_states.moveit_to_joints_dyn_state import MoveitToJointsDynState
from hrwros_factory_states.control_feeder_state import ControlFeederState
from hrwros_factory_states.vacuum_gripper_control_state import VacuumGripperControlState
from hrwros_factory_states.locate_factory_device_state import LocateFactoryDeviceState
from hrwros_factory_states.detect_part_camera_state import DetectPartCameraState
from flexbe_states.subscriber_state import SubscriberState
from hrwros_factory_states.set_conveyor_power_state import SetConveyorPowerState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]
from geometry_msgs.msg import Pose2D
# [/MANUAL_IMPORT]


'''
Created on Sun Oct 07 2018
@author: Carlos Hernandez
'''
class FinalProjectSM(Behavior):
	'''
	Final project for the MOOC Hello (Real) World with ROS
The three robots in the factory move to process the parts
	'''


	def __init__(self):
		super(FinalProjectSM, self).__init__()
		self.name = 'Final Project'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]

		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		names1 = ['robot1_shoulder_pan_joint', 'robot1_shoulder_lift_joint', 'robot1_elbow_joint', 'robot1_wrist_1_joint', 'robot1_wrist_2_joint', 'robot1_wrist_3_joint']
		pick1_group = 'robot1'
		pick2_group = 'robot2'
		robot1_loc = Pose2D(x=-0.2, y=2.03, theta=0.0)
		names2 = ['robot2_shoulder_pan_joint', 'robot2_shoulder_lift_joint', 'robot2_elbow_joint', 'robot2_wrist_1_joint', 'robot2_wrist_2_joint', 'robot2_wrist_3_joint']
		gripper1 = "vacuum_gripper1_suction_cup"
		gripper2 = "vacuum_gripper2_suction_cup"
		robot2_loc = Pose2D(x=-8.2, y=-1.4, theta=0.0)
		# x:9 y:195, x:413 y:347
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.speed = '100.0'
		_state_machine.userdata.robot1_loc = robot1_loc
		_state_machine.userdata.pick2_configuration = []
		_state_machine.userdata.pose_turtlebot = []
		_state_machine.userdata.robot2_loc = robot2_loc

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]

		# [/MANUAL_CREATE]


		with _state_machine:
			# x:87 y:217
			OperatableStateMachine.add('Move R2 to Home',
										SrdfStateToMoveit(config_name='R2Home', move_group=pick2_group, action_topic='/move_group', robot_name=''),
										transitions={'reached': 'Move R1 Home', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1025 y:148
			OperatableStateMachine.add('Compute Pick for R1',
										ComputeGraspState(group=pick1_group, offset=0.0, joint_names=names1, tool_link=gripper1),
										transitions={'continue': 'Activate Gripper 1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose', 'joint_values': 'pick1_configuration', 'joint_names': 'joint_names'})

			# x:885 y:309
			OperatableStateMachine.add('Move R1 to Pick',
										MoveitToJointsDynState(move_group=pick1_group, offset=0.0, tool_link=gripper1, action_topic='/move_group'),
										transitions={'reached': 'Move R1 back Home', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pick1_configuration', 'joint_names': 'joint_names'})

			# x:421 y:15
			OperatableStateMachine.add('Start feeder',
										ControlFeederState(activation=True),
										transitions={'succeeded': 'Wait for part', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:588 y:25
			OperatableStateMachine.add('Stop feeder',
										ControlFeederState(activation=False),
										transitions={'succeeded': 'Stop Conveyor', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:845 y:227
			OperatableStateMachine.add('Activate Gripper 1',
										VacuumGripperControlState(enable=True, service_name='/gripper1/control'),
										transitions={'continue': 'Move R1 to Pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:874 y:578
			OperatableStateMachine.add('Compute place Turtlebot',
										ComputeGraspState(group=pick1_group, offset=0.55, joint_names=names1, tool_link=gripper1),
										transitions={'continue': 'Move R1 to place', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose_turtlebot', 'joint_values': 'place1_configuration', 'joint_names': 'joint_names'})

			# x:890 y:658
			OperatableStateMachine.add('Move R1 to place',
										MoveitToJointsDynState(move_group=pick1_group, offset=0.55, tool_link=gripper1, action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'place1_configuration', 'joint_names': 'joint_names'})

			# x:882 y:494
			OperatableStateMachine.add('LocateTurtlebot',
										LocateFactoryDeviceState(model_name='mobile_base', output_frame_id='world'),
										transitions={'succeeded': 'Compute place Turtlebot', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose_turtlebot'})

			# x:915 y:398
			OperatableStateMachine.add('Move R1 back Home',
										SrdfStateToMoveit(config_name='R1Home', move_group=pick1_group, action_topic='/move_group', robot_name=''),
										transitions={'reached': 'Move R1 Home', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:56 y:468
			OperatableStateMachine.add('Move R2 back Home',
										SrdfStateToMoveit(config_name='R2Home', move_group=pick2_group, action_topic='/move_group', robot_name=''),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1011 y:56
			OperatableStateMachine.add('Locate Part Camera1',
										DetectPartCameraState(ref_frame='robot1_base', camera_topic='/hrwros/logical_camera_1', camera_frame='logical_camera_1_frame'),
										transitions={'continue': 'Compute Pick for R1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose'})

			# x:508 y:144
			OperatableStateMachine.add('Wait for part',
										SubscriberState(topic='/break_beam_sensor_change', blocking=True, clear=False),
										transitions={'received': 'Stop feeder', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:58 y:55
			OperatableStateMachine.add('Move R1 Home',
										SrdfStateToMoveit(config_name='R1Home', move_group=pick1_group, action_topic='/move_group', robot_name=''),
										transitions={'reached': 'Start Conveyor', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:212 y:22
			OperatableStateMachine.add('Start Conveyor',
										SetConveyorPowerState(stop=False),
										transitions={'succeeded': 'Start feeder', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'speed': 'speed'})

			# x:817 y:25
			OperatableStateMachine.add('Stop Conveyor',
										SetConveyorPowerState(stop=True),
										transitions={'succeeded': 'Locate Part Camera1', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'speed': 'speed'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]

	# [/MANUAL_FUNC]
