# Configuration

# Le temps à laiser à l'enfant de se déplacer, en secondes
TEMPS_ENFANT = 10

# QT Look
look_up = [0.0,-20.0]
look_center = [0.0,0.0]
look_down = [0.0,+10.0]
look_right = [-20.0,0.0]
look_left = [+20.0,0.0]
look_up_right = [-20.0,-20.0]
look_up_left = [+20.0,-20.0]
look_down_right = [-10.0,+10.0]
look_down_left = [+10.0,+10.0]
look_up_short = [0.0,-10.0]
look_down_short = [0.0,+5.0]
look_right_short = [-10.0,0.0]
look_left_short = [+10.0,0.0]

'''
    ROBOT
      O
     / \ 
    /   \     
   /     \ 

+---+---+---+
| T | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 | GRID
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+

     \ /
      o
    CHILD

T = Treasure
'''

tresor = {
    'tile_1' : (
        {
            'e' : 'QT/happy',
            'g' : '',
            'h' : look_right,
            's' : 'Bravo ! Tu as trouve le tresor !'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

    'tile_2' : (
        {
            'e' : 'QT/surprise',
            'g' : '',
            'h' : look_center,
            's' : 'Le trésor se trouve juste à ta gauche !'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

    'tile_2' : (
        {
            'e' : 'QT/confused',
            'g' : '',
            'h' : look_left,
            's' : 'Je pense que le trésor est plus à ta gauche !'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

    'tile_4' : (
        {
            'e' : 'QT/surprise',
            'g' : '',
            'h' : look_left_short,
            's' : 'Le trésor se trouve juste devant toi !'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

    'tile_5' : (
        {
            'e' : 'QT/confused',
            'g' : '',
            'h' : look_center,
            's' : 'Avance un peu plus en avant !'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

    'tile_6' : (
        {
            'e' : 'QT/confused',
            'g' : '',
            'h' : look_right_short,
            's' : 'Et si on cherchait plutôt à gauche ?'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

    'tile_7' : (
        {
            'e' : 'QT/surprise',
            'g' : '',
            'h' : look_left_short,
            's' : 'Je pense que tu trouveras le trésor si tu avances tout droit !'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

    'tile_8' : (
        {
            'e' : 'QT/confused',
            'g' : '',
            'h' : look_center,
            's' : 'Je pense qu\'on est perdu, et si on cherchait plus en avant ?'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

    'tile_9' : (
        {
            'e' : 'QT/confused',
            'g' : '',
            'h' : look_right_short,
            's' : 'Je pense qu\'on est perdu, et si on cherchait plus à gauche ?'
        },
        [
            ('time', TEMPS_ENFANT, 'treasure_game_1')
        ]
    ),

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
            ('key', 'r', 'reset_posture'),
            ('key', '*', 'end'),

            ('key', 'g', 'treasure_game_1'),
        ]
    ),

    'treasure_game_1' : (
        {
            'e' : '',
            'g' : '',
            's' : '' 
        },
        [
            ('gesture', 'tile_1', 'tile_1'),
            ('gesture', 'tile_2', 'tile_2'),
            ('gesture', 'tile_3', 'tile_3'),
            ('gesture', 'tile_4', 'tile_4'),
            ('gesture', 'tile_5', 'tile_5'),
            ('gesture', 'tile_6', 'tile_6'),
            ('gesture', 'tile_7', 'tile_7'),
            ('gesture', 'tile_8', 'tile_8'),
            ('gesture', 'tile_9', 'tile_9'),

            ('key', '1', 'tile_1'),
            ('key', '2', 'tile_2'),
            ('key', '3', 'tile_3'),
            ('key', '4', 'tile_4'),
            ('key', '5', 'tile_5'),
            ('key', '6', 'tile_6'),
            ('key', '7', 'tile_7'),
            ('key', '8', 'tile_8'),
            ('key', '9', 'tile_9'),

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