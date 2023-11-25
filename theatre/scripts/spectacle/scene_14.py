######################################################## SCENE 14 ######################################################


'''
→ SCÈNE 14 : séquence de l’audition de Nao avec Andrea. A la sortie de Nao, moment plus choral et documentaire sur les difficultés des acteurs à  travailler avec les  robots. Andrea commencent puis les autres acteurs entrent [1er partie scène déjà existante, 2ème partie à travailler en impro. A répéter 1er semaine]
'''

# L’audition

# Personnages
# NAO : robot
# AGENT (humain·e): acteur/actrice humain.e

# Indication au magicien d’oz : les paroles de l’agent entre parenthèses sont 
# seulement des ressources pour l’improvisation, il ne faut pas l'atteindre
# pour déclencher l’action suivante.

# NOTE

#! TAGS
#! pitch: vct 50-200 (100)
#! rate: rspd 50-200 (100)
#! pause: pau *
#! volume: vol 0-100 (80)


#? Allume la lumierre

#? PREDRAG : Excusez moi, je pense qu'il faut se calmer là.

#? PREDRAG : C'est moi qui a programme les robots.

states = {
    #? Nao entre sur scène et marche quelques mètres depuis cour vers jardin.
    # L’agent arrive et lui court après.

    # AGENT : Nao ! Nao ! Nao !

    #? Nao s’arrête et se tourne derrière lui vers l’agent.

    # AGENT : Je te cherchais ! Tu sais que c’est le grand jour aujourd’hui ! 

    # NAO : Yessssss !
    #? [&](1)
    'r_yes': (
        {
            'g': 'oui',
            's': '\\rspd=50\\yes!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT : C’est l’occasion de ta vie ! Tout va se jouer aujourd’hui !

    #? [z] leve la tete
    #? [é](2)
    # NAO  : Tu m’as trouvé une faaaaamme ? J’en étais sûr !
    # (Excitation/il lève la tête/ il fait des mouvements de bras comme lever
    # les bras (YEAH))
    'r_femme': (
        {
            'g': 'excited',
            's': 'Have you found a \\rspd=50\\woman\\rspd=100\\ for me ? I was sure you would !'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT : Mais non…(Mais non Nao, nous en avons déjà parlé, tu es un robot…)
 
    #? ["](3)
    # NAO: Je sais ! Tu m’as acheté une nouvelle batterie !
    # (Excitation/ mouvement vibration/pliement du corps)
    # (Très vite il répète :)
    # Une nouvelle batterie ! Une nouvelle batterie! Une nouvelle batterie !
    'r_batterie': (
        {
            'g': 'excited',
            's': 'Have you got me new battery ? \
                A new battery! A new battery! A new battery!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    
    # AGENT :  Oh non, tu ne vas pas recommencer avec ça, nous l’avons changée
    # la semaine dernière… 
    
    #? ['](4)
    # NAO : Alors quoi ?
    'r_alors': (
        {
            'g': 'confused',
            's': 'So what is it ?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    
    # AGENT  :  C’est ton jour d’audition !
    
    #? [(](5)
    #? [c] tete à droite
    # NAO : … (Nao tourne la tête à sa droite, déçu) Ooooo… Non… Tu veux encore
    # me faire faire du théâtre ?
    'r_theatre': (
        {
            'g': 'fear',
            's': 'Ohhh… no… Do you still want me \\rspd=80\\to do comedy? I do not like theater!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT : (L’agent se déplace à gauche autour de Nao) Pour décrocher le rôle
    # de ta vie! (Pendant ce temps, Nao lève la tête)
    
    #? [-](6)
    #? [P] pointer
    # NAO : (Nao lève un bras pour désigner l’agent) Tu veux vraiment te faire
    # de l’argent sur mon dos ! Tu n’as pas honte ? (Nao baisse le bras)
    'r_argent': (
        {
            'g': 'curious',
            's': '\\rspd=80\\So you really want to use me to make money! Are you not ashamed ?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    
    # AGENT : Mais toi aussi tu seras riche, Nao !

    #? [è](7)
    #? [N] neutral
    # NAO : Que veux-tu que je fasse de cet argent, je suis un robot, je n’ai
    # pas le droit de dépenser d’argent…
    'r_argent_2': (
        {
            'g': '',
            's': '\\rspd=80\\What do you want me to do with that money, I\'m a robot, I\'m not allowed to spend money...'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    #? [_](8)
    # NAO  : (Nao regarde le public, il pleure - bruit de pleur) -> (Augmenterle
    #        son et faire durer plus longtemps les pleurs)
    # 'r_cry': (
    #     {
    #         'g': 'sad',
    #         's': 'Je me sens abusé!' # NOTE Nao pleure
    #     },
    #     [
    #         ('time', 1, 'choice')
    #     ]
    # ),

    # AGENT : Arrête de faire ta scène !
    

    # (Nao lève le bras avec coude plié et reste immobile).
    
    #? [ç](9)
    # NAO  : (Surprise :) Oh ! Regarde ! Je ne peux pas… (Triste : )
    #        J’ai une vis qui s’est bloquée…  
    'r_bloquee': (
        {
            'g': 'fear',
            's': 'Look at this! I can\'t...'
        },
        [
            ('time', 3, 'r_bloquee_2')
        ]
    ),
    'r_bloquee_2': (
        {
            'g': '',
            's': '\\rspd=80\\One of my screws is stuck.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT  : Arrête de faire semblant. Je te connais… J’ai changé ton huile la
    # semaine dernière.
    
    #? [à](0)
    # NAO  : Je ! Je ? Je, je, je, (code ralentir) jejeje je ! Jèèèè
    'r_je': (
        {
            'g': '',
            's': 'I! I? I, i,  I, i, i, i, i! Iiiiiiiiiiiiiiiiiiiiii!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT : Je, j’ai quoi?? 

    #? [)](°)
    # NAO : J’ai faim !
    'r_faim': (
        {
            'g': '',
            's': '\\rspd=80\\I am hungry!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT:  Tu as mangé 20 minutes d’électricité il y a une heure !

    #? [=](+)
    # NAO : Je suis fatigué !
    'r_fatigue': (
        {
            'g': 'netural',
            's': ' I am tired!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    
    # AGENT:  Tu es resté déconnecté pendant 3 jours ! Exprès pour être en forme
    # aujourd’hui !

    #? [r]
    # NAO  : Je ! Je ? Jèèèè…
    'r_je_2': (
        {
            'g': '',
            's': 'I! I… i… i… i… i… I!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT: J’ai quoi encore !? 

    #? [t]
    # NAO: J’ai oublié le texte !!! (Effrayé)
    'r_oublie': (
        {
            'g': 'fear',
            's': '\\rspd=80\\I don’t remember the text anymore!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT:  Je l’ai sur USB ! (il lui met une clé usb dans le dos)

    #? [y]
    # NAO : OK. Retour au choix initial… Avec qui veux-tu me faire travailler ?
    'r_retour': (
        {
            'g': '',
            's': 'Ok. \\rspd=80\\Back to the beginning. Who \\pau=200\\ am I \\pau=200\\ supposed to work with?'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT: Le grand metteur en scène international que nous connaissons tous
    # (le grand, l’unique, l’exceptionnel…)
    
    #? [u]
    # NAO: (Nao part de l’autre côté) Je te l’ai déjà dit ! Je ne veux pas
    # travailler avec ce metteur en scène, je veux une metteuse en scène !
    # (Répéter plusieurs fois tandis que Nao s’en va)
    'r_metteuse': (
        {
            'g': '',
            's': 'Oh, no, \\rspd=80\\I already told you! I don\'t want to work with your great master of theater, I want to work with a \\rspd=60\\ great woman director!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),


    # AGENT: Arrête de faire ton cirque, c’est moi qui décide…Tu vas faire cette
    #  audition avec ce grand metteur en scène, point barre.

    #? [i]
    
    # NAO: Tu m'harcèles!!!! Ça c’est de la violence robotique!
    
    
   
    # (En vitesse, a capela) Les robots sont fabriqués libres et demeurent
    # libres et égaux en droit avec les humains….avec les humains….
    'r_harcelement': (
        {
            'g': '',
            's': '\\rspd=80\\You are tormenting me! This is robot oh phobic violence!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    #? [P] pointer
    #? [o] 
    # (Nao avec un bras pointe l’agent) Tu n’es pas mon maître!!!!
    'r_harcelement_2': (
        {
            'g': '',
            's': 'You are not my boss!!!'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    #? [p]
    # (Nao plie son coude)
    # Je te rappelle la Déclaration des droits robotiques universels.
    # Art. 1 Les robots sont fabriqués libres et demeurent libres et égaux en
    # droit avec les humains
    'r_harcelement_3': (
        {
            'g': '',
            's': '\\rspd=80\\Let me remind you the Universal Declaration of Robotics Rights\
                  universels. Article one, Robots are made free and remain free and equal in rights to humans.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    #? [7] or [9] to rotate
    #? [f]
     # (L’Agent se fige; Nano se tourne pour sortir de scène, en marchant,
    # il répète: )
    # Les robots sont fabriqués libres et demeurent libres et égaux en droit
    # avec les humains.
    'r_harcelement_4': (
        {
            'g': '',
            's': '\\rspd=90\\Robots are made free and remain free and equal in rights to humans.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    #? [g]
    'r_harcelement_5': (
        {
            'g': '',
            's': 'Robots are made free and remain free and equal in rights to humans.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    #? Nao s'éteint

    'pointer': (
        {
            's': '',
            'la': [-0.5,0,0,0,0,1]
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    # Comportements de base

    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,

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

            ('key', '8', 'walk_fwd'),
            ('key', '5', 'stop'),
            ('key', '2', 'walk_back'),
            ('key', '4', 'strife_left'),
            ('key', '6', 'strife_right'),
            ('key', '7', 'rotate_left'),
            ('key', '9', 'rotate_right'),

            ('key', 'j', 'end'),

            ('key', '&', 'r_yes'),
            ('key', 'é', 'r_femme'),
            ('key', '\"', 'r_batterie'),
            ('key', '\'', 'r_alors'),
            ('key', '(', 'r_theatre'),
            ('key', '-', 'r_argent'),
            ('key', 'è', 'r_argent_2'),
            ('key', '_', 'r_cry'),
            ('key', 'ç', 'r_bloquee'),
            ('key', 'à', 'r_je'),
            ('key', ')', 'r_faim'),
            ('key', '=', 'r_fatigue'),
            ('key', 'r', 'r_je_2'),
            ('key', 't', 'r_oublie'),
            ('key', 'y', 'r_retour'),
            ('key', 'u', 'r_metteuse'),
            ('key', 'i', 'r_harcelement'),
            ('key', 'o', 'r_harcelement_2'),
            ('key', 'p', 'r_harcelement_3'),
            ('key', 'f', 'r_harcelement_4'),
            ('key', 'g', 'r_harcelement_5'),
            ('key', 'P', 'pointer'),

            ('key', ';', 'progressiveD'),
            ('key', ',', 'progressiveG'),
            ('key', '!', 'degressiveD'),
            ('key', ':', 'degressiveG'),

            ('key', 'S', 'sad'),
            ('key', 'F', 'fear'),
            ('key', 'C', 'confused'),

            ('key', 'N', 'neutral'),
            
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

    'progressiveD': ( {'w': [0,0,0,0,0,-1], 'h': [-1.5,+0.0]}, [('time', 2.5, 'progres_D_Retablis')]),
    'progres_D_Retablis':( {'w': [0,0.0,0,0,0,0], 'h': [+0.0,+0.0]}, [('time', 0.1, 'progres_D_Retablis1')]),
    'progres_D_Retablis1':( {'g': 'debout'}, [('time', 0.1, 'choice')]),

    'progressiveG': ( {'w': [0,0,0,0,0,1], 'h': [+1.5,+0.0]}, [('time', 2.5, 'progres_G_Retablis')]),
    'progres_G_Retablis':( {'w': [0,0.0,0,0,0,0], 'h': [+0.0,+0.0]}, [('time', 0.1, 'progres_G_Retablis1')]),
    'progres_G_Retablis1':( {'g': 'debout'}, [('time', 0.1, 'choice')]),

    'degressiveD': ( {'w': [0,0,0,0,0,-1], 'h': [0.0,+0.0]}, [('time', 1, 'degressiveD1')]),
    'degressiveD1': ( {'w': [0,0,0,0,0,-1], 'h': [0.5,+0.0]}, [('time', 4, 'degres_D_Retablis')]),
    'degres_D_Retablis':( {'w': [0,0.0,0,0,0,0], 'h': [+0.0,+0.0]}, [('time', 0.1, 'degres_D_Retablis1')]),
    'degres_D_Retablis1':( {'g': 'debout'}, [('time', 0.1, 'choice')]),

    'degressiveG': ( {'w': [0,0,0,0,0,1], 'h': [0.0,+0.0]}, [('time', 1, 'degressiveG1')]),
    'degressiveG1': ( {'h': [-0.5,+0.0]}, [('time', 4, 'degres_G_Retablis')]),
    'degressiveG2': ( {'w': [0,0,0,0,0,1], 'h': [-0.5,+0.0]}, [('time', 1, 'degres_G_Retablis')]),
    'degres_G_Retablis':( {'w': [0,0.0,0,0,0,0], 'h': [+0.0,+0.0]}, [('time', 0.1, 'degres_G_Retablis1')]),
    'degres_G_Retablis1':( {'g': 'debout'}, [('time', 0.1, 'choice')]),

    'sad': (
        {
            'g': 'sad',
            's': ''
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    'fear': (
        {
            'g': 'fear',
            's': ''
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    'confused': (
        {
            'g': 'confused',
            's': ''
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'neutral': (
        {
            'g': 'neutral',
            's': '\\pau=2000\\'
        }, 
        [
            ('time', 1, 'choice')
        ]
    ),
}