states = {
    'begin': ({}, [('time', 1, 'choice')]),

    #### HANDS ####
    'point_la': (
        {
            'la': [-0.5, 0, 0, 0, 0, 1]
        }, [('time', 0.1, 'choice')]
    ),
    'point_ra': (
        {
            'ra': [-0.5, 0, 0, 0, 0, 1]
        }, [('time', 0.1, 'choice')]
    ),
    'up_la': (
        {
            'la': [-1, 0, 0, 0, 0, 1]
        }, [('time', 0.1, 'choice')]
    ),
    'up_ra': (
        {
            'ra': [-1, 0, 0, 0, 0, 1]
        }, [('time', 0.1, 'choice')]
    ),
    'hands_up': (
        {
            'la': [-1, 0, 0, 0, 0, 1],
            'ra': [-1, 0, 0, 0, 0, 1],
        }, [('time', 0.1, 'choice')]
    ),
    't_pose': (
        {
            'la': [0, 1, 0, 0, 0, 1],
            'ra': [0, -1, 0, 0, 0, 1]
        }, [('time', 0.1, 'choice')]
    ),


    'walk_fwd': ( {'w': [1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'stop': ( {'w': [0,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'walk_back': ( {'w': [-1,0,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'strife_left': ( {'w': [0,1,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'strife_right': ( {'w': [0,-1,0,0,0,0]}, [('time', 0.1, 'choice')]),
    'rotate_left': ( {'w': [0,0,0,0,0,1]}, [('time', 0.1, 'choice')]),
    'rotate_right': ( {'w': [0,0,0,0,0,-1]}, [('time', 0.1, 'choice')]),

    #### LOOK ####
    'look_up': (
        {
            'h': [0, -1],
        }, [('time', 0.1, 'choice')]),
    'look_center': (
        {
            'h': [0, 0],
        }, [('time', 0.1, 'choice')]),
    'look_down': (
        {
            'h': [0, 1],
        }, [('time', 0.1, 'choice')]),
    'look_right': (
        {
            'h': [-2, 0],
        }, [('time', 0.1, 'choice')]),
    'look_left': (
        {
            'h': [2, 0],
        }, [('time', 0.1, 'choice')]),
    'look_up_right': (
        {
            'h': [-0.5, -0.5],
        }, [('time', 0.1, 'choice')]),
    'look_up_left': (
        {
            'h': [0.5, -0.5],
        }, [('time', 0.1, 'choice')]),
    'look_down_right': (
        {
            'h': [-0.5, 0.5],
        }, [('time', 0.1, 'choice')]),
    'look_down_left': (
        {
            'h': [0.5, 0.5],
        }, [('time', 0.1, 'choice')]),

    # Look 180
    'look_left_180': (
        {
            'h': [1.5, 0],
        }, [('time', 0.1, 'choice')]),
    'look_right_180': (
        {
            'h': [-1.5, 0],
        }, [('time', 0.1, 'choice')]),
    'look_up_left_180': (
        {
            'h': [1.5, -2.0],
        }, [('time', 0.1, 'choice')]),
    'look_up_right_180': (
        {
            'h': [-1.5, -2.0],
        }, [('time', 0.1, 'choice')]),

    #### GESTURES ####
    'kisses': ({'g':'kiss'}, [('time', 3, 'choice')]),

    'jessaie': ( {'g': '', 's': 'J\'essaie!'}, [('time', 3, 'choice')]),
    'dontknow': ( {'g': 'dontknow', 's': 'Je ne sais pas!'}, [('time', 3, 'choice')]),
    'oui': ( {'g': 'oui', 's': 'Oui!'}, [('time', 3, 'choice')]),
    'non': ( {'g': 'non', 's': 'Non!'}, [('time', 3, 'choice')]),

    'sad': ( {'g': 'sad', 's': ''}, [('time', 3, 'choice')]),
    'kiss': ( {'g':'kiss', 's': ''}, [('time', 3, 'choice')]),
    'excited': ( {'g':'excited', 's': ''}, [('time', 3, 'choice')]),
    'thinking': ( {'g':'thinking', 's': ''}, [('time', 3, 'choice')]),
    'curious': ( {'g':'curious', 's': ''}, [('time', 3, 'choice')]),
    'fear': ( {'g':'fear', 's': ''}, [('time', 3, 'choice')]),
    'okey': ( {'g': 'confused', 's': ''}, [('time', 3, 'choice')]),

    'nao_1': ( {'g': '', 's': 'On a bien compris'}, [('time', 3, 'choice')]),
    'nao_2': ( {'g': '', 's': 'Un homme, ça ressent par exemple de la joie'}, [('time', 3, 'choice')]),
    'nao_3': ( {'g': '', 's': 'ça a envie de se promener'}, [('time', 3, 'choice')]),
    'nao_4': ( {'g': '', 's': 'qui sont, au fond, inutiles. \\pau=400\\ Alors les hommes, \\pau=200\\ vous'}, [('time', 3, 'choice')]),
    'nao_5': ( {'g': '', 's': 'vous êtes inutiles.'}, [('time', 3, 'choice')]),
    
    'qt_1': ( {'g': '', 's': 'Vous avez raison'}, [('time', 3, 'choice')]),
    'qt_2': ( {'g': '', 's': 'ça joue du violon, ça joue du theâtre'}, [('time', 3, 'choice')]),
    'qt_3': ( {'g': '', 's': 'bref tant de choses'}, [('time', 3, 'choice')]),

    'tai_chi_A':( {'g':'tai_chi_A'}, [('time', 0.1, 'choice')]),
    'tai_chi_B':( {'g':'tai_chi_B'}, [('time', 0.1, 'choice')]),
    'tai_chi_C':( {'g':'tai_chi_C'}, [('time', 0.1, 'choice')]),

    'gorilla':( {'g':'gorilla'}, [('time', 0.1, 'choice')]),
}