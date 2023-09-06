######################################################## SCENE 1 #######################################################

# QT -> DIALOGUE, HEAD, ARMS
# NAO -> DIALOGUE, ?

# SCÈNE 1 : Arrivée de NAO et QTRobot : Ils expliquent leurs habiletés et leurs caractéristiques
# [scène écrite par chatGPT]

# QTRobot : Salut Nao comment vas-tu ?
# NAO : Salut QT, je vais bien. Et toi ?
# QTRobot: Je suis opérationnel. Sais-tu ce que je peux faire ?
# NAO: Non, dis-moi.
# QTRobot: Je suis souvent utilisé dans des études sur l'autisme. Je peux interagir de manière sociale et aider à enseigner des compétences émotionnelles.
# NAO: C'est intéressant ! Moi, je suis polyvalent. Je peux marcher, parler et même danser. Je suis souvent utilisé dans l'éducation et la recherche.
# QTRobot: C'est cool ! As-tu des capteurs ?
# NAO: Oui, j'ai des capteurs tactiles, sonores et une caméra. Et toi ?
# QTRobot: J'ai une tablette intégrée et une caméra. Je suis conçu pour être facilement programmable.
# NAO: Cela semble très utile. On fait une belle équipe, non ?
# QTRobot: Absolument, nous pouvons accomplir beaucoup ensemble !

####################################################### AUTOMATIC (OLD) ################################################

# Example : qt_1 to qt_2, qt_1 time + nao_1 time

# Times in seconds (float)
# qt_times = [3, 6, 11, 4, 9, 5]
# nao_times = [4, 3, 10, 5, 5]

########################################################## NOTES #######################################################

# Used to be automatic but is now WOZ
# Update dialogue with ChatGPT
# Add emotions / movement

qt_states = {
    'qt_1': ( # 3s
        {
            's': 'Salut Nao comment vas-tu ?'
        },
        [
            #('time', qt_times[0] + nao_times[0], 'qt_2')
            ('time', 1, 'choice')
        ]
    ),

    'qt_2': ( # 6s
        {
            's': 'Je suis opérationnel. Sais-tu ce que je peux faire ?' # il a des bug, le bras
        },
        [
            #('time', qt_times[1] + nao_times[1], 'qt_3')
            ('time', 1, 'choice')
        ]
    ),

    'qt_3': ( # 11s
        {
            's': 'Je suis souvent utilisé dans des études sur l\'autisme. Je peux interagir de manière sociale et aider à enseigner des compétences émotionnelles.?'
        },
        [
            #('time', qt_times[2] + nao_times[2], 'qt_4')
            ('time', 1, 'choice')
        ]
    ),

    'qt_4': ( # 4s
        {
            's': 'C\'est cool ! As-tu des capteurs ?'
        },
        [
            #('time', qt_times[3] + nao_times[3], 'qt_5')
            ('time', 1, 'choice')
        ]
    ),

    'qt_5': ( # 9s
        {
            's': 'J\'ai une tablette intégrée et une caméra. Je suis conçu pour être facilement programmable.'
        },
        [
            #('time', qt_times[4] + nao_times[4], 'qt_6')
            ('time', 1, 'choice')
        ]
    ),

    'qt_6': ( #5s
        {
            's': 'Absolument, nous pouvons accomplir beaucoup ensemble !'
        },
        [
            #('time', qt_times[5], 'choice')
            ('time', 1, 'choice')
        ]
    ),

    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 'qt_1'),
            ('key', 'é', 'qt_2'),
            ('key', '"', 'qt_3'),
            ('key', "'", 'qt_4'),
            ('key', '(', 'qt_5'),
            ('key', '-', 'qt_6'),
            ('key', 'e', 'end'),
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
}

nao_states = {
    'nao_1': ( # 4s
        {
            's': 'Salut QT, je vais bien. Et toi ?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_2': ( # 3s
        {
            's': 'Non, dis-moi.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    
    'nao_3': ( # 10s
        {
            's': 'C\'est intéressant ! Moi, je suis polyvalent. Je peux marcher, parler et même danser. Je suis souvent utilisé dans l\'éducation et la recherche.' # cree pour football
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_4': ( # 5s
        {
            's': 'Oui, j\'ai des capteurs tactiles, sonores et une caméra. Et toi ?' # tactiles ?
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_5': ( # 5s
        {
            's': 'Cela semble très utile. On fait une belle équipe, non ?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,

    'choice': (
        {'g': '', 's': '' },
        [
            # Dialogue
            ('key', '&', 'nao_1'),
            ('key', 'é', 'nao_2'),
            ('key', '"', 'nao_3'),
            ('key', "'", 'nao_4'),
            ('key', '(', 'nao_5'),

            # Robot control
            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),

            ('key', '8', 'walk_fwd'),
            ('key', '5', 'stop'),
            ('key', '2', 'walk_back'),
            ('key', '4', 'strife_left'),
            ('key', '6', 'strife_right'),
            ('key', '7', 'rotate_left'),
            ('key', '9', 'rotate_right'),

            # Control
            ('key', '*', 'end'),
        ]
    ),

    # HEAD
    'look_up': ( {'s': '', 'h': [0.0,-1]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,+0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+1]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-2,+0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+2,+0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-0.5,-5.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+0.5,-0.5]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-0.5,+0.5]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+0.5,+0.5]}, [('time', 0.1, 'choice')]),

    # Movement
    'walk_fwd': ( {'w': [1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'stop': ( {'w': [0,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'walk_back': ( {'w': [-1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'strife_left': ( {'w': [0,1,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'strife_right': ( {'w': [0,-1,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'rotate_left': ( {'w': [0,0,0,0,0,1]}, [('time', 0.1, 'choice')]),
    'rotate_right': ( {'w': [0,0,0,0,0,-1]}, [('time', 0.1, 'choice')]),
}
