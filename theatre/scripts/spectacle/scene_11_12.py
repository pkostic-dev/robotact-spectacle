##################################################### SCENE 11 + 12 ####################################################

# → SCÈNE 11 : séquence de l’adoption, avec QT Simona et Konstantinos. Le robot joue désormais un rôle, il est devenu un personnage de fiction.  [scène déjà existante, à répéter 1er semaine] + → SCÈNE 12 : séquence de l'araigné,  QT se rebelle et il nous montre son monde intérieur  [scène déjà existante, à répéter 1er semaine]

# NOTE :
#   w_* : Wizard of Oz
#   s_* : automatic sequence

# TODO Update
# TODO Add spider, pacman

states = {
    # ! [P]
    'pacman': (
        {'s': '', 'e': 'QT/pacman'},[('time', 0.1, 'choice')]
    ),

    'w_attends': (
        {'s': 'Attends deux minutes, j’ai presque fini le niveau!'},[('time', 0.1, 'choice')]
    ),
    
    # ! Regarde son pere [q]

    'w_mais_papa': (
        {'s': 'Mais papa je n’ai pas trop faim. Je me suis rechargé ce matin'},[('time', 0.1, 'choice')]
    ),

    # ! Regarde sa maman quand elle rentre [d]
    # ! Visage content [H]

    'w_ca_allait': (
        {'s': 'ça allait'},[('time', 0.1, 'choice')]
    ),

    # ! Non avec la tete pendant que son pere parle [Q] [D]

    'w_non_pas': (
        {'s': 'Non pas du tout'},[('time', 0.1, 'choice')]
    ),

    # ! Regarde vers le bas [x]

    'w_les_autres': (
        {'s': 'Les autres quoi ?'},[('time', 0.1, 'choice')]
    ),

    # ! coupe sa mere
    'w_oui_oui': (
        {'s': 'Oui, oui'},
        [('time', 2, 'c_cest_juste')]
    ),

    's_cest_juste': (
        {
            's': 'C\'est juste que',
            'e': 'QT/puffing_the_chredo_eeks'
        },[('time', 3, 'c_je_ne_vois')]
    ),

    's_je_ne_vois': (
        {'s': 'Je ne  vois aucune raison pour aller à l’école'},[('time', 0.1, 'choice')]
    ),
    
    'w_je_suis': (
        {
            's': 'Je suis connecté à une bibliothèque universelle de données mise  à jour jusqu\'en 2021.',
            'e': 'QT/talking'
        },[('time', 0.1, 'choice')]
    ),

    'w_qu_est_ce': (
        {
            's': '#MMM01# Qu’est-ce que tu entends, maman', # TODO test MMM
            'e': 'QT/confused'
        },[('time', 0.1, 'choice')]
    ),

    # ! bouge la tete avec impatience [a] [e]

    'w_on_va_manger': (
        {'s': 'On va manger ou pas?'},[('time', 0.1, 'choice')]
    ),
    
    'w_quoi': (
        {'s': 'Quoi!'},[('time', 0.1, 'choice')]
    ),
    
    'w_mais_non': (
        {'s': 'Mais non...'},[('time', 0.1, 'choice')]
    ),

    'w_vous_etes': (
        {'s': 'Vous êtes papa et maman moi je suis un enfant'},[('time', 0.1, 'choice')]
    ),

    'w_ah_bon': (
        {
            's': 'Ah bon ?',
            'e': 'QT/confused'
        },[('time', 0.1, 'choice')]
    ),

    'w_chais_pas': (
        {'s': 'Chais pas'},[('time', 0.1, 'choice')]
    ),

    # ! regarde ses mains [w] [c]
    # ! regarde en haut [z]
    # ! pacman [P]
    # ! regarde en bas [x]
    # ! regarde en haut [z]

    'w_ouais_alors': (
        {'s': 'Ouais alors?'},[('time', 2, 'c_tiens')]
    ),

    's_tiens': (
        {
            's': 'Tiens!',
            'ra': [97, -54, -46] # TODO test
        },[('time', 2, 'c_il_y_a')]
    ),

    's_il_y_a': (
        {
            's': 'Il y a une araignée au plafond.',
            'e': 'QT/surprise'
        },[('time', 0.1, 'choice')]
    ),
    
    # ! talking [T]
    'w_cest_dingue': (
        {
            's': '\\pau=1000\\C’est dingue ces bêtes-là ! C’est fascinant de regarder les araignées, ils sont si intéressantes',
            'h': [0.0, 0.0]
        },[('time', 0.1, 'choice')]
    ),

    'w_moi_le_rebel': (
        {
            's': 'Moi ? Le rebel ? Qu’est ce que tu racontes ?'
        },[('time', 4, 'c_pas_du_tout')]
    ),

    's_pas_du_tout': (
        {
            's': 'Pas du tout !',
            'e': 'QT/angry'
        },[('time', 3, 'c_cest_juste_que')]
    ),

    's_pas_du_tout': (
        {'s': 'C’est juste que j’ai marre de  parler de l’école, les araignées sont beaucoup plus kiffants '},
        [('time', 0.1, 'choice')]
    ),
    
    'w_ouais_il': (
        {
            's': 'Ouais il fait semblant'
        },[('time', 0.1, 'choice')]
    ),

    # ! visage neutre
    # TODO add trigger, behavior, key

    # ! regarde en haut [z]
    # ! leve le bras [b]
    
    'w_ah_une_autre': (
        {
            's': 'Ah! Une autre araignée ! Il y en deux'
        },[('time', 4, 's_araignee')]
    ),

    's_araignee': (
        {
            's': '',
            'e': 'QT/araignee'
        },[('time', 0.1, 'choice')]
    ),

    # TODO
    # ! pendant que la maman parle
    # ! baisse le bras
    # ! baisse la tete [x]

    # ! quand les parents finissent de parler
    # ! leve le bras [b]
    # ! leve la tete [z]

    'w_trois_araignees': (
        {'s': 'Trois araignées ! Une famille comme nous'},[('time', 0.1, 'choice')]
    ),

    # ! regarde les parents
    # ! son pere parle
    # ! confused [O]
    # ! les parents parlent
    # ! confused [O]

    'w_comment_ca': (
        {
            's': 'Comment ça s\'est fait que je ne l\'ai pas en mémoire.. J\'ai toujours été votre seul enfant !',
            'e': 'QT/talking'
        },[('time', 0.1, 'choice')]
    ),

    'w_attends_jai': (
        {
            's': 'Attends j\'ai un frère alors?!'
        },[('time', 0.1, 'choice')]
    ),

    'w_mais_il': (
        {
            's': 'Mais il est où',
            'e': 'QT/talking'
        },[('time', 0.1, 'choice')]
    ),

    # ! regarde sa maman

    'w_et_vous': (
        {
            's': 'Et vous ne me l\'aviez jamais dit?',
            'e': 'QT/talking'
        },[('time', 0.1, 'choice')]
    ),

    # ! angry [R]

    'w_alors_je': (
        {
            's': 'Alors, je suis un remplaçant ?',
            'e': 'QT/talking'
        },[('time', 0.1, 'choice')]
    ),
    
    'w_pourtant_jai': (
        {
            's': 'Pourtant j’ai le même prénom.'
        },[('time', 0.1, 'choice')]
    ),

    'w_maintenant_peut_etre': (
        {
            's': 'Maintenant peut-être, mais s’il était toujours là? Je serais à la table?'
        },[('time', 0.1, 'choice')]
    ),

    'w_laisse_moi': (
        {
            's': 'Laisse-moi!',
            'e': 'QT/disgusted'
        },[('time', 0.1, 'choice')]
    ),

    # ! silence incofortable

    'w_peut_etre': (
        {
            's' : 'Peut-être\\pau=500\\je retourne jouer.',
            'e' : 'QT/talking'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # TODO longue video de pluie
    'pluie': (
        {
            's' : '',
            'e' : 'QT/pluie'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # ! eteindre QT

    # TODO check
    'arm_up': ({'ra': [97, -54, -46],},[('time', 0.1, 'choice')]),
    # TODO test
    'arm_down': ({'ra': [97, -54, -46],},[('time', 0.1, 'choice')]),

    'surprise': ({'e': 'QT/surprise',},[('time', 0.1, 'choice')]),
    'disgust': ({'e': 'QT/disgust',},[('time', 0.1, 'choice')]),
    'angry': ({'e': 'QT/angry',},[('time', 0.1, 'choice')]),
    'talking' : ( {'e':'QT/talking','g': '', 's': ''}, [('time', 1, 'choice')]),
    'happy' : ( {'e':'QT/happy','g': '', 's': ''}, [('time', 1, 'choice')]),
    'confused' : ( {'e':'QT/confused','g': '', 's': ''}, [('time', 1, 'choice')]),
    
    'neutral': ({'g' : 'QT/neutral',},[('time', 0.1, 'choice')]),

    'choice': (
        {},
        [
            # WOZ Dialogue Page 1
            ('key', '&', 'w_attends'),
            ('key', 'é', 'w_mais_papa'),
            ('key', '"', 'w_ca_allait'),
            ('key', '\'', 'w_non_pas'),
            ('key', '(', 'w_les_autres'),
            ('key', '-', 'w_oui_oui'),
            ('key', 'è', 'w_je_suis'),
            ('key', '_', 'w_qu_est_ce'),
            ('key', 'ç', 'w_on_va_manger'),
            ('key', 'à', 'w_quoi'),
            ('key', ')', 'w_mais_non'),
            ('key', '=', 'w_vous_etes'),

            # WOZ Dialogue Page 2
            ('key', '1', 'w_ah_bon'),
            ('key', '2', 'w_chais_pas'),
            ('key', '3', 'w_ouais_alors'),
            ('key', '4', 'w_cest_dingue'),
            ('key', '5', 'w_moi_le_rebel'),
            ('key', '6', 'w_ouais_il'),
            ('key', '7', 'w_ah_une_autre'),
            ('key', '8', 'w_trois_araignees'),
            ('key', '9', 'w_comment_ca'),
            ('key', '0', 'w_attends_jai'),
            ('key', '°', 'w_mais_il'),
            ('key', '+', 'w_et_vous'),

            # WOZ Dialogue Page 3
            ('key', 'r', 'w_alors_je'),
            ('key', 't', 'w_pourtant_jai'),
            ('key', 'y', 'w_maintenant_peut_etre'),
            ('key', 'u', 'w_laisse_moi'),

            # Emotions + Videos + Actions
            ('key', 'H', 'happy'),
            ('key', 'I', 'surprise'),
            ('key', 'G', 'disgust'),
            ('key', 'R', 'angry'),
            ('key', 'T', 'talking'),
            ('key', 'O', 'confused'),

            ('key', 'P', 'pacman'),
            ('key', 'L', 'pluie'),
            
            ('key', 'b', 'arm_up'),
            ('key', 'B', 'arm_down'),
            #('key', 'n', 'neutral'),

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

            ('key', 'Q', 'look_left_short'),
            ('key', 'D', 'look_right_short'),

            # TODO arms
            # TODO disable motors during first part then enable right arm for pointing
            # IDLE
            # rosservice call /qt_robot/motors/setControlMode ['right_arm', 'left_arm'] 0

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

    'look_right_short': ( {'s': '', 'h': [-10.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left_short': ( {'s': '', 'h': [+10.0,0.0]}, [('time', 0.1, 'choice')]),

    # Control
    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,
}