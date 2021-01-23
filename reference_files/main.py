import random
import argparse

MOVE_LIST = []

class Move(object):
    def __init__(self, name, reversible=False, bag=False, quietable=True, opener=False, kb=False, ground=False):
        self.name = name
        self.reversible = reversible
        self.bag = bag
        self.quietable = quietable
        self.opener = opener
        self.kb = kb
        self.ground = ground

def oppositize(move_list):
    oppositized_list = []
    for m in move_list:
        new_move = Move(name=f'OPPOSITE {m.name}', 
                    reversible=m.reversible,
                    quietable=m.quietable,
                    opener=m.opener,
                    bag=m.bag,
                    ground=m.ground)
        oppositized_list.append(new_move)
    return oppositized_list

def appendMove(move_list, reversible=False, quietable=True, bag=False, opener=False, kb=False, ground=False):
    for m in move_list:
        MOVE_LIST.append(Move(m, reversible=reversible, 
                                    quietable=quietable, 
                                    bag=bag, 
                                    opener=opener,
                                    ground=ground))

appendMove([
    'Jab', 'Double jab', 'Cross', 'Lead hook', 'Rear hook', 'Lead upper', 'Rear upper', 
    'Slipping jab, low hook', 'Slipping cross, low hook',
    'Jab, cross, hook', 'Jab, cross, bursting rear elbow',
    'Rear knee', 'Lead knee', 'Rear elbow', 'Lead elbow',
    'Dual hook punches', 'Hook, cross, hook', 'Cross, hook, cross',
    'Jab, cross, liver shot, lead hook, rear elbow', 
    'Double jab, spleen shot, rear uppercut',
    'Lead hook, elbow, liver shot, rear knee',
    'Jab, cross, sprawl', 'Jab, cross, hook, sprawl', 'Jab, cross, hook, hook, sprawl',
    'Side kick', 
    'Overhand, uppercut, overhand',
    'High hook, low hook, high hook',
    'Rear upper, hook, cross',
    'Lead elbow, knee, rear elbow, switch knee', 
    'Jab, cross, slipping jab, cross, hook, cross, takedown',
    'Jab, cross, slipping cross, hook, cross, hook, takedown',

    'KB one-handed snatch',
    'KB one-handed swing',
    'KB one-handed clean',
    'KB one-handed thruster',
    'KB one-handed swing high pull',
    'BAND one-handed lateral raise',
    'SPEAR oblique situp',
    'Ground side kick',
    'Ground front kick',
    'BAND: Ground side kick',
    'BAND: Ground front kick',
    ],
    reversible=True, quietable=True)

appendMove([
    'Push-ups',
    'Squats',
    'Rope',
    'High knees',
    'Jacks',
    'PVC twists',
    'PVC slips'
    ], 
    reversible=False, quietable=True, opener=True)

appendMove([
    "Wide push-ups", 
    "Diamond push-ups",
    "Hindu push-ups", 
    "Reptile push-ups", 
    "SPEAR push-up sequence",
	"Dips",
    
	"Switch knees", 
    "Back kicks",

	"Squats", 
    "Pistol squats", 
    "Squat jumps", 
    "Tuck jumps",

	"Forward lunges", 
    "Backward lunges", 
    "Twisting lunges", 
    "Jump lunges",

	"Reaching crunches", 
    "Feet-raised crunches", 
    "Candlestick crunches",
    "Leg lifts", 
    "Long arm crunches",
    'Alternating precision SPEAR crunches',
	"Bicycle", 
    "X-ups", 
    "V-ups", 

	"Mountain climbers", 
	"Cross-body mountain climbers",
    "SPEAR mountain climbers",
    "Boat extensions", 
    "Russian twist", 
    "Spiderman crunch", 
    "Flutter kicks", 
    "Heel touches",
    "Palm strike situps", 

	"Extended plank", 
    "Forearm plank",

	"Calf raises",
	"Bear-crab roll",
	"Burpees",
	"Bag lift",
    "Hip-outs",
	"Spiderman lunge",
	"Upas", 
    "Butt bridges",
    "SPEAR situp",
    "Candlesticks",

	"Box Thai knees",
    'Box jumps',
    'Box push-ups',
    'Box dips',
    'Box burpees',

    'Ball squat press',
    'Ball push-ups',
    "Ball burpees",
	"Ball tricep extensions",
    "Ball bicep curl", 
    "Ball standing twist",
	"Ball V-ups",
    "Ball twists",
    "Ball plank",

    "KB swings", 
    "KB twist press", 
    "KB deadlift", 
    "KB standing twist", 
	"KB Russian twist", 
    "KB goblet squat", 
    "KB bob & weave", 
    "KB squat and press",
	"KB reverse lunge and press", 
    "KB two-handed high pull",

    "BAND: Bicep curl", 
    "BAND: Front raise",
    "BAND: SPEAR situp",
    "BAND: Palm strikes",
    "BAND: Palm strike situps"
    ],
    reversible=False, quietable=True, opener=False)

appendMove([
    'Lead roundhouse', 
    'Rear roundhouse',
    'Jab, cross, roundhouse', 
    'Cross, jab, lead roundhouse',                
    'Lead groin kick', 
    'Rear groin kick',
    'Lead front kick',
    'Rear front kick',
    'Lead groin kick, jab, cross',
    'Low roundhouse, mid roundhouse, high roundhouse',
    'Jab, rear roundhouse, cross, switch roundhouse',
    'Hook, roundhouse, overhand, switch roundhouse'],
    reversible=True, quietable=False)


parser = argparse.ArgumentParser()
parser.add_argument('--quietable', help='Quietable only', action='store_true')
args = parser.parse_args()

number_of_rounds = 18
keep_balanced = True
my_workout = []
my_workout.append(random.choice([m.name for m in MOVE_LIST if m.opener==True]))

reversible_moves = [m.name for m in MOVE_LIST if m.reversible==True]

#print(f'Total move list size: {len(MOVE_LIST)}')
while len(my_workout) < 18:
    next_move = ''
    if args.quietable:
        next_move = random.choice([m.name for m in MOVE_LIST if m.quietable==True])
    else:
        next_move = random.choice([m.name for m in MOVE_LIST])
    my_workout.append(next_move)
    if keep_balanced and next_move in reversible_moves and len(my_workout)<18:
        my_workout.append('OPPOSITE '+ next_move)
for m in my_workout:
    print(m)
