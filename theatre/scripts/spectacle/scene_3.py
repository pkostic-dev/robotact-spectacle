######################################################## SCENE 3 #######################################################

####################################################### SCRAPPED #######################################################

# Robot 1 : Un homme
# Robot 2 : ça resent par exemple de la joie
# Robot 1 : ça joue du violon
# Robot 2 : ça a envie de se promener
# Robot 1 : ça fait du théâtre
# Robot 2 : Bref, tant de choses
# Robot 1 : Qui sont, au fond
# Robot 2 : Inutiles

robot1_states = {
    'r1': (
        {
            's': 'Un homme..'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'r2': (
        {
            's': 'ça joue du violon..'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'r3': (
        {
            's': 'ça fait du théâtre..'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'r4': (
        {
            's': 'Qui sont, au fond..'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 'r1'),
            ('key', 'é', 'r2'),
            ('key', '"', 'r3'),
            ('key', "'", 'r4'),
        ]
    ),
}

robot2_states = {
    'r1': (
        {
            's': 'ça resent par exemple de la joie..'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'r2': (
        {
            's': 'ça a envie de se promener..'
        },
        [
            ('time', 1, 'choice')
        ]
    ),
    
    'r3': (
        {
            's': 'Bref, tant de choses..'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'r4': (
        {
            's': 'Inutiles.'
        },
        [
            ('time', 1, 'choice')
        ]
    ),

    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]) ,

    'choice': (
        {'g': '', 's': '' },
        [
            ('key', '&', 'r1'),
            ('key', 'é', 'r2'),
            ('key', '"', 'r3'),
            ('key', "'", 'r4'),
        ]
    ),
}
