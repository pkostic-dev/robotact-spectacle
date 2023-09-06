# These states manage switching between different scenes

states = {
    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 'scene_1'),
            ('key', '"', 'scene_3'),
            ('key', '(', 'scene_5'),
            ('key', "è", 'scene_7'),
            ('key', '_', 'scene_8'),
            ('key', 'ç', 'scene_9'),
            ('key', 'à', 'scene_10'),
            ('key', 'a', 'scene_11'),
            ('key', 'z', 'scene_12'),
            ('key', 'f', 'scene_fin'),
        ]
    ),

    'scene_1' : (
        
    )
}