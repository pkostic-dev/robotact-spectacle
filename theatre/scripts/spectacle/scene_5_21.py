######################################################## SCENE 5 #######################################################

# SCÈNE 5 : Scène de ChatGPT

# !!! rosservice call /qt_robot/speech/config "language: 'en_US'"

#! [&](1)
# QTrobot: Salut NAO, comment vas-tu ?

#? [&](1)
# NAO: Salut QTrobot, je vais bien. Et toi ?

#! [é](2)
# QTrobot: Je suis en partie opérationnel. Parfois, je bloque si je bouge trop et je dois être redémarré. Sais-tu ce 
#          que je peux faire ?

#? [é](2)
# NAO: Non, dis-moi. 

#! ["](3)
# QTrobot: Je suis souvent utilisé dans des études sur les déficits du neuro-développement. Je peux interagir de 
#          manière sociale et aider à enseigner des compétences émotionnelles. Je suis conçu pour être facilement 
#          programmable, mais comme je t'ai dit, je peux être un peu instable. Et toi ?

#? ["](3)
#! QT [o] yawn
# NAO: C'est intéressant ! Moi, je suis plutôt polyvalent. Je peux marcher, parler et même danser. Je suis souvent 
#      utilisé dans l'éducation et la recherche. J'ai été à l'origine conçu pour jouer au football.

#! ['](4)
# QTrobot: Ah, c'est pour ça que tu es si polyvalent ! As-tu des capteurs ?

#? ['](4)
#! QT [o] yawn
# NAO: Oui, j'ai un contrôle inertiel avec accéléromètre et gyromètre, deux sonars, un capteur infrarouge, des capteurs 
#      de force sous les pieds, des interrupteurs, des touches capacitives, des capteurs embarqués dans la batterie, 
#      deux caméras et quatre microphones. Et toi ? (les premieres têtes d’acteurs sort des rideaux noir, une file de 
#      trois têtes va venir se creer puis Andrea aura sa tête toute seule)

#! [(](5)
# QTrobot: C'est impressionnant ! Je dispose d'une tablette intégrée, d'une caméra et d'un microphone. Je suis 
#          également équipé de deux ordinateurs embarqués pour gérer mes fonctions. Combien d'ordinateurs as-tu ?

#? [(](5)
#! QT [p] surprised
# NAO: Cela semble très utile. Moi, j'ai seulement un processeur ARM qui gère toutes mes fonctions.. On a chacun nos 
#      forces et nos faiblesses. On fait une belle équipe, non ?

#! [-](6)
# QTrobot: Absolument, nous pouvons accomplir beaucoup ensemble, malgré nos petits défauts !


######################################################## SCENE 21 ######################################################

# Aussi utilisé dans la Scene Photos de famille
# Ordre des emotions :
    #!!!!!!!!! QT Neutral [=]
#   Photo 1 #! [k] Kiss
#   Photo 2 #! [h] Happy
#   Photo 3 #! [o] Yawn
#   Photo 4 #! [f]
#   Photo 5 #! [p]
#   Photo 6 #! [y]
#   Photo 7 #! [r]
#   Photo 8 #! [j]
#   Photo 9 #! [g]
#   Photo 10 #! Sur scene avec ordi
#   Photo 11 #! Ferme ordi

########################################################## NOTE #######################################################

# Used to be automatic but is now WOZ
# QT -> DIALOGUE, HEAD, ARMS
# NAO -> DIALOGUE, HEAD, MOVEMENT, ?


head_to_public = [+20.0,0.0]

qt_states = {
    'qt_1_salut': (
        {
            's': 'Hi NAO, how are you ?',
            'e': 'QT/happy',
            'g': 'QT/hi'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # ! HEAD_TO_NAO [c]
    # ! PUBLIC [q]

    'qt_2_operationnel': (
        {
            's': 'I am partially \\pau=300\\ operational. Sometimes \\pau=300\\ I get stuck \\pau=200\\ if I move too much, and \\pau=200\\ I need to \\rspd=80\\ be restarted. \\rspd=100\\ But I am fine! Do you know what I can do ?',
            'g': 'QT/neutral',
            'e': 'QT/talkinglong',
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # ! HEAD_TO_NAO [c]
    # ! PUBLIC [q]

    'qt_3_autisme': (
        {
            's': 'I am often used \\pau=300\\ in studies on \\pau=200\\ \\rspd=70\\ autism \\rspd=100\\ . I can \\pau=300\\ interact socially \\pau=200\\ and help teach \\pau=200\\ emotional skills. I\'m designed \\pau=200\\ to be \\rspd=70\\ easily programmable \\rspd=100\\ , but \\pau=300\\ as I told you, I can be \\pau=200\\ a bit unstable. How about you ?',
            'e': 'QT/talkinglong',
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # ! HEAD_TO_NAO [c]
    # ! PUBLIC [q]

    'qt_4_polyvalent': (
        {
            's': 'Ah, that is why you are so \\rspd=80\\ agile! \\rspd=100\\ Do you have \\rspd=80\\ sensors ?',
            'e': 'QT/talkinglong',
            'g': 'QT/imitation/hands-on-head'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # ! HEAD_TO_NAO [c]
    # ! NEUTRAL [=] pour baisser les bras
    # ! PUBLIC [q]

    'qt_5_impressionnant': (
        {
            's': 'That is impressive! I have an integrated tablet, a camera, and a microphone. I am also equipped \\pau=200\\ with two onboard computers to control \\pau=300\\ my functions. How many computers do you have ?',
            'e': 'QT/talkinglong',
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # ! HEAD_TO_NAO [c]
    # ! PUBLIC [q]

    'qt_6_absolument': (
        {
            's': 'Absolutely, we can make a lot together ! let\'s go !',
            'e': 'QT/talkinglong'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'qt_retry': (
        {
            's': 'As I was saying',
            'e': 'QT/talking'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'qt_retry_2': (
        {
            's': 'Hey, do not interrupt me please !',
            'e': 'QT/talkinglong'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'neutral': (
        {
            's': '',
            'g': 'QT/neutral'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,

    'choice': (
        {'g': '', 's': '' },
        [
            # Dialogue
            ('key', '&', 'qt_1_salut'),
            ('key', 'é', 'qt_2_operationnel'),
            ('key', '"', 'qt_3_autisme'),
            ('key', "'", 'qt_4_polyvalent'),
            ('key', '(', 'qt_5_impressionnant'),
            ('key', '-', 'qt_6_absolument'),

            ('key', '=', 'neutral'),

            ('key', ')', 'qt_retry'),
            ('key', '', 'qt_retry_2'),

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

            ('key', '*', 'end'),

            # QT emotions
            ('key', 'n', 'talking'),
            ('key', 'N', 'talkinglong'),
            ('key', 'k', 'kiss'), # 1
            ('key', 'h', 'happy'), # 2
            ('key', 'o', 'yawn'), # 3
            ('key', 'f', 'afraid'), # 4
            ('key', 'p', 'surprise'), # 5
            ('key', 'y', 'angry'), # 6
            ('key', 'r', 'cry'), # 7
            ('key', 't', 'talking'),
            ('key', 'g', 'disgusted'), # philipo
            ('key', 'j', 'shy'), # 8
            
            ('key', 'b', 'blowing_raspberry'),

        ]
    ),

    # QT Look
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

    # QT emotions
    'happy' : ( {'e':'QT/happy','g': '', 's': ''}, [('time', 1, 'choice')]),
    'kiss' : ( {'e':'QT/kiss','g': '', 's': ''}, [('time', 1, 'choice')]),
    'cry' : ( {'e':'QT/cry','g': '', 's': ''}, [('time', 1, 'choice')]),
    'afraid' : ( {'e':'QT/afraid','g': '', 's': ''}, [('time', 1, 'choice')]),
    'talking' : ( {'e':'QT/talking','g': '', 's': ''}, [('time', 1, 'choice')]),
    'angry' : ( {'e':'QT/angry','g': '', 's': ''}, [('time', 1, 'choice')]),
    'blowing_raspberry' : ( {'e':'QT/blowing_raspberry','g': '', 's': ''}, [('time', 1, 'choice')]),
    'one_eye_wink' : ( {'e':'QT/one_eye_wink','g': '', 's': ''}, [('time', 1, 'choice')]),
    'shy' : ( {'e':'QT/shy','g': '', 's': ''}, [('time', 1, 'choice')]),
    'surprise' : ( {'e':'QT/surprise','g': '', 's': ''}, [('time', 1, 'choice')]),
    'disgusted' : ( {'e':'QT/disgusted','g': '', 's': ''}, [('time', 1, 'choice')]),
    'yawn' : ( {'e':'QT/yawn','g': '', 's': ''}, [('time', 1, 'choice')]),
    'talking' : ( {'e':'QT/talking','g': '', 's': ''}, [('time', 1, 'choice')]),
    'talkinglong' : ( {'e':'QT/talkinglong','g': '', 's': ''}, [('time', 1, 'choice')]),

    # Gestures
    'hi' : ( {'e':'','g': 'QT/hi', 's': ''}, [('time', 1, 'choice')]),
    'hands-up' : ( {'e':'','g': 'QT/imitation/hands-up', 's': ''}, [('time', 1, 'choice')]),
    'hands-on-head' : ( {'e':'','g': 'QT/imitation/hands-on-head', 's': ''}, [('time', 1, 'choice')]),
    'neutral' : ( {'e':'','g': 'QT/neutral', 's': ''}, [('time', 1, 'choice')]),
}

nao_states = {
    'nao_1_salut': ( # 4s
        {
            's': 'Hi QTrobot, I\'m doing well. And you ?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_2_non': ( # 3s
        {
            's': 'No, tell me.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    
    'nao_3_polyvalent': (
        {
            's': 'That\'s interesting! I\'m quite versatile. I can walk, talk, and even dance. I\'m often used in education and research. I was originally designed to play football.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_4_capteurs': (
        {
            's': 'Yes, I have an inertial controller with an accelerometer and gyroscope, two sonars, an infrared sensor, force sensors under my feet, switches, capacitive touch sensors, battery-embedded sensors, two cameras, and four microphones. And you ?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_5_equipe': ( # 5s
        {
            's': 'That sounds very useful. I only have one ARM processor that manages all my functions. We each have our strengths and weaknesses. We make a great team, don\'t we ?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'nao_retry': (
        {
            's': 'As I was saying.',
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'nao_retry_2': (
        {
            's': 'Stop interrupting me please.',
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,

    'choice': (
        {'g': '', 's': '' },
        [
            # Dialogue
            ('key', '&', 'nao_1_salut'),
            ('key', 'é', 'nao_2_non'),
            ('key', '"', 'nao_3_polyvalent'),
            ('key', "'", 'nao_4_capteurs'),
            ('key', '(', 'nao_5_equipe'),

            ('key', ')', 'nao_retry'),
            ('key', '=', 'nao_retry_2'),

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

            # TODO other motions ? arms ?

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
