#! /usr/bin/env python3

import roslib
roslib.load_manifest('theatre')
import rospy
import actionlib

import sys

from std_msgs.msg import String
from theatre.msg import QTBehaviorAction

class QTBehaveServer:
    def __init__(self):
        print(sys.version)
        self.server = actionlib.SimpleActionServer('qt_behave', QTBehaviorAction, self.execute, False)

        self.pub_emotion = rospy.Publisher('qt_robot/emotion/show', String, queue_size=1)
        self.pub_gesture = rospy.Publisher('qt_robot/gesture/play', String, queue_size=1)
        self.pub_speech = rospy.Publisher('/qt_robot/speech/say', String, queue_size=1)
        self.pub_bhw_speech = rospy.Publisher('/qt_robot/behavior/talkText', String, queue_size=1)

        print("Starting actionlib server...")
        self.server.start()
        print("Server started!")


    def execute(self, goal):
        print('Executing goal :')
        print(goal)
        print("\n")

        self.pub_emotion.publish(goal.emotion)
        self.pub_gesture.publish(goal.gesture)

        if goal.speech.startswith('~'):
            self.pub_bhw_speech.publish(goal.speech[1:])
        else:
            self.pub_speech.publish(goal.speech)

        self.server.set_succeeded()



if __name__ == '__main__':
    rospy.init_node('qt_behave')
    server = QTBehaveServer()
    rospy.spin()

