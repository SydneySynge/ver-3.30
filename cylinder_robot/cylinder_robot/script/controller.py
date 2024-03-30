#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def controller():
    pub = rospy.Publisher('/robot/control', Twist, queue_size = 10)

    rospy.init_node('talker',anonymous=True)
    #============design your trace below=============
    rate = rospy.Rate(10)
    for i in range(0,10000):
        twist = Twist()
        twist.linear.x=0.050*abs(i-49.5)/(i-49.5)
        twist.linear.y=0.050*abs(i-49.5)/(i-49.5)
        pub.publish(twist)
        rate.sleep()
    sys.exit(0)

if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass

























