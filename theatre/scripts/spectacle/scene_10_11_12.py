######################################################## SCENE 10 ######################################################

# QT -> DIALOGUE, HEAD, ?
# NAO -> DIALOGUE, WALK

# SCÈNE 10 : “QT et son ami blanc”  (Léandre + QT)

#? Léandre entre tout seul
#! Predrag : allumer l'UV

#? bras
#! N
#? pied
#! N
#? ventre
#! O
#? bras en haut
#! O ensemble
#? coucou raté
#! i
#? coucou
#! i ensemble
#? bouge
#! N
#? bouge
#! N
#? sort
#! P

#? Léandre sort
#! Predrag : éteindre l'UV

#! [&](1)
# QT : Où vas-tu ? Reste. J’ai envie que nous jouions ensemble.

#! juste apres
#! [1]
# QT : Mais je sens bien qu’il y a un problème de communication. 

#? Nao entre

#! [2]
# QT : Nao, Nao, viens !

#? [&](1)
# NAO : Oui QT, je suis là !

#! [é](2)
# QT : Est-ce que tu as réussi à t’entendre avec les comédiens ?

#? [é](2)
# NAO : Mmmmhhh, je ne suis pas sûr, mais je sens que nous sommes sur la bonne voie. Quand les acteurs portent des 
#       masques, ils deviennent aussi un peu artificiels. Ils nous ressemblent.

#! ["](3)
# QT : Oui, c’est vrai. Par contre,  ils sont si grands par rapport à nous !

#? ["](3)
# NAO : Et si rapides, imprévisibles, ce n’est pas simple de les suivre. Nous sommes justement en train de travailler 
#       sur cette question maintenant…

######################################################## SCENE 11 ######################################################

# NAO -> HEAD, WALK, CUSTOM

# SCÈNE 11 : la séquence de Claire Heggen sur les principes du mouvement : la rencontre du groupe avec NAO. Séquence métaphorique sur la représentation de la relation d'intérêt et méfiance de l’homme par rapport aux robots. [scène déjà existante, à répéter 2ème semaine]

#! QT je suis le corps

# NOTE Anis s'occupe de cette scene

#! QT lance la video Claire Heggen en même temps que la video [(](5)
#! QT couper la video à la fin de la projection avec rosservice

######################################################## SCENE 12 ######################################################

# Scène 12 : Les acteurs ces êtres compliqués (NAO + QT + ampoule)

# Une replique de chaque robot :

#? Nao ['](4)
# puis
#! QT ['](4)

######################################################### NOTE #########################################################

# Le dialogue entre les robots commence quand l'acteur quitte la scene

#! Apres la video de Saeed les robots parlent des acteurs
#! Eteindre QT pendant Ampoule S

head_to_public = [0.0,0.0]
jardin = [-20.0,0.0]

qt_states = {
    # ! [&]
    'qt_1_reste': (
        {
            's': '\\rspd=120\\ Where are you going? \\rspd=100\\ Stay, please! \\rspd=80\\ I still want to play together.',
            'e': 'QT/talkinglong',
            'h': jardin
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    # ! CRY [r]

    # ! [é]
    'qt_1b_probleme': (
        {
            's': 'I am having some communication problems with the actors.',
            'e': 'QT/talkinglong',
            'h': head_to_public
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    # ? wait for Nao stop
    # ! ["]
    'qt_1c_nao': (
        {
            's': 'Nao, Nao, come here!',
            'e': 'QT/talking',
            'h': jardin
        },
        [
            ('time', 1, 'choice')
        ]
    ),
# ? wait for Nao stop
    # ! [']
    'qt_2_comediens': ( # 6s
        {
            's': 'Were you able to play with the actors?',
            'e': 'QT/talking',
            'h': jardin
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    # ! [(]
    'qt_3_grands': (
        {
            's': 'Yes, that\'s true. But they are \\rspd=50\\ so big \\rspd=100\\ \\pau=300\\ compared to us!',
            'e': 'QT/talking',
            'h': head_to_public
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    # ! [-]
    'qt_acteurs': (
        {
            's': 'I see, you had to \\rspd=80\\ learn \\pau=200\\ to \\rspd=70\\ cordinate \\pau=200\\ \\rspd=100\\ your movements \\rspd=75\\ and your rythm \\rspd=100\\ . Unfortunately I can\'t move like you.',
            'e': 'QT/talkinglong',
            'h': head_to_public
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
            ('key', 'é', 'qt_1b_probleme'),
            ('key', '"', 'qt_1c_nao'),
            ('key', '\'', 'qt_2_comediens'),
            ('key', '(', 'qt_3_grands'),
            ('key', '-', 'qt_acteurs'),

            ('key', 'P', 'non_pleure'),
            ('key', 'N', 'non'),
            ('key', 'O', 'oui'),

            # Video
            ('key', 'è', 'claire_heggen'),

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
            ('key', 'r', 'cry'),
            ('key', 'f', 'afraid'),
            ('key', 'y', 'happy'),
            ('key', 'k', 'kiss'),
            ('key', 'g', 'disgusted'),

            # Arms
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

    # Video
    'claire_heggen' : ( {'e':'QT/claire_heggen','g': '', 's': ''}, [('time', 1, 'choice')]),
    # pluie

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

    # Short
    'non_pleure' : ( {'e':'QT/cry', 'g': 'QT/sad', 's': 'Non!'}, [('time', 1, 'choice')]),
    'non' : ( {'e':'QT/sad','g': 'QT/sad', 's': 'Non'}, [('time', 1, 'choice')]),
    'oui' : ( {'e':'QT/happy','g': 'QT/happy', 's': 'Oui!'}, [('time', 1, 'choice')]),
}

nao_states = {
    'nao_1_oui': ( # 4s
        {
            's': 'Yes, QT, I\'m here!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_2_masques': (
        {
            's': 'Mmmmhhh, I\'m not sure, but I feel like we\'re on the right track. When the actors wear masks, they become artificial in some ways. They look like us.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_3_rapides': (
        {
            's': 'And so fast, unpredictable… it\'s not easy to keep up with them. We\'re actually working on these issues right now...'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_acteurs': (
        {
            's': 'Did you see, QT, all the work we did with Claire Heggen? Learning her grammar was very tough. It\'s a true language, as complex as programming!'
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
            ('key', '\'', 'nao_acteurs'),

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

