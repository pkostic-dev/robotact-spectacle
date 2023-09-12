#! /usr/bin/env python3
# coding: utf-8

import roslib
roslib.load_manifest('theatre')
import rospy
import actionlib

from std_msgs.msg import String

from geometry_msgs.msg import Twist
from theatre.msg import NaoBehaviorAction
from theatre.msg import NaoBehaviorGoal

import sys, select, termios, tty

import nao_states.nao_oz as nao_oz
import nao_states.nao_default as nao_default
import nao_states.nao_all as nao_all
import nao_states.nao_choices as nao_choices
import theatre.scripts.spectacle.scene_5 as scene_5

#nao
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed

TRIGGER_KEY = 0
TRIGGER_VALUE = 1
TRIGGER_NEXT_STATE = 2

STATE_BEHAVIOR = 0
STATE_TRIGGERS = 1

FIRST_TRIGGER = 0

stdin_settings = termios.tcgetattr(sys.stdin)

def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, stdin_settings) #NOTE : AJOUTE DES TABULATIONS
    return key


class NaoPlay:
    def __init__(self):
        self.rate = rospy.Rate(10) # 10hz

        self.keyboard_pub = rospy.Publisher('/keyboard', String, queue_size=10)
        self.state_pub = rospy.Publisher('/robot_state', String, queue_size=10)

        # 'state' : (
        #   {
        #       g: gesture,
        #       s: say,
        #       h: [head],
        #       la: [left_arm],
        #       ra: [right_arm],
        #       w: [x, y, z, ex, ey, ez]
        #   },
        #   [
        #       (trigger, param, next_state)
        #   ]
        # )
        self.states = nao_all.states
        self.add_states(scene_5.nao_states)

        self.state = 'begin'

        self.angles_pub = rospy.Publisher('/joint_angles', JointAnglesWithSpeed, queue_size=10)
        self.walk_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        begin_state_duration = self.states[self.state][STATE_TRIGGERS][FIRST_TRIGGER][TRIGGER_VALUE]
        rospy.Timer(
            rospy.Duration(begin_state_duration),
            self.time_callback,
            oneshot=True)
        print(self.state)


    def time_callback(self, event):
        # go to next state
        print('time callback')
        triggers = self.states[self.state][STATE_TRIGGERS]
        for trigger in triggers:
            if trigger[TRIGGER_KEY] == 'time':
                self.state = trigger[TRIGGER_NEXT_STATE]
                print('next_state: ' + self.state)
                self.next_state()
#        self.state = self.states[self.state][2]
#        pass

    def keyboard_callback(self, key):
        print('keyboard callback: ' + key)
        self.keyboard_pub.publish(key)
        triggers = self.states[self.state][STATE_TRIGGERS]
        for trigger in triggers:
            if trigger[TRIGGER_KEY] == 'key':
                if trigger[TRIGGER_VALUE] == key:
                    self.state = trigger[TRIGGER_NEXT_STATE]
                    print('next_state: ' + self.state)
                    self.next_state()
                    break
#        pass

    def next_state(self):
        if(self.state != 'end'):
            self.state_pub.publish(self.state)
            # send bhw
            bhw = self.states[self.state][STATE_BEHAVIOR]
            if(len(bhw)):
                # AL machine => pass to smach
                print(self.state + ' =bhw=> ' + str(bhw))

                if 'h' in bhw:
                    self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['HeadYaw', 'HeadPitch'], joint_angles=bhw['h'], speed=0.25))
                if 'la' in bhw:
                    self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand'], joint_angles=bhw['la'], speed=0.25))
                if 'ra' in bhw:
                    self.angles_pub.publish(JointAnglesWithSpeed(joint_names=['RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand'], joint_angles=bhw['ra'], speed=0.25))
                if ('g' in bhw) or ('s' in bhw):
                    client = actionlib.SimpleActionClient('/nao_behave', NaoBehaviorAction)
                    client.wait_for_server()

                    goal = NaoBehaviorGoal( gesture=bhw['g'] if 'g' in bhw else '',
                                            speech=bhw['s'] if 's' in bhw else '')
                    client.send_goal(goal)
                    # ...
                    client.wait_for_result()
                    result = client.get_result()
                if 'w' in bhw:
                    cmd_vel = Twist()
                    cmd_vel.linear.x=bhw['w'][0]
                    cmd_vel.linear.y=bhw['w'][1]
                    cmd_vel.linear.z=bhw['w'][2]
                    cmd_vel.angular.x=bhw['w'][3]
                    cmd_vel.angular.y=bhw['w'][4]
                    cmd_vel.angular.z=bhw['w'][5]
                    self.walk_pub.publish(cmd_vel) 


            # prepare jump for next state
            triggers = self.states[self.state][STATE_TRIGGERS]

            print(self.state + ' =trig=> ' + str(triggers))
            for trigger in triggers:
                if trigger[TRIGGER_KEY] == 'time':
                    rospy.Timer(rospy.Duration(trigger[TRIGGER_VALUE]), self.time_callback, oneshot=True)


    def execute(self):
        while not rospy.is_shutdown():
            if self.state == 'end': break
            key = getKey(0.1)
            if (len(key)):
                self.keyboard_callback(key)
            self.rate.sleep()

    def add_states(self, states:dict):
        self.states.update(states)





if __name__ == '__main__':
    rospy.init_node('nao_play')

    nao_play = NaoPlay()
    nao_play.execute()


