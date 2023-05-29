#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy

def user_trigger():
    rospy.wait_for_service('/go_home')
    try:
        trigger = rospy.ServiceProxy('/go_home', Empty)
        print("Please do something.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    user_trigger()
