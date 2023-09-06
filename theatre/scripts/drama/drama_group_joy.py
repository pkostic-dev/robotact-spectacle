#! /usr/bin/env python
# coding: utf-8

import roslib
roslib.load_manifest('theatre')
import rospy
import actionlib

from std_msgs.msg import String
import theatre.msg 

import sys, select, termios, tty

stdin_settings = termios.tcgetattr(sys.stdin)

def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, stdin_settings)
    return key


class DramaWaking:
    def __init__(self):
        self.rate = rospy.Rate(10) # 10hz

        # state: ( (emotion, gesture, say), [(trigger, param, next_state)])

        self.states = {  'begin': ((), [('time', 1, 'nuit')] ),
                            'nuit': ( ('QT/confused','QT/imitation/hands-side',''), [('key', 'c', 'décompte')]),
                            'décompte': ( ('QT/happy','QT/neutral',''), [('key', 'c', 'bonne_année')]),
                            'bonne_année': ( ('QT/surprise','QT/happy',''), [('key', 'c', 'alé')]),
                            'alé': ( ('', 'QT/happy', '~Allons y!'), [('key', 'c', 'incomprhension')]),
                            'incomprhension': ( ('QT/afraid', '', '\pau=500\Mais on va où ?'), [('key', 'c', 'froid_01')]),
                            'froid_01': ( ('QT/with_a_cold', 'QT/angry', ''), [('time', 4, 'froid_02')]),
                            'froid_02': ( ('', 'QT/imitation/hands-side', '~La météo dit: Température -8°C et mes détecteurs le confirment. Ce n’est pas logique, pourquoi voulez-vous sortir ?'), [('time', 9, 'froid_03')]),
                            'froid_03': ( ('QT/sad', 'QT/neutral', 'On est si bien à l’intérieur!'), [('key', 'c', 'refus_01')]),

                            'refus_01': ( ('', 'QT/angry', '~Non, je ne veux pas y aller!'), [('time', 4, 'refus_02')]),
                            'refus_02': ( ('', 'QT/shy', '~Selon wikipédia: la neige c’est froid, ça brûle les mains, et puis ça mouille… C’est quoi l’intérêt?'), [('key', 'c', 'accord_01')]),

                            'accord_01': ( ('QT/confused','QT/touch-head','\pau=1000\Ah bon?'), [('time', 6, 'accord_02')]),
                            'accord_02': ( ('QT/shy','QT/neutral',''), [('time', 4, 'accord_03')]),
                            'accord_03': ( ('','QT/imitation/nodding_yes','~Un QT en neige, d’accord, montrez-moi!'), [('key', 'c', 'imitation_01')]),

                            'imitation_01': ( ('','QT/peekaboo-back',''), [('time', 2, 'imitation_02')]),
                            'imitation_02': ( ('QT/one_eye_wink','','Allons-y'), [('key', 'c', 'end')]),



                            'end': ((), [('time', 0.1, 'end')]) }


        self.state = 'begin'
        rospy.Timer(rospy.Duration( self.states[self.state][1][0][1]), self.time_callback, oneshot=True)
        print(self.state)


    def time_callback(self, event):
        # go to next state
        print('time callback')
        triggers = self.states[self.state][1]
        for trigger in triggers:
            if trigger[0] == 'time':
                self.state = trigger[2]
                print('next_state: ' + self.state)
                self.next_state()

#        self.state = self.states[self.state][2]

#        pass

    def keyboard_callback(self, key):
        print('keyboard callback: ' + key)
        triggers = self.states[self.state][1]
        for trigger in triggers:
            if trigger[0] == 'key':
                if trigger[1] == key:
                    self.state = trigger[2]
                    print('next_state: ' + self.state)
                    self.next_state()
                    break;

#        pass

    def next_state(self):
        if(self.state != 'end'):
            # send bhw
            bhw = self.states[self.state][0]
            if(len(bhw)):
                # AL machine => pass to smach
                print(self.state + ' =bhw=> ' + str(bhw))
                client = actionlib.SimpleActionClient('/qt_behave', theatre.msg.QTBehaviorAction)
                client.wait_for_server()

                goal = theatre.msg.QTBehaviorGoal( emotion=bhw[0],
                                                    gesture=bhw[1],
                                                    speech=bhw[2])
                client.send_goal(goal)
                # ...
                client.wait_for_result()
                result = client.get_result()

            # prepare jump for next state
            triggers = self.states[self.state][1]

            print(self.state + ' =trig=> ' + str(triggers))
            for trigger in triggers:
                if trigger[0] == 'time':
                    rospy.Timer(rospy.Duration(trigger[1]), self.time_callback, oneshot=True)


    def execute(self):
        while not rospy.is_shutdown():
            if self.state == 'end': break
            key = getKey(0.1)
            if (len(key)):
                self.keyboard_callback(key)
            self.rate.sleep()





if __name__ == '__main__':
    rospy.init_node('drama_group_joy')
    drama = DramaWaking()
    drama.execute()  

