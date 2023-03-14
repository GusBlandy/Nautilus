#!/usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs
import math

if __name__ == '__main__':
    rospy.init_node('star4')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.frame_id = rospy.get_param("/mars/name")
    t.child_frame_id = rospy.get_param("/fobos/name")
    rospy.loginfo(t)


    rate = rospy.Rate(10)
    rospy.loginfo(t)
    while not rospy.is_shutdown():
        time = rospy.Time.now().to_sec()

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = 1.0 * math.cos(1.8*time)
        t.transform.translation.y = 1.0 * math.sin(1.8*time)
        t.transform.translation.z = 0.0 

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        rospy.loginfo(t)

        br.sendTransform(t)
        rate.sleep()