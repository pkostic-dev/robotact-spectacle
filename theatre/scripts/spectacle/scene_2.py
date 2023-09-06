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
            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),

            ('key', 'r', 'rien'),     
            ('key', 't', 'toujours'), ('key', 'T', 'tout'),
            ('key', 'y', 'super'),    ('key', 'Y', 'et_toi'),
            ('key', 'u', 'peux'),     ('key', 'U', 'peuxpas'),
            ('key', 'o', 'oui'),      ('key', 'O', 'mais_oui'),
            ('key', 'p', 'peutetre'), ('key', 'P', 'parfois'),

            ('key', 'f', 'fort'),     ('key', 'F', 'faible'),
            # G
            ('key', 'h', 'salut'),    ('key', 'H', 'cava'),
            ('key', 'k', 'quand'),    ('key', 'K', 'pourquoi'),
            ('key', 'j', 'sais'),     ('key', 'J', 'saispas'),
            ('key', 'l', 'quoi'),     ('key', 'L', 'qui'),
            # M

            # V
            ('key', 'b', 'biensur'),  ('key', 'B', 'biensur_non'),
            ('key', 'n', 'non'),      ('key', 'N', 'mais_non'),
            
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

    'salut': ( {'e': '', 'g': '', 's': 'Salut!'}, [('time', 0.1, 'choice')]),
    'sais': ( {'e': '', 'g': '', 's': 'Je sais'}, [('time', 0.1, 'choice')]),
    'saispas': ( {'e': '', 'g': '', 's': 'Je ne sais pas'}, [('time', 0.1, 'choice')]),
    'oui': ( {'e': '', 'g': '', 's': 'Oui!'}, [('time', 0.1, 'choice')]),
    'mais_oui': ( {'e': '', 'g': '', 's': 'Mais oui!'}, [('time', 0.1, 'choice')]),
    'non': ( {'e': '', 'g': '', 's': 'Non!'}, [('time', 0.1, 'choice')]),
    'mais_non': ( {'e': '', 'g': '', 's': 'Mais non!'}, [('time', 0.1, 'choice')]),
    'biensur': ( {'e': '', 'g': '', 's': 'Oui, Biensur!'}, [('time', 0.1, 'choice')]),
    'biensur_non': ( {'e': '', 'g': '', 's': 'Biensur que non!'}, [('time', 0.1, 'choice')]),
    'rien': ( {'e': '', 'g': '', 's': 'Rien!'}, [('time', 0.1, 'choice')]),
    'tout': ( {'e': '', 'g': '', 's': 'Tout!'}, [('time', 0.1, 'choice')]),
    'super': ( {'e': '', 'g': '', 's': 'Super!'}, [('time', 0.1, 'choice')]),
    'peux': ( {'e': '', 'g': '', 's': 'Je peux'}, [('time', 0.1, 'choice')]),
    'peuxpas': ( {'e': '', 'g': '', 's': 'Je ne peux pas'}, [('time', 0.1, 'choice')]),
    'toujours': ( {'e': '', 'g': '', 's': 'Toujours'}, [('time', 0.1, 'choice')]),
    'peutetre': ( {'e': '', 'g': '', 's': 'Peut-être'}, [('time', 0.1, 'choice')]),
    'parfois': ( {'e': '', 'g': '', 's': 'Parfois'}, [('time', 0.1, 'choice')]),
    'qui': ( {'e': '', 'g': '', 's': 'Qui?'}, [('time', 0.1, 'choice')]),
    'quand': ( {'e': '', 'g': '', 's': 'Quand?'}, [('time', 0.1, 'choice')]),
    'quoi': ( {'e': '', 'g': '', 's': 'Quoi?'}, [('time', 0.1, 'choice')]),
    'pourquoi': ( {'e': '', 'g': '', 's': 'Pourquoi?'}, [('time', 0.1, 'choice')]),
    'cava': ( {'e': '', 'g': '', 's': 'ça va?'}, [('time', 0.1, 'choice')]),
    'et_toi': ( {'e': '', 'g': '', 's': 'Et toi?'}, [('time', 0.1, 'choice')]),
    'fort': ( {'e': '', 'g': '', 's': 'Fort!'}, [('time', 0.1, 'choice')]),
    'faible': ( {'e': '', 'g': '', 's': 'Faible!'}, [('time', 0.1, 'choice')]),
}