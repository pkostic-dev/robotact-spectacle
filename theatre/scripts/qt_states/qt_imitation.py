"""
Poses :
 - tpose : arms are extended to the sides
 - relaxed : arms are relaxed, extended down
 - hips : hands are on the hips
 - touching : hands touch
 - heart : one hand is on the heart
 - egyptian : arms are bent at the elbow at 90°, mirroring at the x and y axis
 - up : arms are extended up
 - robot : arms are bent at the elbow at 90° rotated downwards
 - mime : idem, rotated upwards

Prefix :
 - la : left arm
 - ra : right arm

rostopic echo /qt_robot/joints/state

name: [HeadPitch, HeadYaw,
       LeftElbowRoll, LeftShoulderPitch, LeftShoulderRoll,
       RightElbowRoll, RightShoulderPitch, RightShoulderRoll]
position: [1.899999976158142, 0.0,
           -34.5, 89.9000015258789, -58.0,
           -34.79999923706055, -89.9000015258789, -59.29999923706055]

rostopic pub /qt_robot/left_arm_position/command std_msgs/Float64MultiArray "layout:
  dim:
  - label: ''
    size: 0
    stride: 0
  data_offset: 0
data: [LeftShoulderPitch, LeftShoulderRoll, LeftElbowRoll]"

ShoulderPitch : 
negative - internal rotation
positive - external rotation

ShoulderRoll :
negative - internal
positive - external

ElboxRoll :
negative - internal
positive - external

"""

head_poses = {
    'look_front' : [0.0, 0.0],
    'look_left' : [20.0, 0.0],
}

arm_poses = {
    'straight' : [0.0, 0.0, 0.0],
    'la_relaxed' : [89.9, -58.0, -34.5],
    'ra_relaxed' : [-89.9, -59.3, -34.8],
    'la_hip' : [],
    'ra_hip' : [],
    'la_touching' : [],
    'ra_touching' : [],
    'la_heart' : [],
    'la_lateral' : [], # rotation end position
    'ra_lateral' : [],
    'la_medial' : [], # rotation end position
    'ra_medial' : [],
    'la_up' : [],
    'ra_up' : [],
}

poses = {
    'tpose': {
        'la' : arm_poses['straight'],
        'ra' : arm_poses['straight'],
    },
    'relaxed': {
        'la' : arm_poses['la_relaxed'],
        'ra' : arm_poses['ra_relaxed'],
        'h' : head_poses['look_front'],
    },
    'hips': {
        'la' : arm_poses['la_hip'],
        'ra' : arm_poses['ra_hip'],
    },
    'touching': {
        'la' : arm_poses['la_touching'],
        'ra' : arm_poses['ra_touching'],
    },
    'heart': {
        'la' : arm_poses['la_heart'],
        'ra' : arm_poses['ra_relaxed'],
    },
    'egyptian': {
        'la' : arm_poses['la_lateral'],
        'ra' : arm_poses['ra_medial'],
        'h' : head_poses['look_left'],
    },
    'up': {
        'la' : arm_poses['la_up'],
        'ra' : arm_poses['ra_up'],
    },
    'robot': {
        'la' : arm_poses['la_medial'],
        'ra' : arm_poses['ra_medial'],
    },
    'mime': {
        'la' : arm_poses['la_lateral'],
        'ra' : arm_poses['ra_lateral'],
    },
}

states = {
    'begin': ({}, [('time', 1, 'choice')]),
    'end': ((), [('time', 0.1, 'end')]),

    'choice': (
        {'g': '', 's': '' }, 
        [
            # Commands
            ('key', 'i', 'imitate'),
            ('key', 'e', 'end'),
            
            # Poses
            ('key', '&', 'do_tpose'),
            ('key', 'é', 'do_relaxed'),
            ('key', '"', 'do_hips'),
            ('key', "'", 'do_touching'),
            ('key', '(', 'do_heart'),
            ('key', '-', 'do_egyptian'),
            ('key', 'è', 'do_up'),
            ('key', '_', 'do_robot'),
            ('key', 'ç', 'do_mime'),
        ]
    ),
    'imitate': (
        {},
        [
            # Commands
            ('key', 'c', 'choice'),
            ('key', 'e', 'end'),

            # Poses
            ('gesture', 'tpose',    'imitate_tpose'),
            ('gesture', 'relaxed',  'imitate_relaxed'),
            ('gesture', 'hips',     'imitate_hips'),
            ('gesture', 'touching', 'imitate_touching'),
            ('gesture', 'heart',    'imitate_heart'),
            ('gesture', 'egyptian', 'imitate_egyptian'),
            ('gesture', 'up',       'imitate_up'),
            ('gesture', 'robot',    'imitate_robot'),
            ('gesture', 'mime',     'imitate_mime'),

        ]
    ),

    # IMITATE POSE
    'imitate_tpose': (
        poses['tpose'],
        [('time', 1, 'done_imitating')]
    ),
    'imitate_relaxed': (
        poses['relaxed'],
        [('time', 1, 'done_imitating')]
    ),
    'imitate_hips': (
        poses['hips'],
        [('time', 1, 'done_imitating')]
    ),
    'imitate_touching': (
        poses['touching'],
        [('time', 1, 'done_imitating')]
    ),
    'imitate_heart': (
        poses['heart'],
        [('time', 1, 'done_imitating')]
    ),
    'imitate_egyptian': (
        poses['egyptian'],
        [('time', 1, 'done_imitating')]
    ),
    'imitate_up': (
        poses['up'],
        [('time', 1, 'done_imitating')]
    ),
    'imitate_robot': (
        poses['robot'],
        [('time', 1, 'done_imitating')]
    ),
    'imitate_mime': (
        poses['mime'],
        [('time', 1, 'done_imitating')]
    ),

    'done_imitating': (
        {
            's': "Est-ce que je le fais bien ?"
        },
        [('time', 1, 'imitate')]
    ),

    # DO POSE
    'do_tpose': (
        poses['tpose'],
        [('time', 1, 'done_posing')]
    ),
    'do_relaxed': (
        poses['relaxed'],
        [('time', 1, 'done_posing')]
    ),
    'do_hips': (
        poses['hips'],
        [('time', 1, 'done_posing')]
    ),
    'do_touching': (
        poses['touching'],
        [('time', 1, 'done_posing')]
    ),
    'do_heart': (
        poses['heart'],
        [('time', 1, 'done_posing')]
    ),
    'do_egyptian': (
        poses['egyptian'],
        [('time', 1, 'done_posing')]
    ),
    'do_up': (
        poses['up'],
        [('time', 1, 'done_posing')]
    ),
    'do_robot': (
        poses['robot'],
        [('time', 1, 'done_posing')]
    ),
    'do_mime': (
        poses['mime'],
        [('time', 1, 'done_posing')]
    ),

    'done_posing': (
        {
            's': "Est-ce que tu peux faire cele la ?"
        },
        [('time', 1, 'choice')]
    ),
}
