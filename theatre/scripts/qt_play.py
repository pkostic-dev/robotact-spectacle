#! /usr/bin/env python3
# coding: utf-8

import roslib

import select
import sys
import termios
import tty

import actionlib
import rospy
from std_msgs.msg import Float64MultiArray, String
from theatre.msg import QTBehaviorAction, QTBehaviorGoal

import qt_states.qt_default as qt_default
import qt_states.qt_simple as qt_simple
import qt_states.qt_drague as qt_drague
import qt_states.qt_oz as qt_oz
import qt_states.qt_imitation as qt_imitation
import qt_states.qt_emotions as qt_emotions
import spectacle.scene_1 as scene_1
import spectacle.scene_2 as scene_2
import spectacle.scene_5_6 as scene_5_6
import spectacle.scene_10 as scene_10
import spectacle.scene_11_12 as scene_11_12

roslib.load_manifest('theatre')

TRIGGER_KEY = 0
TRIGGER_VALUE = 1
TRIGGER_NEXT_STATE = 2

STATE_BEHAVIOR = 0
STATE_TRIGGERS = 1

FIRST_TRIGGER = 0

def get_key(key_timeout):
    file_descriptor = sys.stdin.fileno()
    old = termios.tcgetattr(file_descriptor)
    tty.setraw(file_descriptor)
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    key = ''
    if rlist:
        key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)
    return key


class QTPlay:
    def __init__(self):
        self.rate = rospy.Rate(10) # 10hz

        self.keyboard_publisher = rospy.Publisher('/keyboard', String, queue_size=10)
        self.state_publisher = rospy.Publisher('/robot_state', String, queue_size=10)

        self.gesture_subscriber = rospy.Subscriber('/gesture', String, self.gesture_callback)
        self.human_position = rospy.Subscriber('/human_position', String, self.human_position_callback)

        print(sys.version)

        # STATE FORMAT
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
        self.states = {}
        # self.add_states(scene_1.qt_states)
        # self.add_states(scene_2.states)
        # self.add_states(scene_5_6.qt_states)
        self.add_states(scene_1.qt_states)
        # self.add_states(qt_emotions.states)
        self.state = 'begin'

        self.head_publisher = rospy.Publisher(
            '/qt_robot/head_position/command',
            Float64MultiArray,
            queue_size=1
            )
        self.left_arm_publisher = rospy.Publisher(
            '/qt_robot/left_arm_position/command',
            Float64MultiArray,
            queue_size=1
            )
        self.right_arm_publisher = rospy.Publisher(
            '/qt_robot/right_arm_position/command',
            Float64MultiArray,
            queue_size=1
            )

        begin_state_duration = self.states[self.state][STATE_TRIGGERS][FIRST_TRIGGER][TRIGGER_VALUE]
        rospy.Timer(
            rospy.Duration(begin_state_duration),
            self.time_callback,
            oneshot=True
        )
        print(self.state)


    def time_callback(self, _):
        print('time callback')
        triggers = self.states[self.state][STATE_TRIGGERS]
        for trigger in triggers:
            if trigger[TRIGGER_KEY] == 'time':
                self.state = trigger[TRIGGER_NEXT_STATE]
                print('next_state: ' + self.state)
                self.next_state()
                break
    

    def keyboard_callback(self, key):
        print('keyboard callback: ' + key)
        triggers = self.states[self.state][STATE_TRIGGERS]
        for trigger in triggers:
            if trigger[TRIGGER_KEY] == 'key':
                if trigger[TRIGGER_VALUE] == key:
                    self.state = trigger[TRIGGER_NEXT_STATE]
                    print('next_state: ' + self.state)
                    self.next_state()
                    break


    def gesture_callback(self, gesture):
        print('gesture callback: ' + gesture.data)
        triggers = self.states[self.state][STATE_TRIGGERS]
        for trigger in triggers:
            if trigger[TRIGGER_KEY] == 'gesture':
                if trigger[TRIGGER_VALUE] == gesture.data:
                    self.state = trigger[TRIGGER_NEXT_STATE]
                    print('next_state: ' + self.state)
                    self.next_state()
                    break

    def human_position_callback(self, human_position):
        print('human_position callback: ' + human_position.data)
        triggers = self.states[self.state][STATE_TRIGGERS]
        for trigger in triggers:
            if trigger[TRIGGER_KEY] == 'gesture':
                if trigger[TRIGGER_VALUE] == human_position.data:
                    self.state = trigger[TRIGGER_NEXT_STATE]
                    print('next_state: ' + self.state)
                    self.next_state()
                    break


    def next_state(self):
        if (self.state != 'end'):
            self.state_publisher.publish(self.state)
            # Send behavior dictionary
            behavior = self.states[self.state][STATE_BEHAVIOR]
            if(len(behavior)):
                # AL machine => pass to smach
                # NOTE: no idea what the comment above means
                print(self.state + ' =bhw=> ' + str(behavior))

                # Simple publishers throught ROS
                if 'h' in behavior:
                    self.head_publisher.publish(Float64MultiArray(data=behavior['h']))
                if 'la' in behavior:
                    self.left_arm_publisher.publish(Float64MultiArray(data=behavior['la']))
                if 'ra' in behavior:
                    self.right_arm_publisher.publish(Float64MultiArray(data=behavior['ra']))
                
                # actionlib send goal
                if ('e' in behavior) or ('g' in behavior) or ('s' in behavior):
                    client = actionlib.SimpleActionClient('/qt_behave', QTBehaviorAction)
                    client.wait_for_server()

                    goal = QTBehaviorGoal(
                        emotion=behavior['e'] if 'e' in behavior else '',
                        gesture=behavior['g'] if 'g' in behavior else '',
                        speech=behavior['s'] if 's' in behavior else ''
                        )
                    client.send_goal(goal)
                    # ...
                    client.wait_for_result()
                    
                    client.get_result()


            # prepare jump for next state
            triggers = self.states[self.state][STATE_TRIGGERS]
            print(self.state + ' =trig=> ' + str(triggers))
            for trigger in triggers:
                if trigger[TRIGGER_KEY] == 'time':
                    rospy.Timer(rospy.Duration(trigger[TRIGGER_VALUE]), self.time_callback, oneshot=True)


    def execute(self):
        while not rospy.is_shutdown():
            if self.state == 'end':
                break
            key = get_key(0.1)
            if (len(key)):
                self.keyboard_callback(key)
            self.rate.sleep()

    
    def add_states(self, states:dict):
        self.states.update(states)


if __name__ == '__main__':
    rospy.init_node('qt_play')

    qt_play = QTPlay()
    qt_play.execute()


