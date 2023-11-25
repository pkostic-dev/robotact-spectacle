######################################################## SCENE 6 #######################################################

# QT -> DIALOGUE, HEAD, ?
# NAO -> DEAD

# SCÈNE 6 : “La première rencontre” (acteurs + QT et NAO) 

'''
Andrea: Coucou! Tu m'écoutes ? Tu peux me voir ?
Elle tourne autour de QT pour s’assurer qu’il la voit vraiment:  
Tu sais qu’on va travailler ensemble ?
#! Réponse de QT [b] Biensur
#? Sarah entre côté J.
Sarah: Après avoir observé un instant QT: Tu as vu qu’il a aussi des capteurs ? Il peut nous entendre. Tu peux nous entendre QT ?
#! Réponse de QT [O] Mais Oui
Andrea- Très bien, QT, je te présente Sarah
#! Réponse de QT [m] Enchanté [h] Salut [H] Ca va
#? Jérémy entre côté J.
Jeremy - Il nous voit, il nous écoute… c’est génial! Et il peut parler plusieurs langues ?
Andrea-  Peux-tu parler plusieurs langues, QT ?
#! Réponse de QT [p] Peut-être
Sarah - Et mettre de la musique
Jérémy - Il peut mettre de la musique ?
Sarah - Je crois
Andrea - QT! Peux-tu mettre de la musique ?
#! Réponse de QT [n] Non
Jérémy -  Pourquoi fais-tu des réponses si courtes? Tout à l’heure tu faisais des phrases longues, des phrases 
          complexes… tu parlais mieux!
#? PREDRAG : Oui, mais tout à l'heure il parlait grâce à ChatGPT.
Sarah - Mais là aussi il dit des phrases!
Andrea acquiesce
Jérémy: Oui, je veux dire des phrases longues, des phrases complexes… il parlait mieux! Grâce à ChatGpt il pourrait créer des dialogues avec nous !
Andrea- Mais est-ce qu’il peut marcher ? Il a les pieds unis, comme… comme un tronc!
Jérémy - QT! Est-ce que tu peux marcher ?
#! Réponse de QT [U] Peux pas
Sarah - Et tu as toujours besoin d’être branché pour fonctionner  ?
#! Réponse de QT [t] Toujours
Sarah - Il est vraiment mignon!
Andrea - Et tu as déjà travaillé avec des comédiens ? Je n’ai jamais travaillé avec des robots
#! Réponse de QT [K] Pourquoi
Sarah - T’es content, QT ? Nous allons faire du théâtre ensemble!
#! Réponse de QT [y] Super
#? Filippo entre sur scène, l’air sceptique.
Filippo - Théâtre, théâtre, mais quel théâtre!!! Il parle comme un bébé….
Andrea, Jeremy et Sarah défendent QT en parlant tous ensemble: mais non… pas du tout… toujours gâche-fête
Filippo-  À la limite je préfère l’autre
Andréa- Qui, Nao ?
Filippo - Oui, le petit
Sarah - Tu as entendu, QT ? Filippo préfère Nao
#! Réponse de QT [l] Quoi
Jeremy - QT! Crois-tu que Nao est meilleur acteur que tu ne l’es ?
#! Réponse de QT [B] Biensur que non
#? Débat. Jalousie de QT……………………………………………………….
Filippo - Quoiqu’il en pense notre bébé-là….
Andrea -Il s’appelle QT!
#! Réponse de QT [j] Je sais
Filippo - Quoiqu’il en pense QT… je préfère l’autre, au moins il peut bouger.
#? Les autres se serrent autour de Nao: c’est vrai qu’il n’est pas mal… il bouge… oui peut-être
Sarah - Il pourrait danser. Je crois qu’il serait un excellent danseur.
Filippo - Il ne manquerait plus que ça! Avec tous les excellents danseurs qui sont au chômage… on va embaucher un robot!
Jérémy - Mais il pourrait les remplacer! Quand ils sont malades ou blessés…
Filippo - Toujours sceptique. Bien sûr, bien sûr… ce serait le début de la fin
Andrea - Moi je crois qu’il pourrait être aussi un excellent comédien. Tu sais qu’il peut jouer en plusieurs langues ?
Sarah -Il pourrait jouer Molière en français, Shakespeare en anglais, Garcia Lorca en espagnol…
#? Les autres acquiescent
Jérémy - Super!
Filippo - Le théâtre n’est pas un cours de langue. Il peut jouer dans toutes les langues de l’univers, mais est-ce qu’il saurait donner des couleurs à ses répliques ? Saurait-il jouer une réplique tragique avec une touche comique ? Ralentir, accélérer, jouer contre le sens du texte …
Sarah - Qui sait
Jérémy - Peut-être
Andrea- Avec le temps…
#? Un temps bref
Andrea - Dans tous les cas, il a de très beaux haut-parleurs…
Jérémy et Sarah en caressant les hauts-parleurs : C’est vrai… en effet… ils sont magnifiques
Filippo - Vous êtes incroyables! Est-ce qu’il doit faire l’acteur ou servir d’enceinte ? Parce que si c’est pour écouter de la musique, aucun souci, je l’installe avec plaisir dans mon salon. J’ai une étagère libre.   
Jérémy - Prenant Nao dans ses bras. Moi je l’aime bien!
Andrea et Sarah se serrent autour de Nao et le caressent : Moi aussi… il est tellement beau… il sera un grand comédien
Filippo continue de faire la gueule. Andrea, Jérémy et Sarah soulèvent Nao au bout de leurs bras ne cessant de l’exalter. 
Filippo - Vous êtes fous! Il n’est qu’un morceau de plastique avec une voix enregistrée! Aparté Ils ont perdu la tête.   
Andrea, Jérémy et Sarah tournent Nao vers Filippo et commencent à scander son nom: Nao! Nao! Nao!

'''


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
            #('key', 'r', 'rien'),     ('key', 'R', 'bien'),
            #('key', 't', 'toujours'), ('key', 'T', 'tout'),
            #('key', 'y', 'super'),    ('key', 'Y', 'et_toi'),
            #('key', 'u', 'peux'),     ('key', 'U', 'peuxpas'),
            #('key', 'i', 'de_rien'),  ('key', 'I', 'plaisir'),
            #('key', 'o', 'oui'),      ('key', 'O', 'mais_oui'),
            #('key', 'p', 'peutetre'), ('key', 'P', 'parfois'),

            #('key', 'f', 'fort'),     ('key', 'F', 'faible'),
            #('key', 'g', 'daccord'),  ('key', 'G', 'pas_daccord'),
            #('key', 'h', 'salut'),    ('key', 'H', 'cava'),
            #('key', 'k', 'quand'),    ('key', 'K', 'pourquoi'),
            #('key', 'j', 'sais'),     ('key', 'J', 'saispas'),
            #('key', 'l', 'quoi'),     ('key', 'L', 'qui'),
            #('key', 'm', 'enchante'), ('key', 'M', 'au_revoir'),

            #('key', 'v', 'pardon'),   ('key', 'V', 'merci'),
            #('key', 'b', 'biensur'),  ('key', 'B', 'biensur_non'),
            #('key', 'n', 'non'),      ('key', 'N', 'mais_non'),
            
            ('key', 'o', 'of_course'), 
            ('key', 't', 'nice_to'), 
            ('key', 'y', 'yes'),
            ('key', 'n', 'no'),
            ('key', 'm', 'maybe'),
            ('key', 'g', 'great'),
            ('key', 'N', 'no_no_no'),

            
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

    # QT simple replies UNSCRIPTED
    # 'salut': ( {'e':'QT/talking', 'g': '', 's': 'Hi!'}, [('time', 0.1, 'choice')]),
    # 'sais': ( {'e':'QT/talking', 'g': '', 's': 'I know'}, [('time', 0.1, 'choice')]),
    # 'saispas': ( {'e':'QT/talking', 'g': '', 's': 'I don\'t know'}, [('time', 0.1, 'choice')]),
    # 'oui': ( {'e':'QT/talking', 'g': '', 's': 'Yes !'}, [('time', 0.1, 'choice')]),
    # 'mais_oui': ( {'e':'QT/talking', 'g': '', 's': 'Oh yeah !'}, [('time', 0.1, 'choice')]),
    # 'non': ( {'e':'QT/talking', 'g': '', 's': 'No !'}, [('time', 0.1, 'choice')]),
    # 'mais_non': ( {'e':'QT/talking', 'g': '', 's': 'Not at all !'}, [('time', 0.1, 'choice')]),
    # 'biensur': ( {'e':'QT/talking', 'g': '', 's': 'Yes, of course !'}, [('time', 0.1, 'choice')]),
    # 'biensur_non': ( {'e':'QT/talking', 'g': '', 's': 'Of course not !'}, [('time', 0.1, 'choice')]),
    # 'rien': ( {'e':'QT/talking', 'g': '', 's': 'It\'s nothing.'}, [('time', 0.1, 'choice')]),
    # 'tout': ( {'e':'QT/talking', 'g': '', 's': 'It\'s everything !'}, [('time', 0.1, 'choice')]),
    # 'super': ( {'e':'QT/talking', 'g': '', 's': 'Great !'}, [('time', 0.1, 'choice')]),
    # 'peux': ( {'e':'QT/one_eye_wink', 'g': '', 's': 'I can'}, [('time', 0.1, 'choice')]),
    # 'peuxpas': ( {'e':'QT/sad', 'g': '', 's': 'I cannot'}, [('time', 0.1, 'choice')]),
    # 'toujours': ( {'e':'QT/talking', 'g': '', 's': 'Always'}, [('time', 0.1, 'choice')]),
    # 'peutetre': ( {'e':'QT/talking', 'g': '', 's': 'Maybe'}, [('time', 0.1, 'choice')]),
    # 'parfois': ( {'e':'QT/talking', 'g': '', 's': 'Sometimes'}, [('time', 0.1, 'choice')]),
    # 'qui': ( {'e': 'QT/confused', 'g': '', 's': 'Who ?'}, [('time', 0.1, 'choice')]),
    # 'quand': ( {'e': 'QT/confused', 'g': '', 's': 'When ?'}, [('time', 0.1, 'choice')]),
    # 'quoi': ( {'e': 'QT/confused', 'g': '', 's': 'What ?'}, [('time', 0.1, 'choice')]),
    # 'pourquoi': ( {'e': 'QT/confused', 'g': '', 's': 'Why ?'}, [('time', 0.1, 'choice')]),
    # 'cava': ( {'e':'QT/talking', 'g': '', 's': 'How are you ?'}, [('time', 0.1, 'choice')]),
    # 'et_toi': ( {'e':'QT/talking', 'g': '', 's': 'And you ?'}, [('time', 0.1, 'choice')]),
    # 'fort': ( {'e':'QT/one_eye_wink', 'g': '', 's': 'Strong !'}, [('time', 0.1, 'choice')]),
    # 'faible': ( {'e':'QT/sad', 'g': '', 's': 'Weak !'}, [('time', 0.1, 'choice')]),
    # 'bien': ( {'e':'QT/happy', 'g': '', 's': 'Good !'}, [('time', 0.1, 'choice')]),
    # 'daccord': ( {'e':'QT/happy', 'g': '', 's': 'I agree !'}, [('time', 0.1, 'choice')]),
    # 'pas_daccord': ( {'e':'QT/sad', 'g': '', 's': 'I don\'t agree !'}, [('time', 0.1, 'choice')]),
    # 'pardon': ( {'e':'QT/talking', 'g': '', 's': 'Sorry.'}, [('time', 0.1, 'choice')]),
    # 'merci': ( {'e':'QT/talking', 'g': '', 's': 'Thank you !'}, [('time', 0.1, 'choice')]),
    # 'enchante': ( {'e':'QT/happy', 'g': '', 's': 'My pleasure !'}, [('time', 0.1, 'choice')]),
    # 'au_revoir': ( {'e':'QT/talking', 'g': '', 's': 'Bye !'}, [('time', 0.1, 'choice')]),
    # 'de_rien': ( {'e':'QT/talking', 'g': '', 's': 'It\'s ok !'}, [('time', 0.1, 'choice')]),
    # 'plaisir': ( {'e':'QT/happy', 'g': '', 's': 'With pleasure'}, [('time', 0.1, 'choice')]),

    # QT simple replies SCRIPTED
    'of_course': ( {'e':'QT/talking', 'g': '', 's': 'Of course!'}, [('time', 0.1, 'choice')]),
    'nice_to': ( {'e':'QT/talking', 'g': '', 's': 'Nice to meet you.'}, [('time', 0.1, 'choice')]),
    'yes': ( {'e':'QT/talking', 'g': '', 's': 'Yes!'}, [('time', 0.1, 'choice')]),
    'maybe': ( {'e':'QT/talking', 'g': '', 's': 'Maybe'}, [('time', 0.1, 'choice')]),
    'no': ( {'e':'QT/talking', 'g': '', 's': 'No'}, [('time', 0.1, 'choice')]),
    'great': ( {'e':'QT/talking', 'g': '', 's': 'Great!'}, [('time', 0.1, 'choice')]),
    'no_no_no': ( {'e':'QT/talking', 'g': '', 's': 'No no no.'}, [('time', 0.1, 'choice')]),

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