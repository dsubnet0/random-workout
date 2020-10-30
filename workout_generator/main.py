import random
import argparse

class Move(object):
    def __init__(self, name, reversible=False, weightable=False, quietable=True, opener=False):
        self.name = name
        self.reversible = reversible
        self.weightable = weightable
        self.quietable = quietable
        self.opener = opener

def oppositize(move_list):
    oppositized_list = []
    for m in move_list:
        new_move = Move(name=f'OPPOSITE {m.name}', 
                    reversible=m.reversible,
                    quietable=m.quietable,
                    opener=m.opener)
        oppositized_list.append(new_move)
    return oppositized_list

MOVE_LIST = []
def appendMove(move_list, reversible=False, quietable=True, weightable=False, opener=False):
    for m in move_list:
        MOVE_LIST.append(Move(m, reversible=reversible, quietable=quietable, weightable=weightable, opener=opener))

appendMove([
    'Jab', 'Double jab', 'Cross', 'Lead hook', 'Rear hook', 'Lead upper', 'Rear upper', 
    'Slipping jab, low hook', 'Slipping cross, low hook',
    'KB one-handed swing', 'Jab, cross, hook', 'Jab, cross, bursting rear elbow',
    'Rear knee', 'Lead knee', 'Rear elbow', 'Lead elbow',
    'Dual hook punches', 'Hook, cross, hook', 'Cross, hook, cross',
    'Jab, cross, liver shot, lead hook, rear elbow', 
    'Double jab', 'Double jab, spleet shot, rear uppercut',
    'Lead hook, elbow, liver shot, rear knee',
    'Jab, cross, sprawl', 'Jab, cross, hook, sprawl', 'Jab, cross, hook, hook, sprawl',
    'Side kick', 'Back kick',
    'Overhand, uppercut, overhand',
    'High hook, low hook, high hook',
    'Rear upper, hook, cross'
    'Lead elbow, knee, rear elbow, switch knee', 
    'Jab, cross, slipping jab, cross, hook, cross, takedown',
    'Jab, cross, slipping cross, hook, cross, hook, takedown',

    'KB one-handed snatch',
    'KB one-handed swing',
    'KB one-handed clean',
    'KB one-handed thruster',
    'KB one-handed swing high pull',
    'BAND one-handed lateral raise'
    ],
    reversible=True, quietable=True)

appendMove([
    'Push-ups',
    'Squats',
    'Rope',
    'High knees',
    'Jacks',
    'PVC twists',
    'PVC slips',
    'PVC twist squats'
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
	"Bicycle", 
    "X-ups", 
    "V-ups", 

	"Mountain climbers", 
	"Cross-body mountain climbers",
    "Boat extensions", 
    "Russian twist", 
    "Spiderman crunch", 
    "Flutter kicks", 
    "Heel touches", 

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

	"Box Thai knees",
    'Box jumps',
    'Box-weighted lunges',
    'Box push-ups',
    'Box dips',
    'Box-weighted squat press',
    'Box-weighted burpee press',
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
    "BAND: Front raise"
    ],
    reversible=False, quietable=True, opener=False)

appendMove([
    'Lead roundhouse', 
    'Rear roundhouse',
    'Jab, cross, roundhouse', 
    'Cross, jab, lead roundhouse',                
    'Lead groin kick', 
    'Rear groin kick',
    'Lead groin kick, jab, cross',
    'Low roundhouse, mid roundhouse, high roundhouse',
    'Jab, rear roundhouse, cross, switch roundhouse',
    'Hook, roundhouse, overhand, switch roundhouse'],
    reversible=True, quietable=False)


parser = argparse.ArgumentParser()
parser.add_argument('--quietable', help='Quietable only', action='store_true')
args = parser.parse_args()

number_of_rounds = 18
my_workout = []
my_workout.append(random.choice([m.name for m in MOVE_LIST if m.opener==True]))

MOVE_LIST = MOVE_LIST + oppositize([m for m in MOVE_LIST if m.reversible==True])

print(f'Total move list size: {len(MOVE_LIST)}')
for r in range(number_of_rounds-1):
    if args.quietable:
        my_workout.append(random.choice([m.name for m in MOVE_LIST if m.quietable==True]))
    else:
        my_workout.append(random.choice([m.name for m in MOVE_LIST]))

for m in my_workout:
    print(m)
