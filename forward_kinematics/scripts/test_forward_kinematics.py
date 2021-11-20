import rospy
import numpy as np 
from math import pi
from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from forward_kinematics import forward_kinematics

class Manipulator():
    def __init__(self):
        rospy.init_node('manipulator')
        rospy.loginfo("Press Ctrl + C to terminate")
        self.rate = rospy.Rate(1000)
        self.joint_pub = rospy.Publisher('/rx150/joint_states', JointState,queue_size=10)
        # prepare joint message to publish
        joint_msg = JointState()
        joint_msg.header = Header()
        joint_msg.name = ['waist', 'shoulder', 'elbow', 'wrist_angle','wrist_rotate', 'gripper', 'left_finger', 'right_finger']
        joint_msg.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.026, -0.026]
        # test cases for forward kinematics
        # test_case = [pi/6, -pi/3, -pi/6] # joint angle in radian
        # test_case = [0, 0, 0]
        # test_case = [-pi/3, pi/4, pi/2]
        test_case = [3*pi/5, -pi/3, -pi/4]

        result = forward_kinematics(test_case)
        print(test_case)
        print(result[0:3])
        print(result[3:6])
        print(np.rad2deg(result[3:6]))

        while not rospy.is_shutdown():
            joint_msg.header.stamp = rospy.Time.now()
            joint_msg.position[0:3] = test_case
            self.joint_pub.publish(joint_msg)
            self.rate.sleep()

if __name__ == '__main__':
    whatever = Manipulator()