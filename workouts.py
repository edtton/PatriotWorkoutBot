from enum import Enum

class Workout:
    def __init__(self, name, machine, gym, notes):
        self.name = name
        self.machine = machine 
        self.gym = gym 
        self.notes = notes

class Machine(Enum):
    #cardio includes pool, erg, treadmill, bike, and ruck. any running movements will be under treadmill even though a treadmill is entirely optional. 
    POOL = "Pool"
    ERG = "Ergometer/rowing machine"
    TREADMILL = "Treadmill"
    BIKE = "Indoor/recumbent cycle or air assault bike"
    STAIR = "Stairmaster machine"
    ELLIPTICAL = "Elliptical machine"
    #if movement requires a rucksack and a treadmill, use RUCK. treadmill is not necessary for anything requiring a ruck.
    RUCK = "Rucksack or heavy backpack"
    #if movement requires dumbbells or barbells + bench, use BENCH 
    BENCH = "Bench variety - decline, incline, adjustable, or upright seat"
    #if movement does not require BENCH or SQUATRACK, use DB or BB
    DUMBBELL = "Dumbbells, EZ-bars or barbell may also be used in a pinch"
    BARBELL = "Barbell, EZ-bars or dumbbells may also be used in a pinch"
    EZBAR = "EZ-bar, dumbbells or barbells may also be used in a pinch"
    PLATELOADSQUAT = "Plate loaded squat machine"
    HIPABDUCTOR = "Hip abduction/sus machine"
    PECDECK = "Pec deck/chest fly machine"
    LATPULLDOWN = "Lat pulldown machine"
    CONVERGINGSHOULDERPRESS = "Converging shoulder press machine"
    CONVERGINGCHESTPRESS = "Converging chest press machine"
    DIP = "Assisted dip machine OR dip bench"
    ROW = "Diverging low row machine (NOT an erg)"
    ABCRUNCH = "Abdominal crunch machine/ab crunch bench"
    ABBENCH = "Ab bench, decline or otherwise is okay too"
    CABLE = "Cable machine, handle selection as necessary"
    TRICEP = "Tricep extension machine"
    BICEP = "Bicep curl machine"
    PREACHER = "Preacher curl machine or preacher curl bench"
    LEGPRESS = "Leg press machine"
    LEGCURL = "Leg curl machine"
    #if movement requires barbells + squatrack, use SQUATRACK 
    SQUATRACK = "Squat rack + barbell"
    DEADLIFT = "Deadlift pad + barbell"
    POWERTOWER = "Pullup/chinup bar or power tower"
    MEDBALL = "Medicine ball"
    BOX = "Plyometric box"
    EXTEND = "Back extension machine/hyperextension bench"
    NONE = "Bodyweight. No equipment required."

machinesList = {machine.name for machine in Machine}

class Gym(Enum):
    RAC = "RAC (Recreation & Athletic Complex)"
    AFC = "AFC (Aquatic & Fitness Center)"
    SKY = "Skyline Fitness Center"
    ANY = "Anywhere you can find space."

list = [
    #RAC erg 
    Workout("4x1000m row, 4:00 rest", Machine.ERG, Gym.RAC, "Start with aggressive burst of 10-20 strokes, then lengthen into sustainable pace. Try to be consistent on all 4 pieces."),
    Workout("8x4:00 row, 2 on 2 off", Machine.ERG, Gym.RAC, "2 minutes ON at race pace (28-34 SPM), followed by 2 minutes OFF active rest."),
    Workout("4x10:00 row, 5:00 rest", Machine.ERG, Gym.RAC, "4-3-2-1 format. Aim for 28-32 race pace for final 3 min of each 10 min."),
    Workout("10x1:00 row, 1:00 rest", Machine.ERG, Gym.RAC, "Sprint work, try to maintain race pace for each piece (28-34 SPM)."),
    Workout("8x250m row, 0:45 rest", Machine.ERG, Gym.RAC, "Sprint work, try to maintain race pace and higher for each piece (28-34 SPM)."),
    Workout("4x15:00 row, 3:00 rest", Machine.ERG, Gym.RAC, "Increase rate and pressure every 5 minutes of the piece, 5-5-5 format. First 5:00 at 75% pressure, 18-22 SPM. Second 5:00 at 90% pressure, 22-26 SPM. Last 5:00 at 100% pressure, 24-28 SPM. Target split recommended to be +15-17 above your last 2K."),
    Workout("5x750m row, 3:00 rest", Machine.ERG, Gym.RAC, "Sprint work, try to maintain race pace (28-34 SPM) and negative splits."),
    Workout("7x6:00 row, no rest", Machine.ERG, Gym.RAC, "Aerobic threshold (AT) work, 3:00 22 SPM, 2:00 25 SPM, 1:00 28 SPM, repeat until done. Challenging pressure."),
    Workout("3x10:00 row, 2:00 rest", Machine.ERG, Gym.RAC, "4-3-2-1 format, first piece 18/20/22/24 SPM, second piece 20/22/24/26 SPM, third piece 22/24/26/28 SPM. Row at half pressure during rest period."),
    Workout("40:00 row", Machine.ERG, Gym.RAC, "Power piece, Low rate (18-22 SPM) but at high to full pressure. Keep the rate consistent and focus on your breathing and form."),
    Workout("6x6:00 row, no rest", Machine.ERG, Gym.RAC, "Aerobic threshold (AT) work, 5 minutes on, 1 minute off as your rest, continuous rowing essentially. Keep consistent rate at 24-26 SPM and 75% pressure for the 5:00, 50-60% pressure for the 1:00."),
    Workout("29:00 row", Machine.ERG, Gym.RAC, "5:00 at 16 SPM, 4:00 at 18 SPM, 3:00 at 20 SPM, 2:00 at 22 SPM, 1:00 at 24 SPM, and back down. Can be done as steady state or power piece."),
    Workout("3x12:00 row, 3:00 rest", Machine.ERG, Gym.RAC, "4:00 at 18 SPM, 4:00 at 20 SPM, 4:00 at 22 SPM. Bump each rate +2 for each subsequent piece. Focus on your technique, own each stroke."),
    Workout("2x20:00 row, 3:00 rest", Machine.ERG, Gym.RAC, "5:00 at 16 SPM, 5:00 at 18 SPM, 5:00 at 20 SPM, 5:00 at 16 SPM. Split should be 10-15 seconds off your 5k split. Focus on your breathing. Can be done as steady state."),
    Workout("3x12:00 row, 3:00 rest", Machine.ERG, Gym.RAC, "First piece at 18 SPM, second at 20 SPM, last at 18 SPM. Aim for a split 10-15 seconds off 5k split. Focus on your form."),
    Workout("2x15:00 row, no rest", Machine.ERG, Gym.RAC, "40 seconds on, 20 seconds off. Beat your PRs. Empty the tank."),
    Workout("3x10:00 row, 4:00 rest", Machine.ERG, Gym.RAC, "30 seconds on, 30 seconds off. On strokes are all out - empty the tank. Control each stroke."),

    #RAC steady state erg 
    Workout("4x15:00 row, 2:00 rest", Machine.ERG, Gym.RAC, "Steady state, start at 18 SPM for first 5:00, bump to 20 for second 5:00, last 5:00 at 22 SPM."),
    Workout("40:00 row", Machine.ERG, Gym.RAC, "Steady state, aim for a rate between 18-22. Can be done in a moderate calorie climb format."),
    Workout("30:00 row", Machine.ERG, Gym.RAC, "Steady state, aim for a rate between 18-22. Can be done in a moderate calorie climb format."),
    Workout("2x30:00 row, 5:00 rest", Machine.ERG, Gym.RAC, "Steady state, aim for a rate between 18-22."),
    Workout("45:00 row", Machine.ERG, Gym.RAC, "Steady state, aim for a rate between 18-22."),
    Workout("11000m row", Machine.ERG, Gym.RAC, "Steady state, pick a low rate (18-22 SPM) and a comfortable split to hold and just try to be consistent throughout the piece."),
    Workout("8000m row", Machine.ERG, Gym.RAC, "Steady state, aim for a rate between 18-22 and a low, comfortable split you can hold."),
    Workout("10x6:30 row, 0:30 rest", Machine.ERG, Gym.RAC, "Steady state, low intervals but keep that rate low (18-22 SPM) and a low split. This is NOT sprint work."),
    Workout("20:00 row", Machine.ERG, Gym.RAC, "Steady state, aim for a rate between 16-22. Try to focus on your form and maintaining a low rate and not exceeding that UT2 zone."),
    Workout("10,000m row", Machine.ERG, Gym.RAC, "Steady state, aim for a rate between 18-22. Focus on your breathing."),
    Workout("21:00 row", Machine.ERG, Gym.RAC, "Steady state, 6-7-8 format. First 6:00 at 16-18 SPM, next 7:00 at 18-20 SPM, last 8:00 at 20-22 SPM."),
    Workout("3x20:00 row, 4:00 rest", Machine.ERG, Gym.RAC, "Steady state, aim for a rate between 18-22."),
    Workout("2x30:00 row, 5:00 rest", Machine.ERG, Gym.RAC, "Steady state pyramid, 5:00 at 18 SPM, 4:00 at 20 SPM, 3:00 at 22 SPM, 2:00 at 24 SPM, 1:00 at 26 SPM, and reverse back down. +2 SPM for each interval on the second piece."),
    

    #RAC bench 
    Workout("4x6 barbell bench, 4:00 rest", Machine.BENCH, Gym.RAC, "-"),
    Workout("3x10 barbell close grip bench, 3:00 rest", Machine.BENCH, Gym.RAC, "-"),
    Workout("3x12 seated shoulder press, 3:00 rest", Machine.BENCH, Gym.RAC, "Use an adjustable bench or an upright seat."),
    #RAC dumbbell
    Workout("3x12 DB bicep curls, 3:00 rest", Machine.DUMBBELL, Gym.RAC, "Can be done seated or standing."),
    Workout("3x12 DB shoulder press, 3:00 rest", Machine.DUMBBELL, Gym.RAC, "Can be done seated or standing."),
    Workout("3x12 Arnold press, 3:00 rest", Machine.DUMBBELL, Gym.RAC, "Can be done seated or standing."),
    #RAC barbell
    Workout("4x10 barbell Pendlay row, 3:00 rest", Machine.BARBELL, Gym.RAC, "-"),
    Workout("4x10 barbell overhead press, rest as needed", Machine.BARBELL, Gym.RAC, "-"),
    Workout("3x12 barbell floor press, rest as needed", Machine.BARBELL, Gym.RAC, "-"),
    #RAC bike
    Workout("5 ROUNDS: 0:10 100% pressure, 1:30 10% pressure", Machine.BIKE, Gym.RAC, "Done on a bike/AAB, but running, rowing, or ski works too."),
    Workout("4x4:30 bike, 1:30 rest", Machine.BIKE, Gym.RAC, "4 rounds for max reps."),
    Workout("4x24 calorie bike", Machine.BIKE, Gym.RAC, "Rest as needed, but keep in mind you're doing these 4 rounds for time."),
    #RAC power tower
    Workout("3x10 chin up, rest as needed", Machine.POWERTOWER, Gym.RAC, "No kipping."),
    Workout("3x5 weighted pull up, rest as needed", Machine.POWERTOWER, Gym.RAC, "No kipping. Try to find a weight vest, backpack, or plate carrier."),
    Workout("3x6 wide-grip pull up, rest as needed", Machine.POWERTOWER, Gym.RAC, "No kipping."),
    #RAC stairmaster
    Workout("3 minutes at 60 steps per minute", Machine.STAIR, Gym.RAC, "If you can find a weighted vest/plate carrier, even better."),
    Workout("5 minutes at 60 steps a minute", Machine.STAIR, Gym.RAC, "If you can find a weighted vest/plate carrier, even better."),
    Workout("1 minute at 90 steps a minute", Machine.STAIR, Gym.RAC, "If you can safely do this weighted down, do it. If not, don't stress it."),
    #RAC hip abductor 
    Workout("3x6-8 hip abductor, 3:00 rest", Machine.HIPABDUCTOR, Gym.RAC, "Low rep range, max 10 reps."),
    Workout("3x10 hip abductor, 3:00 rest", Machine.HIPABDUCTOR, Gym.RAC, "-"),
    Workout("2x8-10 hip abductor, 3:00 rest", Machine.HIPABDUCTOR, Gym.RAC, "-"),
    #RAC pec deck
    Workout("3x10-12 standing pec deck, 3:00 rest", Machine.PECDECK, Gym.RAC, "Lower/costal pecs movement. Good option if there are no cable machines available."),
    Workout("10-12-15-12-10 pec deck pyramid, 3:00 rest", Machine.PECDECK, Gym.RAC, "Start with light weight for 10 reps, increase for 12 reps, heaviest for 15 reps, then work back down."),
    Workout("12 rep pec deck drop set, 3:00 rest", Machine.PECDECK, Gym.RAC, "Start with weight you can move for 12 reps, then drop weight into another 12 reps. Continue until you can no longer perform 12 reps."),

    #AFC pool 
    Workout("3x75m swim, rest as needed", Machine.POOL, Gym.AFC, "Warmup with a 1.5 mile run."),
    Workout("10 min continuous swim", Machine.POOL, Gym.AFC, "Side stroke. Warmup with a 1.5 mile run."),
    Workout("4x200m swim, rest as needed", Machine.POOL, Gym.AFC, "Active recovery piece. Don't empty the tank."),
    Workout("1600m swim", Machine.POOL, Gym.AFC, "Split as desired."),
    Workout("4x200m, 4x100m, 8x50m swim, rest as needed between intervals", Machine.POOL, Gym.AFC, "Split as desired."),
    Workout("4x250 swim, rest as needed", Machine.POOL, Gym.AFC, "Split as desired."),
    #AFC erg
    Workout("4x1500m row, 2:00 rest", Machine.ERG, Gym.AFC, "Conditioning piece. Aim for negative splits, bump rate and pressure every 500m of each piece."),
    #AFC treadmill
    Workout("3 mile easy run", Machine.TREADMILL, Gym.AFC, "5 min easy warmup, aim for a 12 min tempo during the run."),
    #AFC bench
    Workout("4x8 dumbbell bench press, rest as needed", Machine.BENCH, Gym.AFC, "-"),
    #AFC dumbbells
    Workout("1:00 max squats", Machine.DUMBBELL, Gym.AFC, "Done while bear hugging dumbbell or plate."),
    Workout("3x12 dumbbell front squat, 3:00 rest", Machine.DUMBBELL, Gym.AFC, "35 lbs DB is the recommended baseline, but adjust weight as needed."),
    Workout("5x15 goblet squat, 1:30 rest", Machine.DUMBBELL, Gym.AFC, "Done with a 53 lbs kettlebell as baseline, but adjust weight and equipment as necessary."),
    Workout("50x alternating DB goblet reverse lunges", Machine.DUMBBELL, Gym.AFC, "Done for time. 50/35 lbs baseline dumbbell weight."),
    Workout("3x12 walking DB lunges, 3:00 rest", Machine.DUMBBELL, Gym.AFC, "12 lunges EACH LEG, 24 total each set."),
    Workout("3x12 one arm dumbbell rows, 2:00 rest", Machine.DUMBBELL, Gym.AFC, "12 rows ea. arm, 24 total per set."),
    #AFC barbell
    Workout("3x12 barbell Pendlay row, rest as needed", Machine.BARBELL, Gym.AFC, "-"),
    #AFC cable
    Workout("3x10 'JPG' kneeling cable lat pulldown, 3:00 rest", Machine.CABLE, Gym.AFC, "Upper lats movement, but if you want mid-low lats, finish with partials or load the top position more."),
    #AFC squat rack 
    Workout("5x2 clean and jerk, rest as needed", Machine.SQUATRACK, Gym.AFC, "-"),
    #AFC back extension
    Workout("4x12 back extensions, 3:00 rest", Machine.EXTEND, Gym.AFC, "Can be done while holding a plate or dumbbell for added weight."),

    #Skyline bike
    Workout("6x50 cal bike, 2:00 rest", Machine.BIKE, Gym.SKY, "Can also be done with an indoor cycle, but an air assault bike is the preferred platform."),
    Workout("5-6-7 cal bike", Machine.BIKE, Gym.SKY, "Can also be done with an indoor cycle, but an air assault bike is the preferred platform."),
    #Skyline pull up/chin up bar 
    Workout("30x strict pull-ups", Machine.POWERTOWER, Gym.SKY, "Do it for time."),
    #Skyline medicine ball 
    Workout("50x wall ball", Machine.MEDBALL, Gym.SKY, "20/14 lbs medicine ball."),
    Workout("10-12-14 wall ball, 2:00 rest", Machine.MEDBALL, Gym.SKY, "20/14 lbs medicine ball."),
    #Skyline plyo box
    Workout("20 box jump overs", Machine.BOX, Gym.SKY, "Jumping on the box, then off the box is ONE rep. Be careful, your first rep might be a little off."),

    #bodyweight 
    Workout("3x12 Push-Ups, 3:00 rest", Machine.NONE, Gym.ANY, "Distinct pause at the bottom."),
    Workout("3x12 Decline Push-Ups, 3:00 rest", Machine.NONE, Gym.ANY, "Distinct pause at the bottom. Use a box, bench, sidewalk, or a buddy :)"),
    Workout("3x12 Incline Push-Ups, 3:00 rest", Machine.NONE, Gym.ANY, "Distinct pause at the bottom. Use a box, bench, sidewalk, or a buddy :)"),
    Workout("3x12 Diamond Push-Ups", Machine.NONE, Gym.ANY, "90-120 second rest between sets."),
    Workout("Max Plank", Machine.NONE, Gym.ANY, "Record max plank time. Try and beat your previous PR."),
    Workout("4x12 Crunches", Machine.NONE, Gym.ANY, "60-90 second rest between sets."),
    Workout("3x20 lunges ea. leg, 3:00 rest", Machine.NONE, Gym.ANY, "Can be done with a dumbbell or backpack for added weight. Pause at the bottom w/ slow torso twist."),
    Workout("3x12 gorilla butt-ups, 2:00 rest", Machine.NONE, Gym.ANY, "Starting position: bent at the hips, knuckles on the ground, legs straight. Bend your knees and come down until you feel the burn in your thighs. Repeat. Good for boat-movers."),
]
