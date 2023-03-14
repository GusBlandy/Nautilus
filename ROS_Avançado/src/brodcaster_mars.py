#!/usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs
import math

if __name__ == '__main__':
    rospy.init_node('star3')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.frame_id = rospy.get_param("/sun/name")
    t.child_frame_id = rospy.get_param("/mars/name")
    rospy.loginfo(t)


    rate = rospy.Rate(10)
    rospy.loginfo(t)
    while not rospy.is_shutdown():
        time = rospy.Time.now().to_sec()

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = 3.0 * math.cos(0.5*time)
        t.transform.translation.y = 3.0 * math.sin(0.5*time)
        t.transform.translation.z = 0.0 

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        rospy.loginfo(t)

        br.sendTransform(t)
        rate.sleep()
