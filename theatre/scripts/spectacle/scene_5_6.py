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

# TODO : add scene 6 behavior and triggers, ask Anis if has PC with Ubuntu and ROS

qt_states = {
    'qt_1_reste': ( # 3s
        {
            's': 'Où vas-tu ? Reste. J’ai envie que nous jouions ensemble. Mais je sens bien qu’il y a un problème de communication. Nao, Nao, viens !'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'qt_2_comediens': ( # 6s
        {
            's': 'Est-ce que tu as réussi à t’entendre avec les comédiens ?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'qt_3_grands': (
        {
            's': 'Oui, c’est vrai. Par contre,  ils sont si grands par rapport à nous ! '
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
            # Dialogue fin de scene
            ('key', '&', 'qt_1_reste'),
            ('key', 'é', 'qt_2_comediens'),
            ('key', '"', 'qt_3_grands'),

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

            # Emotions
            # TODO Test
            ('key', 'r', 'cry'),
            ('key', 'f', 'afraid'),
            ('key', 'y', 'happy'),
            ('key', 'k', 'kiss'),
            ('key', 'g', 'disgusted'),

            # Arms
            # TODO Test
            ('key', 'i', 'hi'),
            ('key', 'h', 'hands-up'),
            ('key', 'H', 'hands-on-head'),
            ('key', 'n', 'neutral'),
        ]
    ),

    # Head
    'look_up': ( {'s': '', 'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),

    # Emotions
    'happy' : ( {'e':'QT/happy','g': '', 's': ''}, [('time', 1, 'choice')]),
    'kiss' : ( {'e':'QT/kiss','g': '', 's': ''}, [('time', 1, 'choice')]),
    'cry' : ( {'e':'QT/cry','g': '', 's': ''}, [('time', 1, 'choice')]),
    'afraid' : ( {'e':'QT/afraid','g': '', 's': ''}, [('time', 1, 'choice')]),
    'disgusted' : ( {'e':'QT/disgusted','g': '', 's': ''}, [('time', 1, 'choice')]),

    # Gestures
    'hi' : ( {'e':'','g': 'QT/hi', 's': ''}, [('time', 1, 'choice')]),
    'hands-up' : ( {'e':'','g': 'QT/imitation/hands-up', 's': ''}, [('time', 1, 'choice')]),
    'hands-on-head' : ( {'e':'','g': 'QT/imitation/hands-on-head', 's': ''}, [('time', 1, 'choice')]),
    'neutral' : ( {'e':'','g': 'QT/neutral', 's': ''}, [('time', 1, 'choice')]),
}

nao_states = {
    'nao_1_oui': ( # 4s
        {
            's': ' Oui QT, je suis là !'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_2_masques': (
        {
            's': 'Mmmmhhh, je ne suis pas sûr, mais je sens que nous sommes sur la bonne voie. Quand les acteurs portent des masques, ils deviennent aussi un peu artificiels. Ils nous ressemblent.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_3_rapides': (
        {
            's': 'Et si rapides, imprévisibles, ce n’est pas simple de les suivre. Nous sommes justement en train de travailler sur cette question maintenant…'
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
            # Dialogue fin de scene
            ('key', '&', 'nao_1_oui'),
            ('key', 'é', 'nao_2_masques'),
            ('key', '"', 'nao_3_rapides'),

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

