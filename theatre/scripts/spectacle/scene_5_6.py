######################################################## SCENE 5 #######################################################

# QT -> DIALOGUE, HEAD, ?
# NAO -> DIALOGUE, WALK

# SCÈNE 5 : la rencontre d’un masque blanc et de QT : scène sans parole sur l’incapaticé du robot de bouger, reagir, et
#           agir. La scène se termine avec Léandre qui sort. [1er partie de la scène déjà existante,
#           à répéter et finaliser la 1er semaine]

# QT : Où vas-tu ? Reste. J’ai envie que nous jouions ensemble. Mais je sens bien qu’il y a un problème de 
#      communication. Nao, Nao, viens ! 
# NAO : Oui QT, je suis là !
# QT : Est-ce que tu as réussi à t’entendre avec les comédiens ? 
# NAO : Mmmmhhh, je ne suis pas sûr, mais je sens que je suis sur la bonne voie. On y travaille…
# NAO rejoint sa position en diagonale cour. Le chœur masqué entre à jardin. 

######################################################## SCENE 6 #######################################################

# NAO -> HEAD, WALK, CUSTOM

# SCÈNE 6 : la séquence de Claire Heggen sur les principes du mouvement : la rencontre du groupe avec NAO. Séquence métaphorique sur la représentation de la relation d'intérêt et méfiance de l’homme par rapport aux robots. [scène déjà existante, à répéter 2ème semaine]

######################################################### NOTES ########################################################

# TODO : add scene 6 behavior and triggers

qt_states = {
    'qt_1': ( # 3s
        {
            's': 'Où vas-tu ? Reste. J’ai envie que nous jouions ensemble. Mais je sens bien qu’il y a un problème de communication. Nao, Nao, viens !'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'qt_2': ( # 6s
        {
            's': 'Est-ce que tu as réussi à t’entendre avec les comédiens ?'
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
            ('key', '&', 'qt_1'),
            ('key', 'é', 'qt_2'),

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
            
            # Control
            ('key', '*', 'end'),
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
            's': ' Oui QT, je suis là !'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_2': ( # 3s
        {
            's': 'Mmmmhhh, je ne suis pas sûr, mais je sens que je suis sur la bonne voie. On y travaille...'
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

    # Head
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

