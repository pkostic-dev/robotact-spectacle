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

            ('key', 'D', 'look_right_180'),
            ('key', 'Q', 'look_left_180'),
            ('key', 'E', 'look_up_right_180'),
            ('key', 'A', 'look_up_left_180'),
            ('key', 'C', 'look_down_right_180'),
            ('key', 'W', 'look_down_left_180'),

            ('key', 'Z', 'LSU'),
            ('key', 'X', 'LSD'),

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
            ('key','J','jaime'),
            ('key','b','bored'),
            ('key','Y','happy'),
            ('key', 'S', 'sad'),
            ('key', 'u', 'standup'),
            ('key', 'K', 'kisses'),
            ('key', 'E', 'excited'),
            ('key', 't', 'thinking'),
            ('key', 'C', 'curious'),
            ('key', 'F', 'fear'),
            ('key', 'O', 'confused'),

            ('key', '8', 'walk_fwd'),
            ('key', '5', 'stop'),
            ('key', '2', 'walk_back'),
            ('key', '4', 'strife_left'),
            ('key', '6', 'strife_right'),
            ('key', '7', 'rotate_left'),
            ('key', '9', 'rotate_right'),

            ('key', ',', 'hands_up'),
            ('key', ';', 't_pose'),
            ('key', 'p', 'point'),

            ('key', 'j', 'end')
        ]
    ),

    'point': (
        {
            's': '',
            'la': [-0.5,0,0,0,0,1]
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'hands_up': (
        {
            's': '',
            'la': [-1,0,0,0,0,1],
            'ra': [-1,0,0,0,0,1],
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    't_pose': (
        {
            's': '',
            'la': [0,1,0,0,0,1],
            'ra': [0,-1,0,0,0,1]
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'look_up': ( {'s': '', 'h': [0.0,-1]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,+0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+1]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-2,+0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+2,+0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-0.5,-5.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+0.5,-0.5]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-0.5,+0.5]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+0.5,+0.5]}, [('time', 0.1, 'choice')]),

    'look_left_180': ( {'s': '', 'h': [+1.5,-0.5]}, [('time', 0.1, 'choice')]),
    'look_right_180': ( {'s': '', 'h': [-1.5,-0.5]}, [('time', 0.1, 'choice')]),
    'look_up_left_180': ( {'s': '', 'h': [+2.0,-2.0]}, [('time', 0.1, 'choice')]),
    'look_up_right_180': ( {'s': '', 'h': [-2.0,-2.0]}, [('time', 0.1, 'choice')]),
    'look_down_right_180': ( {'s': '', 'h': [-2.0,+2.0]}, [('time', 0.1, 'choice')]),
    'look_down_left_180': ( {'s': '', 'h': [+2.0,+2.0]}, [('time', 0.1, 'choice')]),

    'LSD': ( {'s': '', 'la': [0.5,0,0,0,0,1]}, [('time', 1, 'choice')]),
    'LSU': ( {'s': '', 'la': [-0.5,0,0,0,0,1]}, [('time', 1, 'choice')]),
    #'see': ( {'s': 'Did you see ?'}, [('time', 0.1, 'choice')]),

    'hello': ( {'g': 'hello', 's': '\\pau=4000\\Hello!', 'h': [0,0]}, [('time', 3, 'choice')]),
    'dontknow': ( {'g': 'dontknow', 's': '\\pau=1000\\I dont know'}, [('time', 3, 'choice')]),
    'oui': ( {'g': 'oui', 's': '\\pau=50\\yes!'}, [('time', 3, 'choice')]),
    'non': ( {'g': 'non', 's': '\\pau=5\\no!'}, [('time', 3, 'choice')]),
    'suivi': ( {'g': 'suivi', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
    'public': ( {'g': 'public', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
    'objetDroite': ( {'g': 'objetDroite', 's': '\\pau=9500\\Here !'}, [('time', 3, 'choice')]),
    'objetGauche': ( {'g': 'objetGauche', 's': '\\pau=9500\\Here !'}, [('time', 3, 'choice')]),
    'pense': ( {'g': 'pense', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
    'pense2': ( {'g': 'pense2', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
    'neutral': ( {'g': 'neutral', 's': '\\pau=2000\\'}, [('time', 3, 'choice')]),
    'really': ( {'g': 'really', 's': '\\pau=2000\\really ?'}, [('time', 3, 'choice')]),
    'comment': ( {'g': 'comment', 's': '\\pau=2000\\how ?'}, [('time', 3, 'choice')]),
    'jaime': ( {'g':'jaime', 's': '\\pau=1500\\ I love it !'}, [('time', 3, 'choice')]),
    'bored': ( {'g':'bored', 's': '\\pau=1500\\ Huff'}, [('time', 3, 'choice')]),
    'happy': ( {'g':'happy', 's': '\\pau=1500\\ YES !'}, [('time', 3, 'choice')]),
    'sad': ( {'g':'sad', 's': '\\pau=1500\\ oh'}, [('time', 3, 'choice')]),
    'standup': ( {'g':'standup'}, [('time', 3, 'choice')]),

    'kisses': ( {'g':'kiss'}, [('time', 3, 'choice')]),
    'excited': ( {'g':'excited','s': 'yes !'}, [('time', 3, 'choice')]),
    'thinking': ( {'g':'thinking'}, [('time', 3, 'choice')]),
    'curious': ( {'g':'curious','s': '\\pau=1500\\ oh'}, [('time', 3, 'choice')]),
    'fear': ( {'g':'fear'}, [('time', 3, 'choice')]),
    'confused': ( {'s':'okey','g': 'confused'}, [('time', 3, 'choice')]),


    'walk_fwd': ( {'w': [1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'stop': ( {'w': [0,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'walk_back': ( {'w': [-1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'strife_left': ( {'w': [0,1,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'strife_right': ( {'w': [0,-1,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'rotate_left': ( {'w': [0,0,0,0,0,1]}, [('time', 0.1, 'choice')]),
    'rotate_right': ( {'w': [0,0,0,0,0,-1]}, [('time', 0.1, 'choice')]),

    'end': ((), [('time', 0.1, 'end')]) 
}