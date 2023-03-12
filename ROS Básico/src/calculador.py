#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32
import math

class Receptor_Publicador():
    def __init__(self):
        rospy.init_node('receptor', anonymous=True)
        self.recp = rospy.Subscriber('modulos', Vector3, self.callback)
        self.pub = rospy.Publisher('resultado', Float32, queue_size=10)

    def callback(self, msg):
        x, y, z = msg.x, msg.y, msg.z
        modulo = math.sqrt(x*x + y*y + z*z)
        f = Float32()
        f = modulo
        # print(f'O módulo do vetor é: {f}')
        rospy.loginfo(f)
        self.pub.publish(f)

if __name__ == '__main__':
    r = Receptor_Publicador()
    rospy.spin()