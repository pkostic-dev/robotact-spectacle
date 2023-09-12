##################################################### SCENE 20 ######################################################

# → SCÈNE 11 : séquence de l’adoption, avec QT Simona et Konstantinos. Le robot joue désormais un rôle, il est devenu un personnage de fiction.  [scène déjà existante, à répéter 1er semaine] + → SCÈNE 12 : séquence de l'araigné,  QT se rebelle et il nous montre son monde intérieur  [scène déjà existante, à répéter 1er semaine]

# NOTE :
#   w_* : Wizard of Oz
#   s_* : automatic sequence

# TODO Update
# TODO Add spider, pacman

arm_up_left = [-97, -54, -46]
arm_up_right = [97, -54, -46]

arm_table_left = [0,0,0]
arm_table_right = [0,0,0]

states = {
    # ! pacman [P] durée = 14sec
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
        [('time', 2, 's_cest_juste')]
    ),

    's_cest_juste': (
        {
            's': 'C\'est juste que',
            'e': 'QT/talking'
        },[('time', 4, 's_je_ne_vois')]
    ),

    's_je_ne_vois': (
        {
            's': 'Je ne  vois aucune raison pour aller à l’école',
            'e': 'QT/disgusted'
        },[('time', 0.1, 'choice')]
    ),
    
    'w_je_suis': (
        {
            's': 'Je suis connecté à une bibliothèque universelle de données mise  à jour jusqu\'en 2021.',
            'e': 'QT/talkinglong'
        },[('time', 0.1, 'choice')]
    ),

    'w_qu_est_ce': (
        {
            's': '#MMM01# \\pau=500\\Qu’est-ce que tu entends, maman', # TODO test MMM
            'e': 'QT/confused'
        },[('time', 0.1, 'choice')]
    ),

    # ! bouge la tete avec impatience [a] [e]

    'w_on_va_manger': (
        {
            's': 'On va manger ou pas?',
            'e': 'QT/talking'
         },[('time', 0.1, 'choice')]
    ),
    
    'w_quoi': (
        {
            's': 'Quoi!',
            'e': 'QT/confused'
        },[('time', 0.1, 'choice')]
    ),
    
    'w_mais_non': (
        {'s': 'Mais non...'},[('time', 0.1, 'choice')]
    ),

    'w_vous_etes': (
        {'s': 'Vous êtes papa et maman moi je suis un enfant'},[('time', 0.1, 'choice')]
    ),

    'w_ah_bon': (
        {
            's': '\\pau=500\\Ah bon ?',
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
        {'s': 'Ouais alors?'},[('time', 2, 's_tiens')]
    ),

    's_tiens': (
        {
            's': 'Tiens!',
            'ra': [97, -54, -46] # TODO test
        },[('time', 2, 's_il_y_a')]
    ),

    's_il_y_a': (
        {
            's': 'Il y a une araignée au plafond.',
            'e': 'QT/surprise'
        },[('time', 0.1, 'choice')]
    ),
    
    # ! regarder le public [s]
    'w_cest_dingue': (
        {
            's': 'C’est dingue ces bêtes-là ! C’est fascinant de regarder les araignées, ils sont si intéressantes',
            'e': 'QT/talkinglong'
        },[('time', 0.1, 'choice')]
    ),

    'w_moi_le_rebel': (
        {
            's': 'Moi ? Le rebel ? Qu’est ce que tu racontes ?',
            'e': 'QT/talking'
        },[('time', 4, 's_pas_du_tout')]
    ),

    's_pas_du_tout': (
        {
            's': 'Pas du tout !',
            'e': 'QT/angry'
        },[('time', 3, 's_cest_juste_que')]
    ),

    's_cest_juste_que': (
        {
            's': 'C’est juste que j’ai marre de  parler de l’école, les araignées sont beaucoup plus kiffants ',
            'e': 'QT/talkinglong'
        },
        [('time', 0.1, 'choice')]
    ),
    
    'w_ouais_il': (
        {
            's': 'Ouais il fait semblant',
            'e': 'QT/talking'
        },[('time', 0.1, 'choice')]
    ),

    # ! visage neutre
    # TODO add trigger, behavior, key

    # ! regarde en haut [z]
    # ! leve le bras [b]
    
    'w_ah_une_autre': (
        {
            's': 'Ah! Une autre araignée ! Il y en deux',
            'e': 'QT/talking'
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
        {
            's': 'Trois araignées ! Une famille comme nous',
            'e': 'QT/talking'
        },[('time', 0.1, 'choice')]
    ),

    # ! regarde les parents
    # ! son pere parle
    # ! confused [O]
    # ! les parents parlent
    # ! confused [O]

    'w_comment_ca': (
        {
            's': 'Comment ça s\'est fait que je ne l\'ai pas en mémoire.. J\'ai toujours été votre seul enfant !',
            'e': 'QT/talkinglong'
        },[('time', 0.1, 'choice')]
    ),

    'w_attends_jai': (
        {
            's': 'Attends j\'ai un frère alors?!',
            'e': 'QT/surprise'
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
            's': 'Pourtant j’ai le même prénom.',
            'e': 'QT/confused'
        },[('time', 0.1, 'choice')]
    ),

    'w_maintenant_peut_etre': (
        {
            's': 'Maintenant peut-être, mais s’il était toujours là? Je serais à la table?',
            'e': 'QT/talkinglong'
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
    # ! pluie [L]
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

    # TODO test
    'arm_up_right': ({'ra': arm_up_right,},[('time', 0.1, 'choice')]),
    'arm_table_right': ({'ra': arm_table_right,},[('time', 0.1, 'choice')]),
    'arms_table' : ({'ra': arm_table_right,'la': arm_table_left},[('time', 0.1, 'choice')]),

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
            ('key', 'i', 'w_laisse_moi'),

            # Emotions + Videos + Actions
            ('key', 'H', 'happy'),
            ('key', 'I', 'surprise'),
            ('key', 'G', 'disgust'),
            ('key', 'R', 'angry'),
            ('key', 'T', 'talking'),
            ('key', 'O', 'confused'),
            # TODO add other emotions for final scene

            ('key', 'P', 'pacman'),
            ('key', 'L', 'pluie'),
            
            ('key', 'b', 'arm_up_right'),
            ('key', 'B', 'arm_down_right'),
            ('key', 'N', 'arms_table'),
            ('key', 'n', 'neutral'),

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

    'look_up_short': ( {'s': '', 'h': [0.0,-10.0]}, [('time', 0.1, 'choice')]),
    'look_down_short': ( {'s': '', 'h': [0.0,+5.0]}, [('time', 0.1, 'choice')]),
    'look_right_short': ( {'s': '', 'h': [-10.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left_short': ( {'s': '', 'h': [+10.0,0.0]}, [('time', 0.1, 'choice')]),

    # Control
    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,
}

'''
QT est seul sur scène. Sur son  écran il y a une projection du jeu vidéo Pac-Man accompagné par ses effets sonores. ATTENTION pour le moment le son et la vidéo viennent de 2 sources différentes !! (projections possible sur le cube du fond scène, comme s’il était un frigo, ou un etagère d’une cuisine)

Entre Konstantinos 

KONSTANTINOS : Arthur, arrête de jouer! On va bientôt manger, maman ne va pas tarder. 
QT : Attends deux minutes, j’ai presque fini le niveau ! (toujours Pac-Man) 
 KONSTANTINOS : Allez assez de jeux vidéo (QT étant (toujours Pac-Man → il trouve la tête et regarde son père)
QT : Mais papa je n’ai pas trop faim. Je me suis rechargé ce matin.
KONSTANTINOS : Pas grave on va se mettre à table tous ensemble.
Entre SIMONA
SIMONA : Bonjour mes amours ! (QT regarde sa maman / visage content) Quel plaisir de vous retrouver 
KONSTANTINOS : Salut chérie, ça a été  le travail ? 
SIMONA : Plus ou moins. (QT  suis la conversation)
KONSTANTINOS: Ah, non…
SIMONA : Je suis fatiguée. Trop de réunions interminables. Le dîner a l’air bon. 
KONSTANTINOS: Tu as vu..
SIMONA : Mon cœur,  comment c’était ton premier jour au collège?
K:  C’est vrai, tu m’as rien dit. Raconte-nous alors ta journée 
QT : Ça allait
KONSTANTINOS : Juste ça? Tu as eu des (QT fait non avec la tête) ennuis ?
QT : Non pas du tout 
KONSTANTINOS : Tant mieux
SIMONA : Et tes copains ?
QT : (Pause / Silence QT regarde vers le bas)
SIMONA:  Ça se passe bien avec les autres….? 
QT : Les autres quoi ? 
SIMONA: Les autres  enfants, ceux qui sont…(QT coupe sa mere)
QT: Oui, oui…(QT visage puffing) C’est juste que… Je ne  vois aucune raison pour aller à l’école
KONSTANTINOS: Si tu vas y apprendre beaucoup 
QT: (QT parle) Je suis connecté à une bibliothèque universelle de données mise  à jour jusqu'en 2021. 
SIMONA: On va à l’école pour apprendre à vivre avec les autres aussi, pour apprécier nos différences. Nous sommes tous uniques, toi tu es unique 
QT (QT confused + son mmm) Qu’est-ce que tu entends, maman…: 
KONSTANTINOS: Par exemple, nous trois on est pas pareils
QT : (QT Bouge la tête à droite et à gauche, avec impatience) …on va manger ou pas ?
SIMONA : Papa te parle
QT : QUOI
SIMONA : Est-ce que nous trois nous sommes tous pareils ?
QT : Mais non
KONSTANTINOS : Voilà
SIMONA : Exactement
QT : Vous êtes papa et maman moi je suis votre fils 
SIMONA : Non, oui d’accord mais papa veut dire… quand on se regarde dans le miroir on voit qu’on est différents tous les trois
QT : (QT confused) Ah bon ?
SIMONA: Oui
QT : Chais pas (Je ne sais pas)
SIMONA : Ta main, regarde, la mienne aussi, on se ressemble, mais pas autant. …
QT: (Regarde les mains, puis en haut. QT fait partie musique Pac-man)
KONSTANTINOS: Arthur, écoute! (QT arrête de jouer Pac-Man) Nos corps ne se ressemblent pas ; regarde là-bas notre reflet. Tu vois ? 
SIMONA: (QT regarde en bas) Tu regardes où ? C’est là-bas! 
QT:  (QT lève sa tête) Ouais alors? (lève un bras)TIENS ! (QT surprise) Il y a une araignée au plafond.
KONSTANTINOS: Arthur ! S’il te plaît !
QT : (baisse la tête et le bras / regarde le public et “parole”) C’est dingue ces bêtes-là ! C’est fascinant de regarder les araignées, ils sont si intéressantes…
KONSTANTINOS: Tu fais ton rebel maintenant
QT : Moi ? Le rebel ? Qu’est ce que tu racontes ? (Visage fâché) Pas du tout ! ( Secoue la tête) C’est juste que j’en ai marre de  parler de l’école, les araignées sont beaucoup plus kiffantes 
SIMONA : Arthur, c’est quoi ce langage ?! Papa se préoccupe de toi
QT: Ouais il fait semblant (QT visage neutre)
KONSTANTINOS : N’oublie pas d’un coup ce qu’on fait pour toi : les mises à jour, les batteries remplacées, toute les fois où je t’ai graissé les pièces avec amour !
SIMONA: Moi je pense qu’il est assez intelligent pour savoir de quoi on parle. Papa et moi on est des humains et toi…
QT: (QT lève sa tête et le bras) Ah! Une autre araignée ! Il y en deux (projections araignés sur écrans de QT, Predrag s’en occupe)
SIMONA:  Tu joues à quoi, là? (QT baisse bras et tête, Simona en s’adressant à Konstantinos) On y arrivera jamais! 
KONSTANTINOS: C’est toi qui voulait démarrer cette discussion.
SIMONA: Mais, non, on l’avait décidé ensemble.
QT:  (QT lève sa tête et le bras)  Trois araignées (projections araignés sur cubes)
! Une famille comme nous
SIMONA : Non pas tout à fait..toi, .tu es un enfant ..un enfant robotique… (QT les regardes)
KONSTANTINOS: Un enfant robot ! Robot-enfant. (QT confused)
SIMONA: (à Konstantinos) Mais enfin, dis-lui !
KONSTANTINOS: Avant toi, il y a longtemps, on avait un autre Arthur…je veux dire
un autre fils 
QT: (QT confused + parle) Comment ça s'est fait que je ne l’ai pas en mémoire.. J'ai toujours été votre seul enfant !
SIMONA: On  t’a configuré…hemm éduqué comme ça. 
QT: Attends j'ai un frère alors?!
KONSTANTINOS: Non, il n’est plus ici.
QT: (QT parle) Mais il est où?
SIMONA:   Il n’est plus avec nous. (Qt regarde sa mère)
KONSTANTINOS: C’est comme ça. 
SIMONA: Voilà, c’est comme ça. 
QT: (QT parle) Et vous ne me l'aviez jamais dit ?
KONSTANTINOS: Maman en était malade
SIMONA: Dans nos vies, il y avait un grand vide
KONSTANTINOS: Puis on t’a adopté, on a retrouvé du bonheur
QT: (QT angry + parle) Alors, je suis un remplaçant?
KONSTANTINOS: Bien sûr que non
QT:  Pourtant j’ai le même prénom.
SIMONA: Non, oui alors c’est parce que c’est un joli prénom
KONSTANTINOS: Tu n’es pas lui, tu es toi-même, tu es tout pour nous
QT: (QT  parle) Maintenant peut-être, mais s’il était toujours là? Je serais à la table?
SIMONA: (Elle lui donne un bisou)
QT: (QT expression de petit dégoût) Laisse-moi !!!
Longue silence inconfortable 
KONSTANTINOS: Allez on débarrasse la table, et on en reparle plus tard, d'accord ?
silence de QT, il ne fais rien, Simona touche Qt
SIMONA : Mais tu sais, tu reste notre fils après tout !
QT: Peut-être…je retourne jouer.

'''