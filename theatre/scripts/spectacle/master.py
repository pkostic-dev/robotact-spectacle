# Master file containing all scenes

#! xrandr -o normal
#! Windows + O

states = {
    'begin': ({}, [('time', 1, 'choice')]),
    'end': ({}, [('time', 0.1, 'end')]) ,

    'main_choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 's5_choice'),
            ('key', "é", 's6_choice'),
            ('key', '"', 'scene_10'),
            ('key', '\'', 'scene_9'),
            ('key', '(', 'scene_10'),
            ('key', '-', 'scene_11'),
            ('key', 'è', 'scene_12'),
            ('key', '_', 'scene_fin'),

            ('key', '*', 'end'),
        ]
    ),

    # ? SCENE 5

    # ! SWITCH TO ENGLISH
    # ! rosservice call /qt_robot/speech/config "language: 'en_US'"

    # ! HEAD_TO_NAO [c]
    # ! HEAD_TO_PUBLIC [q]

    's5_choice': (
        {'g': '', 's': '' },
        [
            # Dialogue
            ('key', '&', 's5_1_salut'),
            ('key', 'é', 's5_2_operationnel'),
            ('key', '"', 's5_3_autisme'),
            # ? During Nao :
            # !     SURPRISE [p]
            # !     YAWN [o]
            ('key', "'", 's5_4_polyvalent'),
            # ! NEUTRAL [=]
            # ? During Nao :
            # !     YAWN [o]
            ('key', '(', 's5_5_impressionnant'),
            # ? During Nao :
            # !     RASPBERRY [b]
            ('key', '-', 's5_6_absolument'),

            # Gestures
            ('key', '=', 'neutral'),

            # QT emotions
            ('key', 'o', 'yawn'),
            ('key', 'p', 'surprise'),
            ('key', 'b', 'blowing_raspberry'),

            # Head
            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),
            ('key', 'Z', 'look_up_short'),
            ('key', 'X', 'look_down_short'),
            ('key', 'Q', 'look_left_short'),
            ('key', 'D', 'look_right_short'),

            # CONTROL
            ('key', '*', 'main_choice'),

        ]
    ),

    's5_1_salut': (
        {
            's': 'Hi NAO, how are you ?',
            'e': 'QT/happy',
            'g': 'QT/hi'
        },
        [
            ('time', 0.1, 's5_choice')
        ]
    ),

    's5_2_operationnel': (
        {
            's': 'I am partially \\pau=300\\ operational. Sometimes \\pau=300\\ I get stuck \\pau=200\\ if I move too much, and \\pau=200\\ I need to \\rspd=80\\ be restarted. \\rspd=100\\ But I am fine! Do you know what I can do ?',
            'g': 'QT/neutral',
            'e': 'QT/talkinglong',
        },
        [
            ('time', 0.1, 's5_choice')
        ]
    ),

    's5_3_autisme': (
        {
            's': 'I am often used \\pau=300\\ in studies on \\pau=200\\ \\rspd=70\\ autism \\rspd=100\\ . I can \\pau=300\\ interact socially \\pau=200\\ and help teach \\pau=200\\ emotional skills. I\'m designed \\pau=200\\ to be \\rspd=70\\ easily programmable \\rspd=100\\ , but \\pau=300\\ as I told you, I can be \\pau=200\\ a bit unstable. How about you ?',
            'e': 'QT/talkinglong',
        },
        [
            ('time', 0.1, 's5_choice')
        ]
    ),

    's5_4_polyvalent': (
        {
            's': 'Ah, that is why you are so \\rspd=80\\ agile! \\rspd=100\\ Do you have \\rspd=80\\ sensors ?',
            'e': 'QT/talkinglong',
            'g': 'QT/imitation/hands-on-head'
        },
        [
            ('time', 0.1, 's5_choice')
        ]
    ),

    's5_5_impressionnant': (
        {
            's': 'That is impressive! I have an integrated tablet, a camera, and a microphone. I am also equipped \\pau=200\\ with two onboard computers to control \\pau=300\\ my functions. How many computers do you have ?',
            'e': 'QT/talkinglong',
        },
        [
            ('time', 0.1, 's5_choice')
        ]
    ),

    's5_6_absolument': (
        {
            's': 'Absolutely, we can make a lot together ! let\'s go !',
            'e': 'QT/talkinglong'
        },
        [
            ('time', 0.1, 's5_choice')
        ]
    ),

    's6_choice': (
        {'g': '', 's': '' },
        [
            # QT look
            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),

            # Dialogue            
            ('key', 'o', 'of_course'), 
            ('key', 't', 'nice_to'), 
            ('key', 'y', 'yes'),
            ('key', 'n', 'no'),
            ('key', 'm', 'maybe'),
            ('key', 'g', 'great'),
            ('key', 'N', 'no_no_no'),

            
            # QT emotions
            ('key', '&', 'cry'),
            ('key', '"', 'angry'),
            ('key', '\'', 'yawn'),
            ('key', '(', 'surprise'),
            ('key', '-', 'afraid'),
            ('key', 'è', 'disgusted'),
            ('key', '_', 'happy'),
            ('key', 'ç', 'shy'),
            ('key', 'à', 'kiss'),
            ('key', ')', 'blowing_raspberry'),

            ('key', '*', 'end'),
        ]
    ),

    'of_course': ( {'e':'QT/talking', 'g': '', 's': 'Of course!'}, [('time', 0.1, 's6_choice')]),
    'nice_to': ( {'e':'QT/talking', 'g': '', 's': 'Nice to meet you.'}, [('time', 0.1, 's6_choice')]),
    'yes': ( {'e':'QT/talking', 'g': '', 's': 'Yes!'}, [('time', 0.1, 's6_choice')]),
    'maybe': ( {'e':'QT/talking', 'g': '', 's': 'Maybe'}, [('time', 0.1, 's6_choice')]),
    'no': ( {'e':'QT/talking', 'g': '', 's': 'No'}, [('time', 0.1, 's6_choice')]),
    'great': ( {'e':'QT/talking', 'g': '', 's': 'Great!'}, [('time', 0.1, 's6_choice')]),
    'no_no_no': ( {'e':'QT/talking', 'g': '', 's': 'No no no.'}, [('time', 0.1, 's6_choice')]),

    # ? QT HEAD
    'look_up': ( {'s': '', 'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_up_short': ( {'s': '', 'h': [0.0,-10.0]}, [('time', 0.1, 'choice')]),
    'look_down_short': ( {'s': '', 'h': [0.0,+5.0]}, [('time', 0.1, 'choice')]),
    'look_right_short': ( {'s': '', 'h': [-10.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left_short': ( {'s': '', 'h': [+10.0,0.0]}, [('time', 0.1, 'choice')]),


}