######################################################## SCENE 18 ######################################################

#! Predrag installe la caméra

# ! switch to ITALIAN
# ! rosservice call /qt_robot/speech/config "language: 'it-IT'
# ! > pitch: 0
# ! > speed: 0
# ! > "

look_up = [0.0,-20.0]
look_center = [0.0,0.0]
look_down = [0.0,+10.0]
look_right = [-20.0,0.0]
look_left = [+20.0,0.0]
look_up_right = [-20.0,-20.0]
look_up_left = [+20.0,-20.0]
look_down_right = [-10.0,+10.0]
look_down_left = [+10.0,+10.0]

TEMPS_ACTEUR = 3

spectacle = {
    # QT : Où est le comédien ? Toujours en retard celui-là.
    # S’il continue je le renvoie. On les connaît ces humains,
    # s’ils n’ont pas de café, ils ne peuvent pas travailler !
    'r1_retard' : (
        {
            'e' : 'QT/talkinglong',
            'g' : 'QT/so',
            's' : 'Ma dov’è il prossimo attore che deve passare il provino ? Sempre così. Sempre in ritardo ! '
        }, # ! Regard : cherche le comedien, regarde le publique
        [
            ('time', 8, 'r1_retard_2')
        ]
    ),
    'r1_retard_2' : (
        {
            'e' : 'QT/talkinglong',
            'g' : 'QT/sneezing',
            's' : 'Si sa come sono questi umani, senza caffé non ce la fanno a lavorare !'
        }, # ! Regard : cherche le comedien, regarde le publique
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # Comédien : ça va je n’ai que 2 minutes de retard,
    # je ne marche pas par procédure comme toi QT.

    # QT : De toute façon vous les humains, la ponctualité,
    # ça vous connaît n'est-ce pas ?
    # Je vous demanderai de suivre mon protocole de A à Z,
    # et ça commence par être à l’heure.
    # Bon, ne perdons pas plus de temps, commençons.
    'r2_commencons' : (
        {
            'e' : 'QT/talkinglong',
            'g' : 'QT/bored',
            's' : 'Tant’è, voi umani la puntualità non sapete proprio cosa sia.'
        }, # ! Regard : regarde par terre, regard neutre
        [
            ('time', 6, 'r2_commencons_2')
        ]
    ),
    'r2_commencons_2' : (
        {
            'e' : 'QT/talkinglong',
            'g' : 'QT/surprise',
            's' : 'Vi chiedo di seguire il mio protocollo dalla A alla Z e per prima cosa è richiesto di essere puntuali.'
        }, # ! Regard : regarde par terre, regard neutre
        [
            ('time', 11, 'r2_commencons_3')
        ]
    ),
    'r2_commencons_3' : (
        {
            'e' : 'QT/talkinglong',
            'g' : 'QT/handclap',
            's' : 'Suvvia, non perdiamo altro tempo, cominciamo.'
        }, # ! Regard : regarde par terre, regard neutre
        [
            ('time', 0.1, 'choice')
        ]
    ),

    # Comédien : D'accord, je me place où ? 

    # Le comédien se place. 

    # QT : Êtes-vous professionnel ? Placez vous.
    'r3_professionnel' : (
        {
            'e' : 'QT/talking',
            'g' : '',
            'h' : [0, 0],
            's' : 'Lei è un professionista, vero?'
        },
        [
            ('time', 2, 'r3_professionnel_2')
        ]
    ),

    'r3_professionnel_2' : (
        {
            'e' : 'QT/talking',
            'g' : '',
            'la' : [40, -58, -35],
            's' : 'Allora prenda subito posto.'
        },
        [
            ('time', 2, 'r3_professionnel_3')
        ]
    ),

    'r3_professionnel_3' : (
        {
            'e' : '',
            'g' : '',
            'la' : [89, -58, -35],
            's' : ''
        },
        [
            ('time', 0.1, 'detect_gestures_1')
        ]
    ),


  # 1MG Vous devez intégrer qu’un humain doit rester dans l’axe visuel des
    # robots et pas l’inverse.
    # (un temps)
    '1mj' : (
        {
            'e' : 'QT/talking',
            'g' : '',
            'h' : look_center,
            
            's' : 'Indietreggi, si vedrà meno che recita male.'
        },
        [
            ('time', 6 + TEMPS_ACTEUR, 'detect_gestures_1')
        ]
    ),

    # 1MD Vous n’êtes pas dans la lumière.
    '1mc' : (
        {
            'e' : 'QT/yawn',
            'g' : '',
            'h' : look_down_left,
            's' : '#YAWN01#'
        },
        [
            ('time', 2, '1mc_b')
        ]
    ),

    '1mc_b' : (
        {
            'e' : 'QT/talking',
            'g' : '',
            'h' : look_down_right,
            's' : 'Si fermi, si fermi la prego.'
        },
        [
            ('time', 5, '1mc_c')
        ]
    ),

    '1mc_c' : (
        {
            'e' : 'QT/talking',
            'g' : '',
            'h' : look_down_left,
            's' : 'Ma non sente che proprio non funziona?'
        },
        [
            ('time', 6, '1mc_d')
        ]
    ),

    '1mc_d' : (
        {
            'e' : 'QT/yawn',
            'g' : '',
            'h' : look_down_right,
            's' : 'Via, ripeta.'
        },
        [
            ('time', 2 + TEMPS_ACTEUR, 'detect_gestures_1')
        ]
    ),

    # 1MF ça fait longtemps que vous ne jouez plus en avant-scène, vous vous
    # prenez pour qui ?
    '2mj' : (
        {
            'e' : 'QT/talkinglong',
            'g' : '',
            'h' : look_right,
            's' : 'Ma cosa fa a fondo scena? Si avvicini, le sue capacità vocali sono limitate.'
             #'s' : 'ça fait longtemps que vous ne jouez plus en avant-scène, vous vous prenez pour qui ?'
        },
        [
            ('time', 10 + TEMPS_ACTEUR, 'detect_gestures_1')
        ]
    ),

    # 2MF Écoutez ce que je vous dis et arrêtez avec votre susceptibilité
    # d’humain.
    # (un temps)detect_gestures_1
    # Concentrez-vous
    '2mc' : (
        {
            'e' : 'QT/talkinglong',
            'g' : '',
            'h' : look_right,
            's' : 'Ascolti quello che dico e la smetta con questa suscettibilità da umano. \\pau=1000\\ Si concentri.'
        },
        [
            ('time', 10 + TEMPS_ACTEUR, 'detect_gestures_2')
        ]
    ),

    # (un temps, le robot s’agace)
    # '2mc_concentrez-vous_2' : (
    #     {
    #         'e' : 'QT/angry',
    #         'g' : 'QT/angry',
    #         's' : ''
    #     },
    #     [
    #         ('time', 6, 'detect_gestures_2')
    #     ]
    # ),


    # 1MF Recule,, on verra moins que vous jouez mal.
    # (un temps)
    '1mj_2' : (
        {
            'e' : 'QT/talkinglong',
            'g' : '',
            'h' : look_center,
            's' : ' Eh oh, non ci siamo proprio! Lei deve capire che è l’umano che deve restare nell’asse visivo del robot, non il contrario...'
        },
        [
            ('time', 12 + TEMPS_ACTEUR, 'detect_gestures_2')
        ]
    ),

        # 2MD Vous ne savez rien faire comme on vous le demande, vous êtes vraiment
    # binaire comme humain.
    '1mc_2' : (
        {
            'e' : 'QT/yawn',
            'g' : '',
            'h' : look_left,
            's' : 'Non così.'
            #'s' : 'Vous ne savez rien faire comme on vous le demande, vous êtes vraiment binaire comme humain.'
        },
        [
            ('time', 3 + TEMPS_ACTEUR, 'detect_gestures_2')
        ]
    ),


    # 2MG On n’avait pas dit que vous deviez un peu retravailler votre
    # carrosserie ? Mettez-vous un peu de l’autre côté.
    # (QT perd patience)
    '2mj_2' : (
        {
            'e' : 'QT/talkinglong',
            'g' : '',
            'h' : look_right,
            's' : 'Ma non è possibile!! Non riesce proprio a fare quello che le viene chiesto. Lei è veramente binario, come tutti gli umani...'
            #'s' : 'On n’avait pas dit que vous deviez un peu retravailler votre carrosserie ? Mettez-vous un peu de l’autre côté.'
        },
        [
            ('time', 8 + TEMPS_ACTEUR, 'detect_gestures_2')
        ]
    ),

    # Mais que faites-vous en fond de scène ? Approchez-vous, vous savez bien
    # que vous êtes très limité niveau volume sonore.
    # (QT regarde le comédien exécuter les actions qui lui demande)
    '2mc_2' : (
        {
            'e' : 'QT/angry',
            'g' : '',
            'h' : look_down_right,
            's' : 'No No No, è in ombra. Ma non lo sente ?'
            #'Mais que faites-vous en fond de scène ? Approchez-vous du publique, vous êtes très limité niveau volume sonore.'
        },
        [
            ('time', 5 + TEMPS_ACTEUR, 'detect_gestures_2')
        ]
    ),


    # Le comédien s’agace. 

    # Comédien : Tu sais quoi la ponctualité ? Je vais te refaire ta carrosserie
    # tu vas comprendre ce qu’il t’arrive. 

    # Il le débranche.

    'r4_partez' : (
        {
            'e' : 'QT/talkinglong',
            'g' : '',
            's' : 'Niente, non funziona, è disperante! Se ne vada e faccai entrare il prossimo!'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'robot_code' : (
        {
            'e' : 'QT/robot_code',
            'g' : '',
            's' : ''
        },
        [
            ('time', 0.1, 'choice')
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
            ('key', '&', 'r1_retard'),
            ('key', 'é', 'r2_commencons'),
            ('key', '\"', 'r3_professionnel'),
            ('key', '\'', 'r4_partez'),

            # Video
            ('key', '(', 'robot_code'), 
            # Lance une video de code qui defile
            #! Arreter avec terminal :
            #? rosservice call qt_robot/emotion/stop
            

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

            ('key', 'r', 'reset_posture'),
            ('key', '*', 'end'),

            ('key', 'g', 'detect_gestures_1'),
            ('key', 'G', 'detect_gestures_2'),
        ]
    ),

    'detect_gestures_1' : (
        {
            'e' : '',
            'g' : '',
            's' : '' 
        },
        [
            ('gesture', 'cour_1m', '1mc'),
            ('gesture', 'jardin_1m', '1mj'),
            ('gesture', 'cour_2m', '2mc'), # ! CHANGE
            ('gesture', 'jardin_2m', '2mj'),

            ('key', 'p', '1mc'),
            ('key', 'o', '1mj'),
            ('key', 'm', '2mc'),
            ('key', 'l', '2mj'),

            ('key', 'c', 'choice'),
        ]
    ),

    'detect_gestures_2' : (
        {
            'e' : '',
            'g' : '',
            's' : '' 
        },
        [
            ('gesture', 'cour_1m', '1mc_2'),
            ('gesture', 'jardin_1m', '1mj_2'),
            ('gesture', 'cour_2m', '2mc_2'),
            ('gesture', 'jardin_2m', '2mj_2'),

            ('key', 'p', '1mc_2'),
            ('key', 'o', '1mj_2'),
            ('key', 'm', '2mc_2'),
            ('key', 'l', '2mj_2'),

            ('key', 'c', 'choice'),
        ]
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