#! /usr/bin/env python
# coding: utf-8

import roslib
roslib.load_manifest('theatre')
import rospy
import rospkg
import actionlib

import theatre.msg


import wave
import json
import time as t


rospy.init_node('naogpt')

client = actionlib.SimpleActionClient('/nao_behave', theatre.msg.NaoBehaviorAction)
client.wait_for_server()
goal = theatre.msg.NaoBehaviorGoal( gesture='curious',
                                    speech='')
client.send_goal(goal)
client.wait_for_result()
result = client.get_result()
