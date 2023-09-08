######################################################## SCENE 2 #######################################################

# QT -> DIALOGUE, HEAD, ?
# NAO -> DEAD

# SCÈNE 2 : entrent des acteurs, et, comme dans les premiers jours de workshops, ils découvrent les robots avec qui ils travailleront. Simples objets? Partenaires possibles ? Ils les interrogent sur leur capacités réelles, des points de vue divergents émergent, plus ou moins curieux, critiques ou sceptiques. Les acteurs s’intéressent d’abord à QT et ensuite portent leur attention sur NAO qui est éteint. Le discours glisse des possibilités réelles aux robots rêvés.

states = {
    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]),

    'choice': (
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

            # QT simple replies
            ('key', 'r', 'rien'),     ('key', 'R', 'bien'),
            ('key', 't', 'toujours'), ('key', 'T', 'tout'),
            ('key', 'y', 'super'),    ('key', 'Y', 'et_toi'),
            ('key', 'u', 'peux'),     ('key', 'U', 'peuxpas'),
            ('key', 'u', 'de_rien'),  ('key', 'u', 'plaisir'),
            ('key', 'o', 'oui'),      ('key', 'O', 'mais_oui'),
            ('key', 'p', 'peutetre'), ('key', 'P', 'parfois'),

            ('key', 'f', 'fort'),     ('key', 'F', 'faible'),
            ('key', 'g', 'daccord'),  ('key', 'G', 'pas_daccord'),
            ('key', 'h', 'salut'),    ('key', 'H', 'cava'),
            ('key', 'k', 'quand'),    ('key', 'K', 'pourquoi'),
            ('key', 'j', 'sais'),     ('key', 'J', 'saispas'),
            ('key', 'l', 'quoi'),     ('key', 'L', 'qui'),
            ('key', 'm', 'enchante'), ('key', 'M', 'au_revoir'),

            ('key', 'v', 'pardon'),   ('key', 'V', 'merci'),
            ('key', 'b', 'biensur'),  ('key', 'B', 'biensur_non'),
            ('key', 'n', 'non'),      ('key', 'N', 'mais_non'),
            
            # QT emotions
            ('key', '&', 'cry'),
            ('key', 'é', 'talking'),
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

    # QT look
    'look_up': ( {'s': '', 'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),

    # QT simple replies
    'salut': ( {'e':'QT/talking', 'g': '', 's': 'Salut!'}, [('time', 0.1, 'choice')]),
    'sais': ( {'e':'QT/talking', 'g': '', 's': 'Je sais'}, [('time', 0.1, 'choice')]),
    'saispas': ( {'e':'QT/talking', 'g': '', 's': 'Je ne sais pas'}, [('time', 0.1, 'choice')]),
    'oui': ( {'e':'QT/talking', 'g': '', 's': 'Oui!'}, [('time', 0.1, 'choice')]),
    'mais_oui': ( {'e':'QT/talking', 'g': '', 's': 'Mais oui!'}, [('time', 0.1, 'choice')]),
    'non': ( {'e':'QT/talking', 'g': '', 's': 'Non!'}, [('time', 0.1, 'choice')]),
    'mais_non': ( {'e':'QT/talking', 'g': '', 's': 'Mais non!'}, [('time', 0.1, 'choice')]),
    'biensur': ( {'e':'QT/talking', 'g': '', 's': 'Oui, Biensur!'}, [('time', 0.1, 'choice')]),
    'biensur_non': ( {'e':'QT/talking', 'g': '', 's': 'Biensur que non!'}, [('time', 0.1, 'choice')]),
    'rien': ( {'e':'QT/talking', 'g': '', 's': 'Ce n\'est rien.'}, [('time', 0.1, 'choice')]),
    'tout': ( {'e':'QT/talking', 'g': '', 's': 'C\'est tout!'}, [('time', 0.1, 'choice')]),
    'super': ( {'e':'QT/talking', 'g': '', 's': 'Super!'}, [('time', 0.1, 'choice')]),
    'peux': ( {'e':'QT/one_eye_wink', 'g': '', 's': 'Je peux'}, [('time', 0.1, 'choice')]),
    'peuxpas': ( {'e':'QT/sad', 'g': '', 's': 'Je ne peux pas'}, [('time', 0.1, 'choice')]),
    'toujours': ( {'e':'QT/talking', 'g': '', 's': 'Toujours'}, [('time', 0.1, 'choice')]),
    'peutetre': ( {'e':'QT/talking', 'g': '', 's': 'Peut-être'}, [('time', 0.1, 'choice')]),
    'parfois': ( {'e':'QT/talking', 'g': '', 's': 'Parfois'}, [('time', 0.1, 'choice')]),
    'qui': ( {'e': 'QT/confused', 'g': '', 's': 'Qui?'}, [('time', 0.1, 'choice')]),
    'quand': ( {'e': 'QT/confused', 'g': '', 's': 'Quand?'}, [('time', 0.1, 'choice')]),
    'quoi': ( {'e': 'QT/confused', 'g': '', 's': 'Quoi?'}, [('time', 0.1, 'choice')]),
    'pourquoi': ( {'e': 'QT/confused', 'g': '', 's': 'Pourquoi?'}, [('time', 0.1, 'choice')]),
    'cava': ( {'e':'QT/talking', 'g': '', 's': 'ça va?'}, [('time', 0.1, 'choice')]),
    'et_toi': ( {'e':'QT/talking', 'g': '', 's': 'Et toi?'}, [('time', 0.1, 'choice')]),
    'fort': ( {'e':'QT/one_eye_wink', 'g': '', 's': 'Fort!'}, [('time', 0.1, 'choice')]),
    'faible': ( {'e':'QT/sad', 'g': '', 's': 'Faible!'}, [('time', 0.1, 'choice')]),
    'bien': ( {'e':'QT/happy', 'g': '', 's': 'Bien!'}, [('time', 0.1, 'choice')]),
    'daccord': ( {'e':'QT/happy', 'g': '', 's': 'D\'accord!'}, [('time', 0.1, 'choice')]),
    'pas_daccord': ( {'e':'QT/sad', 'g': '', 's': 'Pas d\'accord!'}, [('time', 0.1, 'choice')]),
    'pardon': ( {'e':'QT/talking', 'g': '', 's': 'Pardon.'}, [('time', 0.1, 'choice')]),
    'merci': ( {'e':'QT/talking', 'g': '', 's': 'Merci!'}, [('time', 0.1, 'choice')]),
    'enchante': ( {'e':'QT/happy', 'g': '', 's': 'Enchanté!'}, [('time', 0.1, 'choice')]),
    'au_revoir': ( {'e':'QT/talking', 'g': '', 's': 'Au revoir!'}, [('time', 0.1, 'choice')]),
    'de_rien': ( {'e':'QT/talking', 'g': '', 's': 'De rien!'}, [('time', 0.1, 'choice')]),
    'plaisir': ( {'e':'QT/happy', 'g': '', 's': 'Avec plaisir'}, [('time', 0.1, 'choice')]),

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
}