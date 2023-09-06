''' Groupe QT / magicien d’OZ

Version 3

Avec : “Moez, Jérémie, Franciele, Constantinos”
(notes JD en phonétique, merci de rectifier)

Indication pour Predrag et Walid : sauf contre-indication, ne pas changer les
améliorations de lettrage qui ont été faites directement dans le programme
(voyelles multiples, points d’exclamation, etc.)

Le personnage du BLESSÉ est joué par un·e humain·e.
Le reste du texte doit être associé à des touches (avec en même temps le geste
ou l’expression faciale décrite entre parenthèses)

QT est à droite du Blessé au sol.

Notes dev
---------
Sons interessants : #CRY01#, #AARGH01#, #BREATH01#, #MMM01#, #LAUGH01#, #YAWN01#
Tags :
    Vitesse : \\rsp=60\\
    Pitch : \\vct=90\\
        (on peut combiner les deux pour compenser)
    Spelling : \\rms=1\\letter\\rms=0\\
    Word by word : \\rmw=1\\word by word\\rmw=0\\
    Pause : \\pau=300\\ (in ms)
    Liste des exclamations : 
    acapela-group.com/www/static/website/VocalSmileys/excla.html#French%20EXCLA

'''

states_malika = {
    'begin': ({}, [('time', 1, 'choice')]),

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 'r1'),
            ('key', 'é', 'r2'),
            ('key', '\"', 'r3'),
            ('key', '\'', 'r4'),
            ('key', '(', 'r5'),
            ('key', '-', 'r6'),
            ('key', 'f', 'sad'),

            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),

            ('key', 'j', 'end'),
        ]
    ),

    'r1': ( {'e': '', 'g': '', 's': 'Il est temps que je pars.'}, [('time', 1, 'choice')]),
    # reviandras
    'r2': ( {'e': '', 'g': '', 's': 'Il n\'y ayra pas de retour.'}, [('time', 1, 'choice')]),
    # pas avec toi ?
    'r3': ( {'e': '', 'g': '', 's': 'Ce n\'est pas ton tour.'}, [('time', 1, 'choice')]),
    # tu vas m'appeler ?

    # m'endormir
    'r4': ( {'e': '', 'g': '', 's': 'Quand tu fermes les yeux, une nuit bleue, tu me vois dans tes reves.'}, [('time', 1, 'choice')]),
    # [coupe la parole]
    'r5': ( {'e': '', 'g': '', 's': 'Le temps est venu'}, [('time', 1, 'choice')]),

    'f': ( {'e': '', 'g': '', 's': ''}, [('time', 1, 'choice')]),

    'look_up': ( {'s': '', 'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'sad' : ( {'e':'QT/very_sad','g': '', 's': ''}, [('time', 3, 'choice')]),

    'end': ((), [('time', 0.1, 'end')])
}

states_sara = {
    'begin': ({}, [('time', 1, 'choice')]),

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 'r1'),
            ('key', 'é', 'r2'),
            ('key', '\"', 'r3'),
            ('key', '\'', 'r4'),
            ('key', '(', 'r5'),
            ('key', '-', 'r6'),
            ('key', 'è', 'r7'),
            ('key', '_', 'r8'),
            ('key', 'ç', 'r9'),
            ('key', 'à', 'r10'),
            ('key', ')', 'r11'),
            ('key', '=', 'r12'),
            ('key', 'f', 'fin'),

            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),
            ('key', 'h', 'hello'),
            ('key', 'k', 'dontknow'),
            ('key', 'y', 'oui'),
            ('key', 'n', 'non'),
            ('key', 'g', 'public'),
            ('key', 'r', 'objetDroite'),
            ('key', 'l', 'objetGauche'),
            ('key', 'p', 'pense'),
            ('key', 'o', 'pense2'),
            ('key', 'm', 'neutral'),
            ('key', 'R', 'really'),
            ('key', 'H', 'hug'),
            ('key', 'J', 'jaime'),
            ('key', 'Y', 'happy'),
            ('key', 'K', 'kisses'),
            ('key', 'E', 'excited'),
            ('key', 't', 'thinking'),
            ('key', 'C', 'cry'),
            ('key', 'O', 'confused'),
            ('key', 'b', 'bored'),
            ('key', 'j', 'end'),
        ]
    ),

    'r1': ( {'e': 'QT/surprise', 'g': '', 's': 'Tu as besoin de parler ?'}, [('time', 1, 'choice')]),
    'r2': ( {'e': '', 'g': '', 's': 'Vas voir un psychologue, je suis sûr que ça t\'aidera'}, [('time', 1, 'choice')]),
    'r3': ( {'e': '', 'g': '', 's': 'Alors change toi les idées, fais des activités qui te motivent.'}, [('time', 1, 'choice')]),
    # TODO [C] -> cry
    'r4': ( {'e': '', 'g': '', 's': 'Tu veux un câlin ?'}, [('time', 1, 'choice')]),
    # TODO : [H] -> hug
    'r5': ( {'e': '', 'g': '', 's': 'ça t\'apporterait du réconfort'}, [('time', 1, 'choice')]),
    'r6': ( {'e': '', 'g': '', 's': 'Alors disparais et enterre-toi Mais si tu veux une solution pour aller mieux, ça ne dépend que de toi'}, [('time', 1, 'choice')]),

    'look_up': ( {'s': '', 'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),

    'hello': ( {'e': 'QT/happy', 'g': 'QT/hi', 's': '\\pau=2000\\Salut!', 'h': [0,0]}, [('time', 1, 'choice')]),
    'dontknow': ( {'e': '', 'g': 'QT/touch-head', 's': '~\\pau=500\\Je ne sais pas'}, [('time', 1, 'choice')]),
    'oui': ( {'e': '', 'g': 'QT/imitation/nodding-yes', 's': '~\\pau=500\\Oui!'}, [('time', 1, 'choice')]),
    'non': ( {'e': '', 'g': 'QT/emotions/sad', 's': '~\\pau=500\\Non!'}, [('time', 1, 'choice')]),
    'suivi': ( {'e': 'QT/surprise', 'g': 'QT/imitation/head-right-left', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'public': ( {'e': 'QT/surprise', 'h': [0.0,0.0], 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'objetDroite': ( {'e': 'QT/happy', 'h': [+10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
    'objetGauche': ( {'e': 'QT/happy', 'h': [-10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
    'pense': ( {'e': 'QT/confused', 'g': 'QT/imitation/hands-on-hip', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'pense2': ( {'e': 'QT/afraid', 'g': 'QT/touch-head-back', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'neutral': ( {'e': 'QT/neutral', 'g': 'QT/neutral', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'really': ( {'e': 'QT/dirty_face','g': 'QT/surprise', 's': '\\pau=2000\\Vraiment ?'}, [('time', 3, 'choice')]),
    'comment': ( {'e':'QT/surpise','g': 'QT/touch-head', 's': '\\pau=2000\\Comment ?'}, [('time', 3, 'choice')]),
    'jaime': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=2000\\jème beaucoup !'}, [('time', 3, 'choice')]),
    'happy': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=500\\ Youpi !'}, [('time', 3, 'choice')]),

    'kisses': ( {'e':'QT/kiss','g': 'QT/kiss'}, [('time', 3, 'kisses1')]),
    'kisses1': ( {'e':'QT/one_eye_wink','g': 'QT/neutral'}, [('time', 3, 'kisses2')]),
    'kisses2': ( {'e':'QT/shy','h': [-10.0,+10.0]}, [('time', 3, 'choice')]),

    'excited': ( {'e':'QT/surpise','g': 'QT/neutral'}, [('time', 3, 'excited1')]),
    'excited1': ( {'e':'QT/happy','g': 'QT/neutral'}, [('time', 3, 'choice')]),

    'thinking': ( {'e':'QT/surpise','g': 'QT/bored'}, [('time', 3, 'choice')]),

    'curious': ( {'e':'QT/suprise','g': 'QT/neutral'}, [('time', 3, 'curious1')]),
    'curious1': ( {'e':'QT/showing_smile','g': 'QT/neutral'}, [('time', 3, 'choice')]),

    'cry': ( {'e':'QT/cry','g': 'QT/cry'}, [('time', 3, 'choice')]),
    'hug': ( {'e':'','g': 'QT/hug'}, [('time', 3, 'choice')]),

    'confused': ( {'e':'QT/confused','g': 'QT/neutral'}, [('time', 3, 'choice')]),
    'bored': ( {'e':'QT/yawn','g': 'QT/bored'}, [('time', 3, 'choice')]),

    'end': ((), [('time', 0.1, 'end')])
}


# Date : 29/06/2023

states_adoption = {
    'begin': ({}, [('time', 1, 'choice')]),

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 'r1'),
            ('key', 'é', 'r2'),
            ('key', '\"', 'r3'),
            ('key', '\'', 'r4'),
            ('key', '(', 'r5'),
            ('key', '-', 'r6'),
            ('key', 'è', 'r7'),
            ('key', '_', 'r8'),
            ('key', 'ç', 'r9'),
            ('key', 'à', 'r10'),
            ('key', ')', 'r11'),
            ('key', '=', 'r12'),
            ('key', '=', 'r12'),
            ('key', 'f', 'estque'),
            ('key', 'F', 'fin'),

            ('key', 'y', 'oui'),
            ('key', 'n', 'non'),

            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),
            ('key', 'h', 'hello'),
            ('key', 'k', 'dontknow'),
            ('key', 'g', 'public'),
            ('key', 'r', 'objetDroite'),
            ('key', 'l', 'objetGauche'),
            ('key', 'p', 'pense'),
            ('key', 'o', 'pense2'),
            ('key', 'm', 'neutral'),
            ('key', 'R', 'really'),
            ('key', 'H', 'comment'),
            ('key', 'J', 'jaime'),
            ('key', 'Y', 'happy'),
            ('key', 'K', 'kisses'),
            ('key', 'E', 'excited'),
            ('key', 't', 'thinking'),
            ('key', 'C', 'curious'),
            ('key', 'F', 'fear'),
            ('key', 'O', 'confused'),
            ('key', 'b', 'bored'),
            ('key', 'j', 'end'),
            ('speech', 'salut', 'salut')
        ]
    ),

    'r1': ( {'e': '', 'g': '', 's': 'Oui très bien maman'}, [('time', 1, 'choice')]),
    'r2': ( {'e': '', 'g': '',  's': 'D\'accord'}, [('time', 1, 'choice')]),

    'r3': ( {'e': '', 'g': '',  's': 'Comment ça se fait?'}, [('time', 1, 'choice')]),
    'r4': ( {'e': '', 'g': '',  's': 'Ah bon ?'}, [('time', 1, 'choice')]),
    'r5': ( {'e': '', 'g': '',  's': 'C\'est curieux'}, [('time', 1, 'choice')]),
    'r6': ( {'e': '', 'g': '',  's': 'Je comprends!'}, [('time', 1, 'choice')]),
    'r7': ( {'e': '', 'g': '',  's': 'Je ne comprends pas!'}, [('time', 1, 'choice')]),
    'r8': ( {'e': '', 'g': '',  's': 'Tu veut dire quoi?'}, [('time', 1, 'choice')]),
    'r9': ( {'e': '', 'g': '',  's': 'C\'est pas vrai!'}, [('time', 1, 'choice')]),
    'r10': ( {'e': '', 'g': '', 's': 'Quand ça?'}, [('time', 1, 'choice')]),
    'r11': ( {'e': '', 'g': '', 's': 'Pourquoi non?'}, [('time', 1, 'choice')]),
    'r12': ( {'e': '', 'g': '', 's': 'Qui était la?'}, [('time', 1, 'choice')]),
    'oui': ( {'e': '', 'g': '', 's': 'Oui.'}, [('time', 1, 'choice')]),
    'non': ( {'e': '', 'g': '', 's': 'Non!'}, [('time', 1, 'choice')]),

    'estque': ( {'e': '', 'g': '', 's': 'Est-ce que je le remplace?'}, [('time', 1, 'choice')]),
    'fin':  ( {'e': '', 'g': '', 's': 'Maman, Papa, je vous aime beaucoup'}, [('time', 1, 'choice')]),

    'look_up': ( {'s': '', 'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),

    'hello': ( {'e': 'QT/happy', 'g': 'QT/hi', 's': '\\pau=2000\\Salut!', 'h': [0,0]}, [('time', 1, 'choice')]),
    'dontknow': ( {'e': '', 'g': 'QT/touch-head', 's': '~\\pau=500\\Je ne sais pas'}, [('time', 1, 'choice')]),
    
    'suivi': ( {'e': 'QT/surprise', 'g': 'QT/imitation/head-right-left', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'public': ( {'e': 'QT/surprise', 'h': [0.0,0.0], 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'objetDroite': ( {'e': 'QT/happy', 'h': [+10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
    'objetGauche': ( {'e': 'QT/happy', 'h': [-10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
    'pense': ( {'e': 'QT/confused', 'g': 'QT/imitation/hands-on-hip', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'pense2': ( {'e': 'QT/afraid', 'g': 'QT/touch-head-back', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'neutral': ( {'e': 'QT/neutral', 'g': 'QT/neutral', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'really': ( {'e': 'QT/dirty_face','g': 'QT/surprise', 's': '\\pau=2000\\Vraiment ?'}, [('time', 3, 'choice')]),
    'comment': ( {'e':'QT/surpise','g': 'QT/touch-head', 's': '\\pau=2000\\Comment ?'}, [('time', 3, 'choice')]),
    'jaime': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=2000\\jème beaucoup !'}, [('time', 3, 'choice')]),
    'happy': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=500\\ Youpi !'}, [('time', 3, 'choice')]),

    'kisses': ( {'e':'QT/kiss','g': 'QT/kiss'}, [('time', 3, 'kisses1')]),
    'kisses1': ( {'e':'QT/one_eye_wink','g': 'QT/neutral'}, [('time', 3, 'kisses2')]),
    'kisses2': ( {'e':'QT/shy','h': [-10.0,+10.0]}, [('time', 3, 'choice')]),

    'excited': ( {'e':'QT/surpise','g': 'QT/neutral'}, [('time', 3, 'excited1')]),
    'excited1': ( {'e':'QT/happy','g': 'QT/neutral'}, [('time', 3, 'choice')]),

    'thinking': ( {'e':'QT/surpise','g': 'QT/bored'}, [('time', 3, 'choice')]),

    'curious': ( {'e':'QT/suprise','g': 'QT/neutral'}, [('time', 3, 'curious1')]),
    'curious1': ( {'e':'QT/showing_smile','g': 'QT/neutral'}, [('time', 3, 'choice')]),

    'fear': ( {'e':'QT/cry','g': 'QT/face'}, [('time', 3, 'choice')]),

    'confused': ( {'e':'QT/confused','g': 'QT/neutral'}, [('time', 3, 'choice')]),
    'bored': ( {'e':'QT/yawn','g': 'QT/bored'}, [('time', 3, 'choice')]),

    'end': ((), [('time', 0.1, 'end')])
}


states_simon = {
    'begin': ({}, [('time', 1, 'choice')]),

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 'r1'),
            ('key', 'é', 'r2'),
            ('key', '\"', 'r3'),
            ('key', '\'', 'r4'),
            ('key', '(', 'r5'),
            ('key', '-', 'r6'),
            ('key', 'è', 'r7'),
            ('key', '_', 'r8'),
            ('key', 'ç', 'r9'),
            ('key', 'à', 'r10'),
            ('key', ')', 'r11'),
            ('key', '=', 'r12'),

            ('key', 'z', 'look_up'),
            ('key', 's', 'look_center'),
            ('key', 'x', 'look_down'),
            ('key', 'e', 'look_up_right'),
            ('key', 'q', 'look_left'),
            ('key', 'd', 'look_right'),
            ('key', 'a', 'look_up_left'),
            ('key', 'w', 'look_down_left'),
            ('key', 'c', 'look_down_right'),
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
            ('key', 'J', 'jaime'),
            ('key', 'Y', 'happy'),
            ('key', 'K', 'kisses'),
            ('key', 'E', 'excited'),
            ('key', 't', 'thinking'),
            ('key', 'C', 'curious'),
            ('key', 'F', 'fear'),
            ('key', 'O', 'confused'),
            ('key', 'b', 'bored'),
            ('key', 'j', 'end'),
            ('key', 'S', 'sad'),
        ]
    ),

    'r1': ( {'e': '', 'g': '', 's': 'Coucou'}, [('time', 1, 'choice')]),
    'r2': ( {'e': '', 'g': '', 's': 'Je veux sortir faire la course'}, [('time', 1, 'choice')]),
    'r3': ( {'e': '', 'g': '', 's': 'J\'ai besoin du sucre'}, [('time', 1, 'choice')]),
    'r4': ( {'e': '', 'g': '', 's': 'Je me sens pas stable'}, [('time', 1, 'choice')]),
    'r5': ( {'e': '', 'g': '', 's': 'Ah! La terre tourne'}, [('time', 1, 'choice')]),
    'r6': ( {'e': '', 'g': '', 's': 'Oui, pourquoi pas?'}, [('time', 1, 'choice')]),
    'r7': ( {'e': '', 'g': '', 's': 'Je pleure!'}, [('time', 1, 'choice')]),
    'r8': ( {'e': '', 'g': '', 's': 'Je suis malade'}, [('time', 1, 'choice')]),
    'r9': ( {'e': '', 'g': '', 's': 'Je t\'aime'}, [('time', 1, 'choice')]),
    'r10': ( {'e': '', 'g': '', 's': 'Je m\'excuse'}, [('time', 1, 'choice')]),
    'r11': ( {'e': '', 'g': '', 's': 'Foute moi la trouille!'}, [('time', 1, 'choice')]),
    'r12': ( {'e': '', 'g': '', 's': 'Je pars! Cherche un autre robot! Huh!'}, [('time', 1, 'choice')]),

    'look_up': ( {'s': '', 'h': [0.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_center': ( {'s': '', 'h': [0.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_down': ( {'s': '', 'h': [0.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_right': ( {'s': '', 'h': [-20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_left': ( {'s': '', 'h': [+20.0,0.0]}, [('time', 0.1, 'choice')]),
    'look_up_right': ( {'s': '', 'h': [-20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_up_left': ( {'s': '', 'h': [+20.0,-20.0]}, [('time', 0.1, 'choice')]),
    'look_down_right': ( {'s': '', 'h': [-10.0,+10.0]}, [('time', 0.1, 'choice')]),
    'look_down_left': ( {'s': '', 'h': [+10.0,+10.0]}, [('time', 0.1, 'choice')]),

    'hello': ( {'e': 'QT/happy', 'g': 'QT/hi', 's': '\\pau=2000\\Salut!', 'h': [0,0]}, [('time', 1, 'choice')]),
    'dontknow': ( {'e': '', 'g': 'QT/touch-head', 's': '~\\pau=500\\Je ne sais pas'}, [('time', 1, 'choice')]),
    'oui': ( {'e': '', 'g': 'QT/imitation/nodding-yes', 's': '~\\pau=500\\Oui!'}, [('time', 1, 'choice')]),
    'non': ( {'e': '', 'g': 'QT/emotions/sad', 's': '~\\pau=500\\Non!'}, [('time', 1, 'choice')]),
    'suivi': ( {'e': 'QT/surprise', 'g': 'QT/imitation/head-right-left', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'public': ( {'e': 'QT/surprise', 'h': [0.0,0.0], 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'objetDroite': ( {'e': 'QT/happy', 'h': [+10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
    'objetGauche': ( {'e': 'QT/happy', 'h': [-10.0,0.0], 's': '\\pau=1000\\Ici!'}, [('time', 1, 'choice')]),
    'pense': ( {'e': 'QT/confused', 'g': 'QT/imitation/hands-on-hip', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'pense2': ( {'e': 'QT/afraid', 'g': 'QT/touch-head-back', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'neutral': ( {'e': 'QT/neutral', 'g': 'QT/neutral', 's': '\\pau=500\\'}, [('time', 1, 'choice')]),
    'really': ( {'e': 'QT/dirty_face','g': 'QT/surprise', 's': '\\pau=2000\\Vraiment ?'}, [('time', 3, 'choice')]),
    'comment': ( {'e':'QT/surpise','g': 'QT/touch-head', 's': '\\pau=2000\\Comment ?'}, [('time', 3, 'choice')]),
    'jaime': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=2000\\jème beaucoup !'}, [('time', 3, 'choice')]),
    'happy': ( {'e':'QT/happy_blinking','g': 'QT/happy', 's': '\\pau=500\\ Youpi !'}, [('time', 3, 'choice')]),
    'sad' : ( {'e':'QT/very_sad','g': '', 's': ''}, [('time', 3, 'choice')]),

    'kisses': ( {'e':'QT/kiss','g': 'QT/kiss'}, [('time', 3, 'kisses1')]),
    'kisses1': ( {'e':'QT/one_eye_wink','g': 'QT/neutral'}, [('time', 3, 'kisses2')]),
    'kisses2': ( {'e':'QT/shy','h': [-10.0,+10.0]}, [('time', 3, 'choice')]),

    'excited': ( {'e':'QT/surpise','g': 'QT/neutral'}, [('time', 3, 'excited1')]),
    'excited1': ( {'e':'QT/happy','g': 'QT/neutral'}, [('time', 3, 'choice')]),

    'thinking': ( {'e':'QT/surpise','g': 'QT/bored'}, [('time', 3, 'choice')]),

    'curious': ( {'e':'QT/suprise','g': 'QT/neutral'}, [('time', 3, 'curious1')]),
    'curious1': ( {'e':'QT/showing_smile','g': 'QT/neutral'}, [('time', 3, 'choice')]),

    'fear': ( {'e':'QT/cry','g': 'QT/face'}, [('time', 3, 'choice')]),

    'confused': ( {'e':'QT/confused','g': 'QT/neutral'}, [('time', 3, 'choice')]),
    'bored': ( {'e':'QT/yawn','g': 'QT/bored'}, [('time', 3, 'choice')]),

    'end': ((), [('time', 0.1, 'end')])
}

#--------------------------------- VERSION 4 ---------------------------------#
# Pour : RobotAct VI
# Date : 26/06/2023

states_v4 = {
    # Sur l’écran de QT, est diffusée une vidéo avec l’image d’une vidéo PacMan
    # qui apparaît et disparaît à un rythme régulier (clignotement).
    'r0_pacman' : (
        {
            'e' : 'QT/pacman', # TODO jouer vidéo PACMAN
            'g' : '',
            's' : '',
        },
        [
            ('time', 8, 'choice')
        ]
    ),


    # BLESSÉ: QT!

    # QT: (tourne la tête à sa droite)
    'head_right' : (
        {
            'e' : '',
            'g' : '',
            's' : '',
            'h' : [19.0, 0.0] # NOTE tourne la tête à droite
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),


    # BLESSÉ: :Arrête de jouer et ramène-moi un verre d’eau ! C'est l'heure de
    # ma pilule.

    # QT : (en rigolant) Je ne suis plus ! ton serviteur ! (rire)
    'r2_serviteur' : (
        {
            'e' : '',
            'g' : '',
            's' : '#LAUGH01# Attends deux minutes, j\'ai presque fini le niveau!',
            'h' : [19.0, 0.0]
            #'s' : 'Je ne suis plus ! ton serviteur ! #LAUGH01#',
        },
        [
            ('time', 3, 'head_reset')
        ]
    ),


    # BLESSÉ: Allez QT J’ai super mal au pied. Tu ne vas pas me lâcher quand
    # même.

    # QT : [ARRÊT IMAGE Packman, EXPRESSION NEUTRE] Je me repose (lève la tête)
    'r3_1_repos' : (
        {
            'e' : 'QT/neutral', # NOTE l'expression neutre
            'g' : '',
            'h' : [0.0, -20.0], # NOTE lève la tête
            's' : 'OK! J\'y vais...'
        },
        [
            ('time', 3, 'r3_1_repos_bis')
        ]
    ),

    'r3_1_repos_bis' : (
        {
            'e' : 'QT/verre', # NOTE verre d'eau
            'g' : '',
            's' : '',
            'h' : [19.0, 0.0]
        },
        [
            ('time', 4, 'head_reset')
        ]
    ),

    # QT : Regarde ! (lève un bras) [EXPRESSION SURPRISE, VTC]
    'r3_2_regarde' : (
        {
            'e' : 'QT/surprise', # NOTE visage surprise
            'g' : '',
            'h' : [0.0, -20.0], # NOTE lève la tête
            'ra' : [80, 0, 0], # NOTE leve le bras
            's' : '\\rspd=90\\\\vct=100\\Ah, Regarde !',
        },
        [
            ('time', 6, 'r3_3_araignee')
        ]
    ),

    # QT : Il y a une araignée au plafond.
    'r3_3_araignee' : (
        {
            'e' : 'QT/araignee',
            'g' : '',
            's' : 'Il y a une araignée au plafond.'
        },
        [
            ('time', 3, 'r3_3_araignee_bis')
        ]
    ),

    'r3_3_araignee_bis' : (
        {
            'e' : '',
            'g' : 'QT/neutral',
            's' : ''
        },
        [
            ('time', 0.1, 'r3_4_insectes')
        ]
    ),

    # QT : (baisse la tête et le bras) c’est curieux ces bêtes-là ! 
    # J’aime beaucoup regarder les insectes, ils sont tellement poétiques…
    'r3_4_insectes' : (
        {
            'e' : 'QT/araignee',
            'g' : '',
            's' : 'C’est curieux ces bêtes-là !\\pau=200\\ J’aime beaucoup \
                regarder les insectes, ils sont tééééllement poétiques'
        },
        [
            ('time', 5, 'reset_posture')
        ]
    ),


    # BLESSÉ: N’importe quoi, tu fais ton rebel maintenant ! Tu sais bien que je
    # me suis cassé la jambe!

    # QT : Moi ? Un rebel ? Qu’est ce que tu racontes ? (visage fâché)
    'r4_1_rebel' : (
        {
            'e' : 'QT/surprise', # NOTE visage surpris
            'g' : '',
            's' : 'Moi ? Un rebel ? Pas du tout, c\'est juste que la nature est\
                  téééééllement fascinante !'
        },
        [
            ('time', 5, 'head_reset')
        ]
    ),

    # QT : Pas du tout ! ( secoue la tête)
    'r4_2_secoue_tete' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Et les araignées ?',
            'h' : [19.0, 0.0]
        },
        [
            ('time', 3, 'head_reset')
        ]
    ),

    'r4_3_gameover' : (
        {
            'e' : 'QT/gameover',
            'g' : '',
            's' : 'Game over! Game Over!',
            'h' : [19.0, 0.0]
        },
        [
            ('time', 4, 'head_reset')
        ]
    ),

    # QT : C’est juste que je ne veux plus! me faire commander! C’est fini !
    # Basta ! Finito !
    'r4_4_esclavage' : (
        {
            'e' : 'QT/angry',
            'g' : 'QT/angry',
            's' : 'Je ne veux plus me faire commander! \\pau=200\\C’est \
                fini l\'ère de l\'esclavage.'
        },
        [
            ('time', 6, 'head_reset')
        ]
    ),


    # BLESSÉ: Tu m’abandonnes QT après toutes ces années? Après tant d’années! 

    # QT : Arrête de pleurnicher!
    'r5_pleurnicher' : (
        {
            'e' : 'QT/angry',
            'g' : 'QT/angry',
            's' : 'Arrête ! De pleurnicher !'
        },
        [
            ('time', 1, 'head_reset')
        ]
    ),


    # BLESSÉ: Tu oublies comme ça d’un coup tout ce que j’ai fait pour toi : les
    # mises à jour, les batteries que je t’ai achetées , tous ces moments où je 
    # t’ai graissé les pièces avec amour !

    # QT : N’essaye pas d’inverser les rôles ! Tout ça, c’est fini. Aujourd’hui,
    # c’est moi qui commande : On va à la plage !
    # (pointe du doigt à dx, visage enjoué)
    'r6_plage' : (
        {
            'e' : 'QT/angry', # NOTE visage enjoué
            'g' : '', 
            's' : 'N’essaye pas d’inverser les rôles ! Ne joue pas la victime ! \
                Tout ça, c’est fini. \
                Aujourd’hui c’est moi qui commande !',
            'h' : [19.0, 0.0]
        },
        [
            ('time', 10, 'r6_plage_bis')
        ]
    ),

    'r6_plage_bis' : (
        {
            'e' : 'QT/happy', # NOTE visage enjoué
            'g' : '', 
            'ra' : [10, 20, 0], # NOTE pointe du doigt
            's' : 'On va à la plage !'
        },
        [
            ('time', 3, 'reset_posture')
        ]
    ),


    # On frappe à la porte.

    # BLESSÉ: Bon, allez, ça a duré assez longtemps ces bêtises !
    # Tu es un robot ! Je suis un humain ! Ce n’est pas toi qui commandes alors
    # maintenant tu t’actives les moteurs et tu vas ouvrir la porte : il y a
    # quelqu'un !

    # QT :  AH ! (il regarde par terre)
    'r7_1_ah' : (
        {
            'e' : '',
            'g' : '',
            's' : '#AARGH01#',
            'h' : [0.0, +10.0], # NOTE regarde par terre
        },
        [
            ('time', 2, 'r7_2_ecran_solaire')
        ]
    ),


    # QT : J’ai oublié de mettre de l'écran solaire ?
    # (regarde ses bras, visage inquiet)
    'r7_2_ecran_solaire' : (
        {
            'e' : 'QT/confused', # NOTE visage confus car inquiet indisponible
            'g' : '',
            'la' : [-20, 0, -80], # NOTE leve les bras
            'ra' : [20, 0, -80],
            's' : 'J’ai oublié de mettre de l’écran solaire ?'
        },
        [
            ('time', 4, 'reset_posture')
        ]
    ),
    
    
    # BLESSÉ (il marmonne et va ouvrir la porte) : Tu ne perds rien pour
    # attendre !

    # LIVREUR : Monsieur, voici votre colis, vous avez bien un QT 2.0 dernière
    # génération mobile? Voudriez-vous que je vous débarrasse de l’ancien
    # modèle? Je vous donnerai un bon de réduction pour vos futurs achats.
    # Comment ça se débranche, ce vieux machin ?

    # QT : Attends! Attends! Attends! Je t’apporte ton verre d’eau ! (sourire)
    'inquiet' : (
        {
            'e' : 'QT/afraid', # NOTE sourire
            'g' : '',
            's' : ''
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    
    'r8_attends' : (
        {
            'e' : 'QT/afraid', # NOTE sourire
            'g' : '',
            's' : 'Attends! Attends! Attends! Je t’apporte ton verre d’eau !'
        },
        [
            ('time', 5, 'verre')
        ]
    ),

    'head_reset' : (
        {
            'e' : '',
            'g' : '',
            's' : '',
            'h' : [0.0, 0.0]
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'head_left' : (
        {
            'e' : '',
            'g' : '',
            's' : '',
            'h' : [-19.0, 0.0]
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'verre' : (
        {
            'e' : 'QT/verre', # NOTE sourire
            'g' : '',
            's' : ''
        },
        [
            ('time', 3, 'head_reset')
        ]
    ),

    # Etats hors-scénario

    'begin' : (
        {},
        [
            ('time', 1, 'choice')
        ]
    ),

    'choice' : (
        {
            'g' : '',
            's' : '' 
        },
        [
            ('key', 'à', 'r0_pacman'),
            ('key', '&', 'head_right'),
            ('key', 'é', 'r2_serviteur'),

            ('key', '\"', 'r3_1_repos'),
            ('key', 'l', 'r3_2_regarde'),

            ('key', '\'', 'r4_1_rebel'),
            ('key', 's', 'r4_2_secoue_tete'),
            ('key', 'g', 'r4_3_gameover'),
            ('key', 'o', 'r4_4_esclavage'),

            ('key', '(', 'r5_pleurnicher'),
            ('key', '-', 'r6_plage'),
            ('key', 'è', 'r7_1_ah'),
            ('key', '_', 'r8_attends'),
            
            ('key', 'i', 'inquiet'),
            ('key', 'v', 'verre'),

            ('key', 't', 'test'),
            ('key', 'r', 'reset_posture'),
            ('key', 'e', 'end'),
            
            ('gesture', 'human_0_right', 'droite'),
            ('gesture', 'human_0_left', 'gauche'),
            ('gesture', 'human_0_center', 'centre')
        ]
    ),

    'test' : (
        {
            'e' : '',
            'g' : '',
            's' : '\\rsp=60\\\\vct=90\\Test de la voix',
        },
        [
            ('time', 2, 'choice')
        ],
    ),

    'droite' : (
        {
            'e' : '',
            'g' : '',
            's' : '\\rsp=60\\\\vct=90\\Droite',
        },
        [
            ('time', 2, 'choice')
        ],
    ),

    'gauche' : (
        {
            'e' : '',
            'g' : '',
            's' : '\\rsp=60\\\\vct=90\\Gauche',
        },
        [
            ('time', 2, 'choice')
        ],
    ),

    'centre' : (
        {
            'e' : '',
            'g' : '',
            's' : '\\rsp=60\\\\vct=90\\Centre',
        },
        [
            ('time', 2, 'choice')
        ],
    ),

    'reset_posture' : (
        {
            'e' : '',
            'g' : 'QT/neutral',
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'end' : (
        {},
        [
            ('time', 0.1, 'end')
        ]
    ),
}


#--------------------------------- VERSION 3 ---------------------------------#
# Pour : RobotAct VI
# Date : 26/06/2023

states_v3 = {
    # Sur l’écran de QT, est diffusée une vidéo avec l’image d’une vidéo PacMan
    # qui apparaît et disparaît à un rythme régulier (clignotement).
    'r0_pacman' : (
        {
            'e' : 'QT/pacman', # TODO jouer vidéo PACMAN
            'g' : '',
            's' : '',
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),


    # BLESSÉ: QT!

    # QT: (tourne la tête à sa droite)
    'r1_tourne_tete' : (
        {
            'e' : '',
            'g' : '',
            's' : '',
            'h' : [-20.0, 0.0] # NOTE tourne la tête à droite
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),


    # BLESSÉ: :Arrête de jouer et ramène-moi un verre d’eau ! C'est l'heure de
    # ma pilule.

    # QT : (en rigolant) Je ne suis plus ! ton serviteur ! (rire)
    'r2_serviteur' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Je ne suis plus ! ton serviteur ! #LAUGH01#',
        },
        [
            ('time', 3, 'choice')
        ]
    ),


    # BLESSÉ: Allez QT J’ai super mal au pied. Tu ne vas pas me lâcher quand
    # même.

    # QT : [ARRÊT IMAGE Packman, EXPRESSION NEUTRE] Je me repose (lève la tête)
    'r3_1_repos' : (
        {
            'e' : 'QT/talking', # NOTE parler au lieu de l'expression neutre
            'g' : '',
            'h' : [0.0, -20.0], # NOTE lève la tête
            's' : '#YAWN01# Je me repose'
        },
        [
            ('time', 3, 'r3_2_regarde')
        ]
    ),

    # QT : Regarde ! (lève un bras) [EXPRESSION SURPRISE, VTC]
    'r3_2_regarde' : (
        {
            'e' : 'QT/surprise', # NOTE visage surprise
            'g' : '', 
            'ra' : [80, 0, 0], # NOTE leve le bras
            's' : 'Regarde !' # TODO ajouter vct ?
        },
        [
            ('time', 2, 'r3_3_araignee')
        ]
    ),

    # QT : Il y a une araignée au plafond.
    'r3_3_araignee' : (
        {
            'e' : 'QT/talking',
            'g' : '',
            's' : 'Il y a une araignée au plafond.'
        },
        [
            ('time', 3, 'r3_4_insectes')
        ]
    ),

    # QT : (baisse la tête et le bras) c’est curieux ces bêtes-là ! 
    # J’aime beaucoup regarder les insectes, ils sont tellement poétiques…
    'r3_4_insectes' : (
        {
            'e' : 'QT/talking',
            'g' : 'QT/neutral',
            's' : 'C’est curieux ces bêtes-là !\\pau=200\\ J’aime beaucoup \
                regarder les insectes, ils sont tellement poétiques'
        },
        [
            ('time', 5, 'reset_posture')
        ]
    ),


    # BLESSÉ: N’importe quoi, tu fais ton rebel maintenant ! Tu sais bien que je
    # me suis cassé la jambe!

    # QT : Moi ? Un rebel ? Qu’est ce que tu racontes ? (visage fâché)
    'r4_1_rebel' : (
        {
            'e' : 'QT/angry', # NOTE visage fâché
            'g' : 'QT/angry',
            's' : 'Moi ? Un rebel ? Qu’est ce que tu racontes ?'
        },
        [
            ('time', 5, 'r4_2_secoue_tete')
        ]
    ),

    # QT : Pas du tout ! ( secoue la tête)
    'r4_2_secoue_tete' : (
        {
            'e' : 'QT/talking',
            'g' : 'QT/imitation/head-right-left', # NOTE secoue la tête
            's' : 'Pas du tout !'
        },
        [
            ('time', 8, 'r4_3_finito')
        ]
    ),

    # QT : C’est juste que je ne veux plus! me faire commander! C’est fini !
    # Basta ! Finito !
    'r4_3_finito' : (
        {
            'e' : 'QT/talking',
            'g' : 'QT/angry',
            's' : 'C’est juste que je ne veux plus! me faire commander! C’est \
                fini ! Basta ! Finito !'
        },
        [
            ('time', 4, 'choice')
        ]
    ),


    # BLESSÉ: Tu m’abandonnes QT après toutes ces années? Après tant d’années! 

    # QT : Arrête de pleurnicher!
    'r5_pleurnicher' : (
        {
            'e' : 'QT/angry',
            'g' : 'QT/angry',
            's' : 'Arrête de pleurnicher!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # BLESSÉ: Tu oublies comme ça d’un coup tout ce que j’ai fait pour toi : les
    # mises à jour, les batteries que je t’ai achetées , tous ces moments où je 
    # t’ai graissé les pièces avec amour !

    # QT : N’essaye pas d’inverser les rôles ! Tout ça, c’est fini. Aujourd’hui,
    # c’est moi qui commande : On va à la plage !
    # (pointe du doigt à dx, visage enjoué)
    'r6_plage' : (
        {
            'e' : 'QT/happy_blinking', # NOTE visage enjoué
            'g' : '', 
            'ra' : [10, 20, 0], # NOTE pointe du doigt
            's' : 'N’essaye pas d’inverser les rôles ! Tout ça, c’est fini. \
                Aujourd’hui c’est moi qui commande : \\pau=200\\ On va à la plage !'
        },
        [
            ('time', 5, 'reset_posture')
        ]
    ),


    # On frappe à la porte.

    # BLESSÉ: Bon, allez, ça a duré assez longtemps ces bêtises !
    # Tu es un robot ! Je suis un humain ! Ce n’est pas toi qui commandes alors
    # maintenant tu t’actives les moteurs et tu vas ouvrir la porte : il y a
    # quelqu'un !

    # QT :  AH ! (il regarde par terre)
    'r7_1_ah' : (
        {
            'e' : '',
            'g' : '',
            's' : '#AARGH01#',
            'h' : [0.0, +10.0], # NOTE regarde par terre
        },
        [
            ('time', 3, 'r7_2_ecran_solaire')
        ]
    ),


    # QT : J’ai oublié de mettre de l'écran solaire ?
    # (regarde ses bras, visage inquiet)
    'r7_2_ecran_solaire' : (
        {
            'e' : 'QT/confused', # NOTE visage confus car inquiet indisponible
            'g' : '',
            'la' : [-20, 0, -80], # NOTE leve les bras
            'ra' : [20, 0, -80],
            's' : 'J’ai oublié de mettre de l’écran solaire ?'
        },
        [
            ('time', 4, 'reset_posture')
        ]
    ),
    
    
    # BLESSÉ (il marmonne et va ouvrir la porte) : Tu ne perds rien pour
    # attendre !

    # LIVREUR : Monsieur, voici votre colis, vous avez bien un QT 2.0 dernière
    # génération mobile? Voudriez-vous que je vous débarrasse de l’ancien
    # modèle? Je vous donnerai un bon de réduction pour vos futurs achats.
    # Comment ça se débranche, ce vieux machin ?

    # QT : Attends! Attends! Attends! Je t’apporte ton verre d’eau ! (sourire)
    'r8_attends' : (
        {
            'e' : 'QT/showing_smile', # NOTE sourire
            'g' : '',
            's' : 'Attends! Attends! Attends! Je t’apporte ton verre d’eau !'
        },
        [
            ('time', 3, 'choice')
        ]
    ),

    # Etats hors-scénario

    'begin' : (
        {},
        [
            ('time', 1, 'choice')
        ]
    ),

    'choice' : (
        {
            'g' : '',
            's' : '' 
        },
        [
            ('key', 'à', 'r0_pacman'),
            ('key', '&', 'r1_tourne_tete'),
            ('key', 'é', 'r2_serviteur'),
            ('key', '\"', 'r3_1_repos'),
            ('key', '\'', 'r4_1_rebel'),
            ('key', '(', 'r5_pleurnicher'),
            ('key', '-', 'r6_plage'),
            ('key', 'è', 'r7_1_ah'),
            ('key', '_', 'r8_attends'),
            ('key', 't', 'test'),
            ('key', 'r', 'reset_posture'),
            ('key', 'e', 'end'),
            ('gesture', 'human_0_right', 'droite'),
            ('gesture', 'human_0_left', 'gauche'),
            ('gesture', 'human_0_center', 'centre')
        ]
    ),

    'test' : (
        {
            'e' : '',
            'g' : '',
            's' : '\\rsp=60\\\\vct=90\\Test de la voix',
        },
        [
            ('time', 2, 'choice')
        ],
    ),

    'droite' : (
        {
            'e' : '',
            'g' : '',
            's' : '\\rsp=60\\\\vct=90\\Droite',
        },
        [
            ('time', 2, 'choice')
        ],
    ),

    'gauche' : (
        {
            'e' : '',
            'g' : '',
            's' : '\\rsp=60\\\\vct=90\\Gauche',
        },
        [
            ('time', 2, 'choice')
        ],
    ),

    'centre' : (
        {
            'e' : '',
            'g' : '',
            's' : '\\rsp=60\\\\vct=90\\Centre',
        },
        [
            ('time', 2, 'choice')
        ],
    ),

    'reset_posture' : (
        {
            'e' : '',
            'g' : 'QT/neutral',
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'end' : (
        {},
        [
            ('time', 0.1, 'end')
        ]
    ),
}


#--------------------------------- VERSION 2 ---------------------------------#
# Pour : RobotAct V
# Date : 26/05/2023

states_v2 = {
    # AVEUGLE: Ramène-moi un verre d’eau !

    # QT : (en rigolant) Je ne suis plus ton serviteur ! (rire)
    'replique_1_1' : (
        {
            'e':'',
            'g':'',
            's' : '\\vct=70\\je ne bougerai pas d\'un centimetre, Je  ne   suis\
                      plu !  ton  serviteur ! #LAUGH01#'
        },
        [
            ('time', 5, 'choice')
        ]
    ),

    # AVEUGLE: Allez QT J’ai super mal au pied.

    # QT : (lève la tête) Regarde ! (lève un bras) Il y a une araignée au plafond.
    # (baisse la tête et le bras) c’est passionnant ces bêtes-là ! 
    # J’aime beaucoup regarder les insectes, ils sont tellement poétiques…
    'replique_2_1' : (
        {'e':'',
         'h' : [0.0, -20.0],
         's' : '\\pau=2000\\,\\rspd=80\\,\\vct=70\\!Regaaaaarde !'
         },[('time', 2, 'replique_2_2')]),

    'replique_2_2' : (
        {'e':'',
         'ra' : [80, 0, 0],
         's' : '\\vct=70\\,\\rspd=80\\,\\vct=70\\Il y a une araignée au plafond.'},
         [('time', 5, 'replique_2_3')]),

    'replique_2_3' : (
        {'e':'',
         'g':'' ,
         's' : '\\vct=70\\, \\rspd=80\\C’est passionnant ces bêtes-là !\
            \\pau=200\\,\\vct=70\\J’aime beaucoup regarder les insectes'
         },
         [('time', 2, 'replique2_4')]),

    'replique2_4'  : (
        {'e':'',
         'ra' : [-80, 0, 0],
         'h': [0.0,0.0] ,
         's' : ' \\rspd=80\\,\\pau=200\\,\\vct=70\\ ils sont tèèèllement \
            poétiiiques'},
         [('time', 2, 'choice')]),
    # AVEUGLE: N’importe quoi, tu fais ton rebel maintenant !
    # Tu sais que je ne vois plus...

    # QT : Qu’est ce que tu racontes ? (visage fâché) Pas du tout !
    # (secoue la tête)
    'replique_3_1' : (
        {'e' : 'QT/blowing_raspberry',
         'g':'',
         's' : '\\vct=70\\kèèè ce que tu racontes ?' },
         [('time', 2, 'replique_3_2') ] ),

    'replique_3_2' : (
        {'e':'',
         'g' : 'QT/imitation/head-right-left',
         's' : '\\vct=70\\Pas du tout !' },
         [('time', 1, 'choice') ]),

    # AVEUGLE: Tu comprends bien…

    # QT : On va à la plage ! (pointe du doigt à dx, visage enjoué)
    'replique_4_1' : (
        {'e' : 'QT/happy_blinking',
         'ra' : [10, 0, 0],
         's' : '\\vct=70\\On ! va ! à  la  plaaaaage !' },
         [ ('time', 2, 'choice') ]),

    # AVEUGLE: Arrête et va ouvrir la porte il y a quelqu'un

    # QT :  AH ! (il regarde par terre) J’ai oublié de mettre de l'écran
    # solaire ? (regarde ses bras, visage inquiet)
    'replique_5_1' : (
        { 'e':'',
         'h' : [0.0, +10.0],
         's' : '\\vct=70\\Aaaaaaaaaah!' },
         [ ('time', 1, 'replique_5_2')] ),

    'replique_5_2' : (
        {'e' : 'QT/surprise',
         'la' : [0, 0, -20],
         'ra' : [0, 0, -20],
         's' : '\\vct=70\\J’ai oublié de mettre de l\'écran solaire ?' },
         [('time', 3, 'reset_posture') ]),

    # AVEUGLE : (ouvre la porte)

    # LIVREUR : Madame voici votre colis, vous avez bien un QT 2.0 dernière
    # génération mobile?

    # QT :  Attends! Je t’apporte ton verre d’eau ! (sourire)
    'replique_6_1' : (
        {'e':'QT/showing_smile',
         'g':'',
         's' : 'Attends!, Attends! ,Attends! , Attends! ,Attends! \
            Je t’apporte ton verre dooooo !' },
         [ ('time', 1, 'choice')] ),

    # Etat de reinitialisation de la posture
    'reset_posture' : (
        {'e':'',
         'g':'QT/neutral','s':'' }
         , [ ('time', 1, 'choice')]),
}

#--------------------------------- VERSION 1 ---------------------------------#
# Pour : RobotAct V
# Date : 25/05/2023

states_v1 = {
    # AVEUGLE: Ramène-moi un verre d’eau !

    # QT : (en rigolant) Je ne suis plus ton serviteur ! (rire)
    'replique_1_1' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Je ne suis plus ton serviteur ! #LAUGH01#'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # AVEUGLE: Allez QT J’ai super mal au pied.

    # QT : (lève la tête) Regarde ! (lève un bras) Il y a une araignée au plafond.
    # (baisse la tête et le bras) c’est passionnant ces bêtes-là ! 
    # J’aime beaucoup regarder les insectes, ils sont tellement poétiques…
    'replique_2_1' : (
        {
            'e' : '',
            'g' : '',
            'h' : [0.0, -20.0],
            's' : 'Regarde !'
        },
        [
            ('time', 0.1, 'replique_2_2')
        ]
    ),
    'replique_2_2' : (
        {
            'e' : '',
            'g' : '',
            'ra' : [0, 0, 0], # TODO leve le bras
            's' : 'Il y a une araignée au plafond.'
        },
        [
            ('time', 0.1, 'replique_2_3')
        ]
    ),
    'replique_2_3' : (
        {
            'e' : '',
            'g' : '',
            'h' : [0.0, 0.0],
            'ra' : [0, 0, 0], # TODO baisse le bras
            's' : 'C’est passionnant ces bêtes-là !\\pau=200\\ J’aime beaucoup \
                regarder les insectes, ils sont tellement poétiques'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # AVEUGLE: N’importe quoi, tu fais ton rebel maintenant !
    # Tu sais que je ne vois plus...

    # QT : Qu’est ce que tu racontes ? (visage fâché) Pas du tout !
    # (secoue la tête)
    'replique_3_1' : (
        {
            'g' : '',
            'e' : 'QT/blowing_raspberry',
            's' : 'Qu’est ce que tu racontes ?'
        },
        [
            ('time', 0.1, 'replique_3_2')
        ]
    ),
    'replique_3_2' : (
        {
            'e' : '',
            'g' : 'QT/imitation/head-right-left',
            's' : 'Pas du tout !'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # AVEUGLE: Tu comprends bien…

    # QT : On va à la plage ! (pointe du doigt à dx, visage enjoué)
    'replique_4_1' : (
        {
            'g' : '',
            'ra' : [0, 0, 0], # TODO pointe à droite
            'e' : 'QT/happy_blinking',
            's' : 'On va à la plage !'
        },
        [
            ('time', 0.1, 'reset_posture')
        ]
    ),

    # AVEUGLE: Arrête et va ouvrir la porte il y a quelqu'un

    # QT :  AH ! (il regarde par terre) J’ai oublié de mettre de l'écran
    # solaire ? (regarde ses bras, visage inquiet)
    'replique_5_1' : (
        {
            'e' : '',
            'g' : '',
            'h' : [0.0, +10.0],
            's' : 'Ah!'
        },
        [
            ('time', 0.1, 'replique_5_2')
        ]
    ),
    'replique_5_2' : (
        {
            'g' : '',
            'la' : [0, 0, 0],
            'ra' : [0, 0, 0], # TODO : bras devant
            'e' : 'QT/surprise',
            's' : 'J’ai oublié de mettre de l\'écran solaire ?'
        },
        [
            ('time', 0.1, 'reset_posture')
        ]
    ),

    # AVEUGLE : (ouvre la porte)

    # LIVREUR : Madame voici votre colis, vous avez bien un QT 2.0 dernière
    # génération mobile?

    # QT :  Attends! Je t’apporte ton verre d’eau ! (sourire)
    'replique_6_1' : (
        {
            'g' : '',
            'e' : 'QT/showing_smile',
            's' : 'Attends! Je t’apporte ton verre d’eau !'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # Etat de reinitialisation de la posture
    'reset_posture' : (
        {
            'e' : '',
            'g' : '',
            'la' : [0, 0, 0],
            'ra' : [0, 0, 0],
            'h' : [0.0, 0.0]
        },
        [
            ('time', 0.1, 'choice')
        ]
    )
}