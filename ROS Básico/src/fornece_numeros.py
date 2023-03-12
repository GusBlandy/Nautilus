#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32
import random

class Gerador():
    def __init__(self):
        rospy.init_node('numeros', anonymous=True)
        self.pub = rospy.Publisher('modulos', Vector3, queue_size=10)
        self.list = list(range(10))
        self.resultado = rospy.Subscriber('resultado', Float32, self.callback)
    
    def start(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            p = Vector3()
            p.x = random.choice(self.list)
            p.y = random.choice(self.list)
            p.z = random.choice(self.list)
            # rospy.loginfo(p)
            self.pub.publish(p)
            rate.sleep()

    def callback(self, msg):
        resultado_final = Float32()
        resultado_final = msg
        print(f'O módulo do vetor é: {resultado_final.data}')        

if __name__ == '__main__':
    c = Gerador()
    c.start()