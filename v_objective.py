#!/usr/bin/env python
import rospy
import math 
from geometry_msgs.msg import PoseStamped
total_count = 0
success_count = 0
list = []

def objective_pose_callback(data):
    global total_count
    global success_count
    total_count += 1
    if math.fabs(data.pose.orientation.w) < 0.99 :
        list.append(2*math.acos(data.pose.orientation.w)/math.pi*180) 
        success_count += 1
def listener():
    rospy.init_node("objective_pose_listener")
    rospy.Subscriber("/objective_pose", PoseStamped, objective_pose_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    total_value = 0.0
    total_square = 0.0
    index = 0
    while (index < success_count):
        total_value += list[index]
        total_square  += list[index] * list[index]
        index += 1

    total_value = total_value / success_count
    total_square = total_square /success_count - total_value * total_value
    print "result:%d,%d,%f,%f" %(success_count,total_count,total_value,total_square)
    
