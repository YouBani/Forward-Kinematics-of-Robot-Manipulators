import numpy as np
from math import pi, cos, sin, atan2, sqrt

def forward_kinematics(joints):
    # input: joint angles [joint1, joint2, joint3]
    # output: the position and orientation of joint 4 (as the end-effector):
    # [x, y, z, roll, pitch, yaw]

    joint1 = joints[0]
    joint2 = joints[1]
    joint3 = joints[2]

    l1 = 65
    l2 = 38.9
    l3 = 150
    l4 = 150
    l5 = 50
    a = 1.249

    dh_table = [[joint1, l1+l2, 0, -pi/2], [joint2-a, 0, 158.1, pi], [joint3-a, 0, 150, pi/2]]
    
    T = np.identity(4)

    for line in dh_table:
        A = [[cos(line[0]), -sin(line[0])*cos(line[3]), sin(line[0])*sin(line[3]), (line[2])*(cos(line[0]))],
        [sin(line[0]), (cos(line[0]))*(cos(line[3])), (-cos(line[0]))*(sin(line[3])), (line[2])*(sin(line[0]))],
        [0, sin(line[3]), cos(line[3]), line[1]],
        [0, 0, 0, 1]]
        T = np.dot(T, A)

    x = round(T[0][3]/1000, 3)
    y = round(T[1][3]/1000, 3)
    z = round(T[2][3]/1000,3)
    yaw = atan2(T[1][0], T[0][0])
    roll = atan2(T[2][1], T[2][2])
    pitch = atan2(-T[2][0], sqrt((T[2][1]**2)+(T[2][2]**2)))

    # add your code here to complete the computation

    # convert the final orientation of the end-effector to roll-pitch-yaw

    return [x, y, z, roll, pitch, yaw]