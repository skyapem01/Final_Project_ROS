#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
def callback(data):
    #rospy.loginfo( data.data)
    print(data.data)
    print(type(data))
    print(type(data.data))
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/go_home", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
