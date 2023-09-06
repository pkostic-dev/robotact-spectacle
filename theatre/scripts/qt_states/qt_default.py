states = {
    'begin': ({}, [('time', 1, 'choice')]),

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),
            ('key', 'h', 'hello'),
            ('key', 'k', 'dontknow'),
            ('key', 'y', 'oui'),
            ('key', 'n', 'non'),
            
            ('key', 'f', 'suivi'),
            ('key', 'g', 'public'),
            ('key', 'r', 'objetDroite'),
            ('key', 'l', 'objetGauche'),
            ('key', 'p', 'pense'),
            ('key', 'o', 'pense2'),
            ('key', 'm', 'neutral'),
            ('key', 'R', 'really'),
            ('key', 'H', 'comment'),
            ('key', 'J', 'jaime'),
            ('key', 'Y', 'happy'),
            ('key', 'K', 'kisses'),
            ('key', 'E', 'excited'),
            ('key', 't', 'thinking'),
            ('key', 'C', 'curious'),
            ('key', 'F', 'fear'),
            ('key', 'O', 'confused'),
            ('key', 'b', 'bored'),
            ('key', 'j', 'end')
        ]
    ),

    'look_up': ( {'s': '', 'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),

    'hello': ( {'e': 'QT/happy', 'g': 'QT/hi', 's': '\\pau=2000\\Salut!', 'h': [0,0]}, [('time', 1, 'choice')]),
    'dontknow': ( {'e': '', 'g': 'QT/touch-head', 's': '~\\pau=500\\Je ne sais pas'}, [('time', 1, 'choice')]),
    'oui': ( {'e': '', 'g': 'QT/imitation/nodding-yes', 's': '~\\pau=500\\Oui!'}, [('time', 1, 'choice')]),
    'non': ( {'e': '', 'g': 'QT/emotions/sad', 's': '~\\pau=500\\Non!'}, [('time', 1, 'choice')]),
    'suivi': ( {'e': 'QT/surprise', 'g': 'QT/imitation/head-right-left', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'public': ( {'e': 'QT/surprise', 'h': [0.0,0.0], 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'objetDroite': ( {'e': 'QT/happy', 'h': [+10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
    'objetGauche': ( {'e': 'QT/happy', 'h': [-10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
    'pense': ( {'e': 'QT/confused', 'g': 'QT/imitation/hands-on-hip', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'pense2': ( {'e': 'QT/afraid', 'g': 'QT/touch-head-back', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'neutral': ( {'e': 'QT/neutral', 'g': 'QT/neutral', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'really': ( {'e': 'QT/dirty_face','g': 'QT/surprise', 's': '\\pau=2000\\Vraiment ?'}, [('time', 3, 'choice')]),
    'comment': ( {'e':'QT/surpise','g': 'QT/touch-head', 's': '\\pau=2000\\Comment ?'}, [('time', 3, 'choice')]),
    'jaime': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=2000\\jème beaucoup !'}, [('time', 3, 'choice')]),
    'happy': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=500\\ Youpi !'}, [('time', 3, 'choice')]),

    'kisses': ( {'e':'QT/kiss','g': 'QT/kiss'}, [('time', 3, 'kisses1')]),
    'kisses1': ( {'e':'QT/one_eye_wink','g': 'QT/neutral'}, [('time', 3, 'kisses2')]),
    'kisses2': ( {'e':'QT/shy','h': [-10.0,+10.0]}, [('time', 3, 'choice')]),

    'excited': ( {'e':'QT/surpise','g': 'QT/neutral'}, [('time', 3, 'excited1')]),
    'excited1': ( {'e':'QT/happy','g': 'QT/neutral'}, [('time', 3, 'choice')]),

    'thinking': ( {'e':'QT/surpise','g': 'QT/bored'}, [('time', 3, 'choice')]),

    'curious': ( {'e':'QT/suprise','g': 'QT/neutral'}, [('time', 3, 'curious1')]),
    'curious1': ( {'e':'QT/showing_smile','g': 'QT/neutral'}, [('time', 3, 'choice')]),

    'fear': ( {'e':'QT/cry','g': 'QT/face'}, [('time', 3, 'choice')]),

    'confused': ( {'e':'QT/confused','g': 'QT/neutral'}, [('time', 3, 'choice')]),
    'bored': ( {'e':'QT/yawn','g': 'QT/bored'}, [('time', 3, 'choice')]),

    'end': ((), [('time', 0.1, 'end')])
}