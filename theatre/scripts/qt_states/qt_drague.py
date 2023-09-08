# Groupe QT / Semi-autonomie

# Jeu de drague/Flatterie

# Avec : Ouliana, Yannis, Sarah (notes JD en phonétique, merci de rectifier)

# Interagir avec l'acteur, improvisation, jouer sur les mots. 
# ( exemple : je suis prête  à te faire une déclaration, si tu te mets à gauche
# je te déclare ma flamme)
# Dès le début, on va savoir dans quel dispositif scénique nous sommes. 
# Dès que l'acteur se déplace, QT complimente l'acteur. 

# 2MG 2MF 2MD
# 1MG 1MF 1MD
#    Robot

# Version spectacle : 4 carrées
# 7 sept.

spectacle = {
    # QT : Où est le comédien ? Toujours en retard celui-là.
    # S’il continue je le renvoie. On les connaît ces humains,
    # s’ils n’ont pas de café, ils ne peuvent pas travailler !
    'r1_retard' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Où est le comédien ? Toujours en retard celui-là. s’il \
                continue je le renvoie. On les connaît ces humains, s’ils \
                n’ont pas de café, ils ne peuvent pas travailler !'
        },
        [
            ('time', 6, 'choice')
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
            'e' : '',
            'g' : '',
            's' : 'De toute façon vous les humains, la ponctualité, ça vous \
                connaît n\'est-ce pas ? Je vous demanderai de suivre mon \
                protocole de A à Z, et ça commence par être à l’heure. \
                Bon, ne perdons pas plus de temps, commençons.'
        },
        [
            ('time', 6, 'choice')
        ]
    ),


    # Comédien : Ok la rigueur, je me place où ? 

    # Le comédien se place. 

    # QT : Êtes-vous professionnel ? Placez vous.
    'r3_professionnel' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Êtes-vous professionnel ? Placez vous.'
        },
        [
            ('time', 4, 'choice')
        ]
    ),


    # 1MD Vous n’êtes pas dans la lumière.
    '1md' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous n’êtes pas dans la lumière.'
        },
        [
            ('time', 10, 'detect_gestures_1')
        ]
    ),


    # 1MG Vous devez intégrer qu’un humain doit rester dans l’axe visuel des
    # robots et pas l’inverse.
    # (un temps)
    '1mg' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous devez intégrer qu’un humain doit rester dans l’axe \
                visuelle du robot et pas l’inverse.\\pau=500\\Reprenez!'
        },
        [
            ('time', 15, 'detect_gestures_1')
        ]
    ),


    # 1MF ça fait longtemps que vous ne jouez plus en avant-scène, vous vous
    # prenez pour qui ?
    '2mg' : (
        {
            'e' : '',
            'g' : '',
            's' : 'ça fait longtemps que vous ne jouez plus en avant-scène, \
                vous vous prenez pour qui ?'
        },
        [
            ('time', 15, 'detect_gestures_1')
        ]
    ),


    # 2MF Écoutez ce que je vous dis et arrêtez avec votre susceptibilité
    # d’humain.
    # (un temps)detect_gestures_1
    # Concentrez-vous
    '2md' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Écoutez ce que je vous dis et arrêtez avec votre\
                  susceptibilité d’humain. \\pau=500\\ Concentrez-vous.'
        },
        [
            ('time', 6, 'detect_gestures_2')
        ]
    ),
    # (un temps, le robot s’agace)
    '2mf_concentrez-vous_2' : (
        {
            'e' : 'QT/angry',
            'g' : 'QT/angry',
            's' : ''
        },
        [
            ('time', 6, 'detect_gestures_2')
        ]
    ),


    # [le robot passe à une nouvelle configuration du carré]
    # Mais que faites-vous en fond de scène ? Approchez-vous, vous savez bien
    # que vous êtes très limité niveau volume sonore.
    # (QT regarde le comédien exécuter les actions qui lui demande)
    '2md_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Mais que faites-vous en fond de scène ? Rapprochez-vous du publique, \
                 vous savez bien que vous êtes très limité niveau volume sonore.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),

    # 1MF Recule,, on verra moins que vous jouez mal.
    # (un temps)
    '1mg_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Reculez.. on verra moins que vous jouez mal.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # 2MG On n’avait pas dit que vous deviez un peu retravailler votre
    # carrosserie ? Mettez-vous un peu de l’autre côté.
    # (QT perd patience)
    '2mg_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'On n’avait pas dit que vous deviez un peu retravailler \
                votre carrosserie ? Mettez-vous un peu de l’autre côté.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # 2MD Vous ne savez rien faire comme on vous le demande, vous êtes vraiment
    # binaire comme humain.
    '1md_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous ne savez rien faire comme on vous le demande, vous \
                êtes vraiment binaire comme humain.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # Le comédien s’agace. 

    # Comédien : Tu sais quoi la ponctualité ? Je vais te refaire ta carrosserie
    # tu vas comprendre ce qu’il t’arrive. 

    # Il le débranche.

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
            ('gesture', 'cour_1m', '1md'),
            ('gesture', 'jardin_1m', '1mg'),
            ('gesture', 'cour_2m', '2md'),
            ('gesture', 'jardin_2m', '2mg'),
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
            ('gesture', 'cour_1m', '1md_2'),
            ('gesture', 'jardin_1m', '1mg_2'),
            ('gesture', 'cour_2m', '2md_2'),
            ('gesture', 'jardin_2m', '2mg_2'),
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
}


# VErsion 4 : 4 carrées 
# 27 juin

states_v4 = {
    # QT : Où est le comédien ? Toujours en retard celui-là.
    # S’il continue je le renvoie. On les connaît ces humains,
    # s’ils n’ont pas de café, ils ne peuvent pas travailler !
    'r1_retard' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Où est le comédien ? Toujours en retard celui-là. s’il \
                continue je le renvoie. On les connaît ces humains, s’ils \
                n’ont pas de café, ils ne peuvent pas travailler !'
        },
        [
            ('time', 6, 'choice')
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
            'e' : '',
            'g' : '',
            's' : 'De toute façon vous les humains, la ponctualité, ça vous \
                connaît n\'est-ce pas ? Je vous demanderai de suivre mon \
                protocole de A à Z, et ça commence par être à l’heure. \
                Bon, ne perdons pas plus de temps, commençons.'
        },
        [
            ('time', 6, 'choice')
        ]
    ),


    # Comédien : Ok la rigueur, je me place où ? 

    # Le comédien se place. 

    # QT : Êtes-vous professionnel ? Placez vous.
    'r3_professionnel' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Êtes-vous professionnel ? Placez vous.'
        },
        [
            ('time', 4, 'choice')
        ]
    ),


    # 1MD Vous n’êtes pas dans la lumière.
    '1md' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous n’êtes pas dans la lumière.'
        },
        [
            ('time', 10, 'detect_gestures_1')
        ]
    ),


    # 1MG Vous devez intégrer qu’un humain doit rester dans l’axe visuel des
    # robots et pas l’inverse.
    # (un temps)
    '1mg' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous devez intégrer qu’un humain doit rester dans l’axe \
                visuelle du robot et pas l’inverse.'
        },
        [
            ('time', 15, 'detect_gestures_1')
        ]
    ),


    # 1MF ça fait longtemps que vous ne jouez plus en avant-scène, vous vous
    # prenez pour qui ?
    '2mg' : (
        {
            'e' : '',
            'g' : '',
            's' : 'ça fait longtemps que vous ne jouez plus en avant-scène, \
                vous vous prenez pour qui ?'
        },
        [
            ('time', 15, 'detect_gestures_1')
        ]
    ),


    # 2MF Écoutez ce que je vous dis et arrêtez avec votre susceptibilité
    # d’humain.
    # (un temps)detect_gestures_1
    # Concentrez-vous
    '2md' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Écoutez ce que je vous dis et arrêtez avec votre\
                  susceptibilité d’humain. \\pau=500\\ Concentrez-vous.'
        },
        [
            ('time', 6, 'detect_gestures_2')
        ]
    ),
    # (un temps, le robot s’agace)
    '2mf_concentrez-vous_2' : (
        {
            'e' : 'QT/angry',
            'g' : 'QT/angry',
            's' : ''
        },
        [
            ('time', 6, 'detect_gestures_2')
        ]
    ),


    # [le robot passe à une nouvelle configuration du carré]
    # Mais que faites-vous en fond de scène ? Approchez-vous, vous savez bien
    # que vous êtes très limité niveau volume sonore.
    # (QT regarde le comédien exécuter les actions qui lui demande)
    '2md_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Mais que faites-vous en fond de scène ? Approchez-vous, \
                 vous savez bien que vous êtes très limité niveau volume sonore.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),

    # 1MF Recule,, on verra moins que vous jouez mal.
    # (un temps)
    '1mg_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Reculez.. on verra moins que vous jouez mal.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # 2MG On n’avait pas dit que vous deviez un peu retravailler votre
    # carrosserie ? Mettez-vous un peu de l’autre côté.
    # (QT perd patience)
    '2mg_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'On n’avait pas dit que vous deviez un peu retravailler \
                votre carrosserie ? Mettez-vous un peu de l’autre côté.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # 2MD Vous ne savez rien faire comme on vous le demande, vous êtes vraiment
    # binaire comme humain.
    '1md_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous ne savez rien faire comme on vous le demande, vous \
                êtes vraiment binaire comme humain.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # Le comédien s’agace. 

    # Comédien : Tu sais quoi la ponctualité ? Je vais te refaire ta carrosserie
    # tu vas comprendre ce qu’il t’arrive. 

    # Il le débranche.

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

            ('key', 'r', 'reset_posture'),
            ('key', 'e', 'end'),

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
            ('gesture', 'human_0_right_1m', '1md'),
            ('gesture', 'human_0_left_1m', '1mg'),
            ('gesture', 'human_0_right_2m', '2md'),
            ('gesture', 'human_0_left_2m', '2mg'),
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
            ('gesture', 'human_0_right_1m', '1md_2'),
            ('gesture', 'human_0_left_1m', '1mg_2'),
            ('gesture', 'human_0_right_2m', '2md_2'),
            ('gesture', 'human_0_left_2m', '2mg_2'),
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
}


#--------------------------------- VERSION 3 ---------------------------------#
# Pour : RobotAct VI
# Date : 26/06/2023

states_v3 = {
    # QT : Où est le comédien ? Toujours en retard celui-là.
    # S’il continue je le renvoie. On les connaît ces humains,
    # s’ils n’ont pas de café, ils ne peuvent pas travailler !
    'r1_retard' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Où est le comédien ? Toujours en retard celui-là. s’il \
                continue je le renvoie. On les connaît ces humains, s’ils \
                n’ont pas de café, ils ne peuvent pas travailler !'
        },
        [
            ('time', 6, 'choice')
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
            'e' : '',
            'g' : '',
            's' : 'De toute façon vous les humains, la ponctualité, ça vous \
                connaît n\'est-ce pas ? Je vous demanderai de suivre mon \
                protocole de A à Z, et ça commence par être à l’heure. \
                Bon, ne perdons pas plus de temps, commençons.'
        },
        [
            ('time', 6, 'choice')
        ]
    ),


    # Comédien : Ok la rigueur, je me place où ? 

    # Le comédien se place. 

    # QT : Êtes-vous professionnel ? Placez vous.
    'r3_professionnel' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Êtes-vous professionnel ? Placez vous.'
        },
        [
            ('time', 4, 'choice')
        ]
    ),


    # 1MD Vous n’êtes pas dans la lumière.
    '1md_lumiere' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous n’êtes pas dans la lumière.'
        },
        [
            ('time', 10, 'detect_gestures_1')
        ]
    ),


    # 1MG Vous devez intégrer qu’un humain doit rester dans l’axe visuel des
    # robots et pas l’inverse.
    # (un temps)
    '1mg_axe' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous devez intégrer qu’un humain doit rester dans l’axe \
                visuel des robots et pas l’inverse.'
        },
        [
            ('time', 15, 'detect_gestures_1')
        ]
    ),


    # 1MF ça fait longtemps que vous ne jouez plus en avant-scène, vous vous
    # prenez pour qui ?
    '1mf_avant-scene' : (
        {
            'e' : '',
            'g' : '',
            's' : 'ça fait longtemps que vous ne jouez plus en avant-scène, \
                vous vous prenez pour qui ?'
        },
        [
            ('time', 15, 'detect_gestures_1')
        ]
    ),


    # 2MF Écoutez ce que je vous dis et arrêtez avec votre susceptibilité
    # d’humain.
    # (un temps)detect_gestures_1
    # Concentrez-vous
    '2mf_concentrez-vous' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Écoutez ce que je vous dis et arrêtez avec votre\
                  susceptibilité d’humain. \\pau=500\\ Concentrez-vous.'
        },
        [
            ('time', 6, '2mf_concentrez-vous_2')
        ]
    ),
    # (un temps, le robot s’agace)
    '2mf_concentrez-vous_2' : (
        {
            'e' : 'QT/angry',
            'g' : 'QT/angry',
            's' : ''
        },
        [
            ('time', 6, 'detect_gestures_2')
        ]
    ),


    # [le robot passe à une nouvelle configuration du carré]
    # Mais que faites-vous en fond de scène ? Approchez-vous, vous savez bien
    # que vous êtes très limité niveau volume sonore.
    # (QT regarde le comédien exécuter les actions qui lui demande)
    '2mf_approchez' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Mais que faites-vous en fond de scène ? Approchez-vous, \
                 vous savez bien que vous êtes très limité niveau volume sonore.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),

    # 1MF Recule,, on verra moins que vous jouez mal.
    # (un temps)
    '1mf_recule' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Recule.. on verra moins que vous jouez mal.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # 2MG On n’avait pas dit que vous deviez un peu retravailler votre
    # carrosserie ? Mettez-vous un peu de l’autre côté.
    # (QT perd patience)
    '2mg_carrosserie' : (
        {
            'e' : '',
            'g' : '',
            's' : 'On n’avait pas dit que vous deviez un peu retravailler \
                votre carrosserie ? Mettez-vous un peu de l’autre côté.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # 2MD Vous ne savez rien faire comme on vous le demande, vous êtes vraiment
    # binaire comme humain.
    '2md_binaire' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Vous ne savez rien faire comme on vous le demande, vous \
                êtes vraiment binaire comme humain.'
        },
        [
            ('time', 15, 'detect_gestures_2')
        ]
    ),


    # Le comédien s’agace. 

    # Comédien : Tu sais quoi la ponctualité ? Je vais te refaire ta carrosserie
    # tu vas comprendre ce qu’il t’arrive. 

    # Il le débranche.

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

            ('key', 'r', 'reset_posture'),
            ('key', 'e', 'end'),

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
            ('gesture', 'human_0_right_1m', '1md_lumiere'),
            ('gesture', 'human_0_left_1m', '1mg_axe'),
            ('gesture', 'human_0_center_1m', '1mf_avant-scene'),
            ('gesture', 'human_0_center_2m', '2mf_concentrez-vous'),
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
            ('gesture', 'human_0_right_2m', '2md_binaire'),
            ('gesture', 'human_0_left_2m', '2mg_carrosserie'),
            ('gesture', 'human_0_center_1m', '1mf_recule'),
            ('gesture', 'human_0_center_2m', '2mf_approchez'),
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
}

#--------------------------------- VERSION 2 ---------------------------------#
# Pour : RobotAct V
# Date : 26/05/2023

states_v2 = {
    # 1MF =  à 1 mètre, face à QT
    # “etat1” : {{‘s’ : “Pas si près, je ne peux pas respirer.”},
    # [(‘time’, 1, “etat2”)]}
    # {‘s’ : “On dirait que vous les humains n'avez jamais entendu parler
    # d'intimité !”}
    # {‘g’ : ”angry”, ‘e’ : “angry”, ‘s’ : “Recule, tu pues !”}
    # “afraid” Arrête, je suis un peu timide ! 
    'human_0_center_1m' : (
        {
            'e' : 'QT/breathing_exercise',
            'g' : 'QT/disgusted',
            's' : 'Pas si près, je ne peux pas respirer.'
        },
        [
            ('time', 6, 'choice')
        ]
    ),

    # 1MG = à 1 mètre, à la gauche de QT 
    # {‘s’ : “\pau=300\ J'ai envie de te contempler. D'ailleurs tu me fais
    # rougir !”, “e” : kiss, “g” : kiss, “s” : Dis-moi, est-ce que je te plais?} 
    # {‘s’ : “Vas gauchement à droite ou droit à gauche!”}
    # {‘s’ : “\vct=50\ T'as jamais entendu parler de l'espace personnel ?”}
    # “breathing_exercise” \rms=1\U-la la ! 
    'human_0_left_1m' : (
        {
            'e' : 'QT/kiss',
            'g' : 'QT/kiss',
            's' : '\\pau=300\\ J\'ai envie de te contempler. D\'ailleurs tu me fais rougir ! \\pau=1000\\ Dis-moi, est-ce que je te plais ?'
        },
        [
            ('time', 6, 'choice')
        ]
    ),

    # 1MD = à 1 mètre, à la gaucΑ1MF de QT
    # Je n’ai pas d’ami….Dis-moi, est-ce que je te plais ?} 
    # {‘s’: ‘g’: “angry”,  ‘e’: “angry”, ‘s’:“\vct=60\ Ouste!\sel=alt\” }
    # {‘s’: ‘g’: “angry”,  ‘e’: “angry”, ‘s’:“\vct=120\ Tu es super \sel=alt\
    # collant!”} 
    # {‘s’: ‘g’: “afraid”,  ‘e’: “afraid”, ‘s’: “\vct=90\ Pas si près, je suis
    # claustrophobe!”} 
    # Encore dix centimètres, halte, pas douze!
    # “angry” \pau=300\C’est beaucoup, hum ?
    'human_0_right_1m' : (
        {
            'e' : 'QT/shy',
            'g' : 'QT/shy',
            's' : 'Je n’ai pas d’ami\\pau=300\\Je n’ai pas d’ami\\pau=300\\ Je n’ai pas d’ami. Dis-moi, est-ce que je te plais ?'
        },
        [
            ('time', 12, 'choice')
        ]
    ),

    # 02MF = à 2 mètres, face à QT
    # Avance un peu, je ne te vois pas.
    # \rspd=80\ Je ne t'entends pas très bien. avance
    # Avance que je te vois.
    # { 's' : "\vce=speaker=Lily\ Un peu plus !" }
    # #SNEEZE01#Viens ! Tu me manques ! 
    'human_0_center_2m' : (
        {
            'e' : 'QT/talking',
            'g' : 'QT/surprised',
            's' : '\\rspd=80\\ Je ne t\'entends pas très bien. Avance que je te vois.'
        },
        [
            ('time', 6, 'choice')
        ]
    ),

    # 2MG = à 2 mètres gauche. 
    # Là tu es hors du champ ma belle!
    # C’est drole !!  tu me fais rire
    # \rmw=0\ Qui es tu ?
    # Mais que fais-tu aussi loin ?\pau=300\ Tu sais que je te vois!
    # “happy_blinking” \vce=speaker=Will\Coucou ! 
    'human_0_left_2m' : (
        {
            'e' : 'QT/happy',
            'g' : 'QT/happy',
            's' : 'C’est drole ! Tu me fais rire'
        },
        [
            ('time', 6, 'choice')
        ]
    ),

    # 2MD = à 2 mètres droite.
    # Je t’aime mais je dois te quitter, adieu !
    # Tu  \pau=300\ me \pau=300\ manques. 
    #  \rspd=50\ Tu as un truc sur la figure, \rspd=80\viens que je l'enlève 
    # Tu as un bouton, viens-là !
    # { 's' : "#SNEEZE01# ai ai ai je suis malade! \rspd=40\ ai ai ai
    # “calming_down” \prn= n E1 s l EI \La bise ! 
    'human_0_right_2m' : (
        {
            'e' : 'QT/with_a_cold_sneezing',
            'g' : 'QT/sad',
            's' : '#SNEEZE01# Pardon, je suis malade !'
        },
        [
            ('time', 6, 'choice')
        ]
    ),


    # 2MF = à 2 mètres face.
    # n’importe quoi! \pau=300\
    # La vie est belle ! \aud=“pathway+filename”\
    # Sans toi ça sera mieux! 
    # #LAUGH01# J'ai faim \aud=“pathway+filename”\ .
    # {‘g’ : «joie», ‘e’ : « joie », ‘s’ : « Youuuhouuu ! Enfin tranquille !! »}
    # Va-t’en! Lache, je n’ai pas besoin de toi!
    # { 's' : "#SNEEZE01# Pardon, je suis malade !" }
    # “kiss”  #SNEEZE01#Quels beaux tous les gens! Je suis enchanté !
}

#--------------------------------- VERSION 1 ---------------------------------#
# Pour : RobotAct V
# Date : 25/05/2023

states_v1 = {
    # 1MF =  à 1 mètre, face à QT
    # “etat1” : {{‘s’ : “Salut comment tu vas ?? ”}, [(‘time’, 1, “etat2”)]}
    # “etat2” : {{‘s’ : " T'es pas mal aujourd'hui ! [(‘time’, 1, “choice”)}]
    # {‘s’ :"Tu sais quoi je te propose un jeu, juste place-toi quelque part au hasard !”
    # "e" : “Afraid” Arrête, je suis un peu timide !}
    'human_0_center_1m' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Salut comment tu vas ??'
        },
        [
            ('time', 1, 'human_0_center_1m_2')
        ]
    ),
    'human_0_center_1m_2' : (
        {
            'e' : '',
            'g' : '',
            's' : 'T\'es pas mal aujourd\'hui !'
        },
        [
            ('time', 1, 'human_0_center_1m_3')
        ]
    ),
    'human_0_center_1m_3' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Tu sais quoi je te propose un jeu, juste place-toi quelque part au hasard !'
        },
        [
            ('time', 1, 'human_0_center_1m_4')
        ]
    ),
    'human_0_center_1m_4' : (
        {
            'g' : '',
            'e' : 'QT/afraid',
            's' : 'Arrête, je suis un peu timide !'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    # 1MG = à 1 mètre, à la gauche de QT 
    # {‘s’ : “\pau=300\ J'ai envie de te contempler. D'ailleurs tu me fais
    # rougir !”, “e” : kiss, “g” : kiss, “s” : Dis-moi, est-ce que je te
    # plais ?}  (expression de séduction, cligner des yeux)
    # {‘s’ : “Va gauchement à droite ou (pause 1 seconde) adroitement à gauche,
    # (pause 1 sec) fin (pause 1 seconde) comme tu veux !”}
    'human_0_left_1m' : (
        {
            'e' : 'QT/kiss',
            'g' : 'QT/kiss',
            's' : '\\pau=300\\ J\'ai envie de te contempler. D\'ailleurs tu me fais rougir !'
        },
        [
            ('time', 1, 'human_0_left_1m_2')
        ]
    ),
    'human_0_left_1m_2' : (
        {
            'e' : 'QT/one_eye_wink',
            'g' : 'QT/shy',
            's' : 'Dis-moi, est-ce que je te plais ?'
        },
        [
            ('time', 1, 'human_0_left_1m_3')
        ]
    ),
    'human_0_left_1m_3' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Va gauchement à droite ou \\pau=1000\\ adroitement à gauche, \\pau=1000\\ fin \\pau=1000\\ comme tu veux !'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    # 2MG = à 2 mètres gauche 
    # {‘s’ :Waouuuuh!  vraiment faut que je te le dise tu es vraiment
    # (pause 2 sec) incroyable !!!!! 
    # \rmw=0\ qu'est ce qu'on fait ensemble maintenant ? 
    # "e" : happy: "g" : happy :  Mais que fais-tu aussi loin ?\pau=300\
    # approche que je te vois plus !  
    # \vce=speaker=Will\  tu me plais.}
    # {'s' :"g" : sad : Tu crois qu'on pourrait rester ensemble pour l'éternité
    # ? Mais nous sommes tellement différents. Tu es un humain et moi je
    # suis...moi !}
    'human_0_left_2m' : (
        {
            'e' : '',
            'g' : '',
            's' : 'Waouuuuh! Vraiment faut que je te le dise tu es vraiment \\pau=2000\\ incroyable ! \\rmw=0\\ qu\'est ce qu\'on fait ensemble maintenant ?' # TODO : volume up
        },
        [
            ('time', 1, 'human_0_left_2m_2')
        ]
    ),
    'human_0_left_2m_2' : (
        {
            'e' : 'QT/happy',
            'g' : 'QT/happy',
            's' : 'Mais que fais-tu aussi loin ?\\pau=300\\ Approche que je te vois plus ! \\vce=speaker=Will\\  tu me plais.' # TODO tester si vce fonctionne correctement
        },
        [
            ('time', 1, 'human_0_left_2m_3')
        ]
    ),
    'human_0_left_2m_3' : (
        {
            'e' : 'QT/sad',
            'g' : 'QT/sad',
            's' : 'Tu crois qu\'on pourrait rester ensemble pour l\'éternité ? Mais nous sommes tellement différents. Tu es un humain et moi je suis...moi !'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    # 2MD = à 2 mètres droite
    # {‘s’ : “\pau=300\ "e" : cry: "g" : sad : je t’aime mais je dois te
    # quitter, adieu !}
    'human_0_right_2m' : (
        {
            'e' : 'QT/cry',
            'g' : 'QT/sad',
            's' : "\\pau=300\\Je t’aime mais je dois te quitter, adieu !"
        },
        [
            ('time', 1, 'choice')
        ]
    )
}