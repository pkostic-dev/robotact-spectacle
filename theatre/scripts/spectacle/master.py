# These states manage switching between different scenes

#! xrandr -o normal
#! Windows + O

states = {
    'begin': ({}, [('time', 1, 'choice')]),
    'end': ({}, [('time', 0.1, 'end')]) ,

    'choice_main': (
        {'g': '', 's': '' },
        [
            ('key', '(', 'scene_5'),
            ('key', "è", 'scene_7'),
            ('key', '_', 'scene_8'),
            ('key', 'ç', 'scene_9'),
            ('key', 'à', 'scene_10'),
            ('key', 'a', 'scene_11'),
            ('key', 'z', 'scene_12'),
            ('key', 'f', 'scene_fin'),

            ('key', '*', 'end'),

            # TEST
            ('key', 't', 'talk_en'),
            ('key', 'T', 'talk_it'),
            ('key', 'e', 'english'),
            ('key', 'i', 'italian'),
            ('key', 's', 'stop_speech'),
        ]
    ),

    # TEST

    'talk_en': (
        {
            's': 'Hello, my name is QT Robot!'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'talk_it': (
        {
            's': 'Ancora due minuti, ho quasi finito il livello!'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'stop_speech': (
        {
            's': '/stop'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'italian': (
        {
            's': '/italian'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),

    'english': (
        {
            's': '/english'
        },
        [
            ('time', 0.1, 'choice')
        ]
    ),
}