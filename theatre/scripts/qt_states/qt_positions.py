states = {
    # 1MF =  à 1 mètre, face à QT
    # “etat1” : {{‘s’ : “Pas si près, je ne peux pas respirer.”}, [(‘time’, 1, “etat2”)]}
    # {‘s’ : “On dirait que vous les humains n'avez jamais entendu parler d'intimité !”}
    # {‘g’ : ”angry”, ‘e’ : “angry”, ‘s’ : “Recule, tu pues !”}
    # “afraid” Arrête, je suis un peu timide ! 
    'human_0_center_1m' : (
        {
            'e' : 'QT/breathing_exercise',
            'g' : 'QT/disgusted',
            's' : 'Pas si près, je ne peux pas respirer.'
        },
        [
            ('time', 5, 'choice')
        ]
    ),

    # 1MG = à 1 mètre, à la gauche de QT 
    # {‘s’ : “\pau=300\ J'ai envie de te contempler. D'ailleurs tu me fais rougir !”, “e” : kiss, “g” : kiss, “s” : Dis-moi, est-ce que je te plais ?} 
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
            ('time', 5, 'choice')
        ]
    ),

    # 1MD = à 1 mètre, à la gaucΑ1MF de QT
    # Je n’ai pas d’ami….Dis-moi, est-ce que je te plais ?} 
    # {‘s’: ‘g’: “angry”,  ‘e’: “angry”, ‘s’:“\vct=60\ Ouste!\sel=alt\” }
    # {‘s’: ‘g’: “angry”,  ‘e’: “angry”, ‘s’:“\vct=120\ Tu es super \sel=alt\ collant!”} 
    # {‘s’: ‘g’: “afraid”,  ‘e’: “afraid”, ‘s’: “\vct=90\ Pas si près, je suis claustrophobe!”} 
    # Encore dix centimètres, halte, pas douze!
    # “angry” \pau=300\C’est beaucoup, hum ?
    'human_0_right_1m' : (
        {
            'e' : 'QT/shy',
            'g' : 'QT/shy',
            's' : 'Je n’ai pas d’ami\\pau=300\\ Je n’ai pas d’ami\\pau=300\\ Je n’ai pas d’ami\\pau=300\\ .Dis-moi, est-ce que je te plais ?'
        },
        [
            ('time', 5, 'choice')
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
            ('time', 5, 'choice')
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
            ('time', 5, 'choice')
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
            ('time', 5, 'choice')
        ]
    ),


    # 2MF = à 2 mètres face.
    # n’importe quoi! \pau=300\
    # La vie est belle ! \aud=“pathway+filename”\
    # Sans toi ça sera mieux! 
    # #LAUGH01# J'ai faim \aud=“pathway+filename”\ .
    # {‘g’ : « joie », ‘e’ : « joie », ‘s’ : « Youuuhouuu ! Enfin tranquille !! »}
    # Va-t’en! Lache, je n’ai pas besoin de toi!
    # { 's' : "#SNEEZE01# Pardon, je suis malade !" }
    # “kiss”  #SNEEZE01#Quels beaux tous les gens! Je suis enchanté !


}
