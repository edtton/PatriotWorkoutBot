import os
import discord
import random
import motivationals
import workouts
import buildings
import machines
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
keep_alive()
token = os.environ['TOKEN']
intents = discord.Intents.default()
#message_content needs to be set to TRUE
intents.message_content = True
client = discord.Client(intents=intents)

imageLinks = [
  "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg",
  "https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg",
  "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
]


#prints out when bot is up and running - wait until this shows in terminal before executing any commands in server chat
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="$help"))
  print("Patriot Workouts Bot is on station and ready for tasking.\n")


#event handler for receiving message commands
@client.event
async def on_message(message):

  #indicates that the bot is reading in a message from itself, and returns to prevent feedback loop
  if message.author == client.user:
    return

  #$help will display a listing of commands
  if message.content.lower().startswith("$help"):

    command = message.content.split()[1:]
    if len(command) == 1:
      if command[0].lower() == "nearest":
        embed = discord.Embed(
          title=":muscle: Welcome to the GMU Patriot Workout Bot! :feather: ",
          description="Here is some notes on the $nearest command:",
          color=0x0c7c04)
        embed.add_field(name=":round_pushpin: Building Abbreviations:",
                        value="",
                        inline=False)
        embed.add_field(
          name="Johnson Center",
          value="The JC is abbreviated as simply 'jc' or 'johnson'.",
          inline=False)
        embed.add_field(
          name="Art & Design Building",
          value="The Art and Design Building is abbreviated as simply 'art'.",
          inline=False)
        embed.add_field(
          name="Nguyen Engineering Building",
          value=
          "The Nguyen Engineering Building is abbreviated as simply 'nguyen'.",
          inline=False)
        embed.add_field(
          name="David King Hall",
          value="David King Hall is abbreviated as simply 'david'.",
          inline=False)
        embed.add_field(
          name="Student Union Building",
          value=
          "The Student Union Building, or SUB I, is abbreviated as simply 'sub' or 'student'.",
          inline=False)
        embed.add_field(
          name="Angel Cabrera Global Center",
          value=
          "The Angel Cabrera Global Center is abbreviated as simply 'globe'.",
          inline=False)

        await message.channel.send(embed=embed)

      elif command[0].lower() == "machines":
        embed = discord.Embed(
          title=":muscle: Welcome to the GMU Patriot Workout Bot! :feather: ",
          description=
          "Here are all the machines that can be filtered by command. For example, '$machine erg' would only give rowing machine workouts, and '$rac erg' would only give rowing machine workouts that are at the RAC: ",
          color=0x0c7c04)
        embed.add_field(name=":gear: Machines and Equipment:",
                        value="",
                        inline=False)

        for machine in workouts.Machine.__members__.values():
          embed.add_field(name=machine.name, value=machine.value, inline=False)

        await message.channel.send(embed=embed)

      else:
        embed = discord.Embed(title="", description="", color=0x0c7c04)
        embed.add_field(
          name=
          ":ring_buoy: Help command not found. Use '$help' for a list of all currently functional commands. Please try again.",
          value="",
          inline=True)

        await message.channel.send(embed=embed)

    else:
      #completed features
      embed = discord.Embed(title=":muscle: Welcome to the GMU Patriot Workout Bot! :feather:", description="Here are the commands you can use:", color=0x0c7c04)
      embed.add_field(name=":green_circle: Workout Commands:", value="", inline=False)
      embed.add_field(name="$workout",value="A random workout from any Mason Rec facility, using any machine.",inline=False)
      embed.add_field(name="$rac or $rac ___", value="Random RAC workout. For a machine specific workout, include the machine after '$rac'.",inline=False)
      embed.add_field(name="$afc or $afc ___", value="Random AFC workout. For a machine specific workout, include the machine after '$afc'",inline=False)
      embed.add_field(name="$sky or $sky ___", value="Random Skyline workout. For a machine specific workout, include the machine after '$sky'", inline=False)
      embed.add_field(name="$machine ___", value="Random workout on a specific machine. For machine commands, use '$help machines'. For example, '$machine erg' would only give erg workouts. For a list of machines at each facility, use '$list ___'.", inline=False)
      embed.add_field(name="$bodyweight", value= "Random bodyweight workout.", inline=False)
      embed.add_field(name="$cardio", value="Random cardio workout.", inline=False)
      embed.add_field(name="$steadystate", value="Random steady state rowing workout.", inline=False)

      #informational commands
      embed.add_field(name=":green_circle: Informational Commands:", value="", inline=False)
      embed.add_field(name="$nearest ___", value="Nearest facility to the requested building. For example, for the nearest facility to Innovation Hall, use '$nearest innovation'.", inline=False)
      embed.add_field(name="$list ___", value="List of machines/equipment at the requested Rec facility, for example '$list RAC'.", inline=False)
      embed.add_field(name="$help", value="Full list of the commands currently in use.", inline=False)
      embed.add_field(name="$help nearest", value="Some notes about building abbreviations and using the '$nearest' command.", inline=False)
      embed.add_field(name="$help machines", value="A full list of machines and equipment currently in our databank.", inline=False)

      #planned features
      # embed.add_field(name="\n----------------PLANNED FEATURES, COMING SOON!----------------", value="", inline=False)
      # embed.add_field(name="$all", value="Wanna just see 'em all? This will give you a list of all our banked workouts.", inline=False)
      # embed.add_field(name="$list ___", value="This will give you list of machines and equipment at the requested Rec facility, for example '$list rac'.", inline=False)
      # embed.add_field(name="$freeweight", value="This will give you a random workout using free weights, rather than a machine.", inline=False)
      # embed.add_field(name="$strength", value="This will give you a random strength workout, which generally includes weight or resistance training movements.", inline=False)
      # embed.add_field(name="$push", value="This will give you a random push day workout, to supplement your existing push day routine.", inline=False)
      # embed.add_field(name="$pull", value="This will give you a random pull day workout, to supplement your existing pull day routine.", inline=False)
      # embed.add_field(name="$legs", value="This will give you a random leg day workout, to supplement your existing leg day routine.", inline=False)
      # embed.add_field(name="$core", value="This will give you a random core/abs workout, to supplement your existing core/abs routine.", inline=False)
      # embed.add_field(name="$recovery", value="This will give you a random active recovery workout, to do on an active recovery day. These are generally low intensity, low impact but are meant to keep you moving and out of complacency.", inline=False)
      # embed.add_field(name="$circuit ___", value="This will give you a random circuit of workouts, based on the number you enter. For example, if I wanted a circuit with 3 movements, I would type '$circuit 3'.", inline=False)
      # embed.add_field(name="$time ___", value="This will give you a random workout within a request time length estimate. Simply enter in the desired length in minutes, and you will receive a workout that is either in that interval or can be easily modified to fit that interval. For example, if I wanted a max length of 10 minutes, I would type '$time 10'.", inline=False)
      # embed.add_field(name="$list ___", value="This will give you a list of all machines/equipment at the requested facility. For example, if I wanted the equipment list at the AFC, I would type '$list afc'.", inline=False

      embed.set_footer(text="NOTE: This bot is intended to supplement your existing routine and is not intended to be a replacement. Do your research and consult a coach/advisor to see what's best for you.")
      await message.channel.send(embed=embed)

  #$workout will give a random workout from bank of ALL workouts, regardless of equipment, or gym.
  if message.content.lower().startswith("$workout"):
    result = random.choice(workouts.list)

    embed = discord.Embed(title=":muscle: Your Random Workout is: ",
                          description=result.name,
                          color=0x0c7c04)

    if result.gym == workouts.Gym.RAC:
      embed.set_thumbnail(
        url=
        "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg")
    elif result.gym == workouts.Gym.AFC:
      embed.set_thumbnail(
        url="https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
    elif result.gym == workouts.Gym.SKY:
      embed.set_thumbnail(
        url=
        "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
      )
    else:
      randomLink = random.choice(imageLinks)
      embed.set_thumbnail(url=randomLink)

    embed.add_field(name=":gear: Machine:",
                    value=result.machine.value,
                    inline=True)
    embed.add_field(name=":round_pushpin: Gym:",
                    value=result.gym.value,
                    inline=False)
    embed.add_field(name=":scroll: Notes:", value=result.notes, inline=False)

    if result.machine == workouts.Machine.ERG:
      randomString = random.choice(motivationals.row) + " #PatriotNation "
    else:
      randomString = random.choice(motivationals.list) + " #PatriotNation "

    embed.set_footer(text=randomString)

    await message.channel.send(embed=embed)

  #cardio-only workout command
  if message.content.lower().startswith("$cardio"):
    result = random.choice(workouts.list)
    while result.machine not in [
        workouts.Machine.POOL, workouts.Machine.ERG,
        workouts.Machine.TREADMILL, workouts.Machine.BIKE,
        workouts.Machine.STAIR, workouts.Machine.ELLIPTICAL,
        workouts.Machine.RUCK
    ]:
      result = random.choice(workouts.list)

    embed = discord.Embed(
      title=":anatomical_heart: Your Random Cardio Workout is:",
      description=result.name,
      color=0x0c7c04)

    if result.gym == workouts.Gym.RAC:
      embed.set_thumbnail(
        url=
        "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg")
    elif result.gym == workouts.Gym.AFC:
      embed.set_thumbnail(
        url="https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
    elif result.gym == workouts.Gym.SKY:
      embed.set_thumbnail(
        url=
        "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
      )
    else:
      randomLink = random.choice(imageLinks)
      embed.set_thumbnail(url=randomLink)

    embed.add_field(name=":gear: Machine:",
                    value=result.machine.value,
                    inline=True)
    embed.add_field(name=":round_pushpin: Gym:",
                    value=result.gym.value,
                    inline=False)
    embed.add_field(name=":scroll: Notes:", value=result.notes, inline=False)

    if result.machine == workouts.Machine.ERG:
      randomString = random.choice(motivationals.row) + " #PatriotNation "
    else:
      randomString = random.choice(motivationals.list) + " #PatriotNation "

    embed.set_footer(text=randomString)

    await message.channel.send(embed=embed)

  #RAC workouts command
  if message.content.lower().startswith("$rac"):

    #RAC machine specific workout
    command = message.content.split()[1:]
    if len(command) == 1:
      target = command[0]
      target = target.upper()

      if target in workouts.machinesList:
        matchingWorkouts = [
          w for w in workouts.list
          if w.machine.name == target and w.gym == workouts.Gym.RAC
        ]
        if not matchingWorkouts:
          embed = discord.Embed(title="", description="", color=0x0c7c04)
          embed.add_field(
            name=
            ":gear: There are currently no workouts using this machine/equipment at the RAC. Please try again.",
            value="",
            inline=True)
          await message.channel.send(embed=embed)
        else:
          result = random.choice(workouts.list)
          while result.machine.name != target or result.gym != workouts.Gym.RAC:
            result = random.choice(workouts.list)

          embed = discord.Embed(title=":muscle: Your RAC " + target +
                                " Workout is: ",
                                description=result.name,
                                color=0x0c7c04)

          if result.gym == workouts.Gym.RAC:
            embed.set_thumbnail(
              url=
              "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg"
            )
          elif result.gym == workouts.Gym.AFC:
            embed.set_thumbnail(
              url=
              "https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
          elif result.gym == workouts.Gym.SKY:
            embed.set_thumbnail(
              url=
              "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
            )
          else:
            randomLink = random.choice(imageLinks)
            embed.set_thumbnail(url=randomLink)

          embed.add_field(name=":gear: Machine:",
                          value=result.machine.value,
                          inline=True)
          embed.add_field(name=":round_pushpin: Gym:",
                          value=result.gym.value,
                          inline=False)
          embed.add_field(name=":scroll: Notes:",
                          value=result.notes,
                          inline=False)
          if result.machine == workouts.Machine.ERG:
            randomString = random.choice(motivationals.row) + " #PatriotNation"
          else:
            randomString = random.choice(
              motivationals.list) + " #PatriotNation"
          embed.set_footer(text=randomString)

          await message.channel.send(embed=embed)

      #user enters in target machine that is not in workout databank
      else:
        embed = discord.Embed(title="", description="", color=0x0c7c04)
        embed.add_field(
          name=
          ":gear: This machine is currently not in our databank. Please try again.",
          value="",
          inline=True)
        await message.channel.send(embed=embed)

    #any RAC workout
    else:
      result = random.choice(workouts.list)
      while result.gym != workouts.Gym.RAC:
        result = random.choice(workouts.list)

      embed = discord.Embed(title=":muscle: Your Random RAC Workout is: ",
                            description=result.name,
                            color=0x0c7c04)
      embed.set_thumbnail(
        url=
        "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg")
      embed.add_field(name=":gear: Machine:",
                      value=result.machine.value,
                      inline=True)
      embed.add_field(name=":round_pushpin: Gym:",
                      value=result.gym.value,
                      inline=False)
      embed.add_field(name=":scroll: Notes:", value=result.notes, inline=False)

      if result.machine == workouts.Machine.ERG:
        randomString = random.choice(motivationals.row) + " #PatriotNation"
      else:
        randomString = random.choice(motivationals.list) + " #PatriotNation"

      embed.set_footer(text=randomString)

      await message.channel.send(embed=embed)

  #AFC workouts command
  if message.content.lower().startswith("$afc"):
    #AFC machine specific workout
    command = message.content.split()[1:]
    if len(command) == 1:
      target = command[0]
      target = target.upper()

      if target in workouts.machinesList:
        matchingWorkouts = [
          w for w in workouts.list
          if w.machine.name == target and w.gym == workouts.Gym.AFC
        ]
        if not matchingWorkouts:
          embed = discord.Embed(title="", description="", color=0x0c7c04)
          embed.add_field(
            name=
            ":gear: There are currently no workouts using this machine/equipment at the AFC. Please try again.",
            value="",
            inline=True)
          await message.channel.send(embed=embed)
        else:
          result = random.choice(workouts.list)
          while result.machine.name != target or result.gym != workouts.Gym.AFC:
            result = random.choice(workouts.list)

          embed = discord.Embed(title=":muscle: Your AFC " + target +
                                " Workout is: ",
                                description=result.name,
                                color=0x0c7c04)

          if result.gym == workouts.Gym.RAC:
            embed.set_thumbnail(
              url=
              "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg"
            )
          elif result.gym == workouts.Gym.AFC:
            embed.set_thumbnail(
              url=
              "https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
          elif result.gym == workouts.Gym.SKY:
            embed.set_thumbnail(
              url=
              "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
            )
          else:
            randomLink = random.choice(imageLinks)
            embed.set_thumbnail(url=randomLink)

          embed.add_field(name=":gear: Machine:",
                          value=result.machine.value,
                          inline=True)
          embed.add_field(name=":round_pushpin: Gym:",
                          value=result.gym.value,
                          inline=False)
          embed.add_field(name=":scroll: Notes:",
                          value=result.notes,
                          inline=False)
          if result.machine == workouts.Machine.ERG:
            randomString = random.choice(motivationals.row) + " #PatriotNation"
          else:
            randomString = random.choice(
              motivationals.list) + " #PatriotNation"
          embed.set_footer(text=randomString)

          await message.channel.send(embed=embed)

      #user enters in target machine that is not in workout databank
      else:
        embed = discord.Embed(title="", description="", color=0x0c7c04)
        embed.add_field(
          name=
          ":gear: This machine is currently not in our databank. Please try again.",
          value="",
          inline=True)
        await message.channel.send(embed=embed)

    #any AFC workout
    else:
      result = random.choice(workouts.list)
      while result.gym != workouts.Gym.AFC:
        result = random.choice(workouts.list)

      embed = discord.Embed(title=":muscle: Your Random AFC Workout is: ",
                            description=result.name,
                            color=0x0c7c04)
      embed.set_thumbnail(
        url="https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
      embed.add_field(name=":gear: Machine:",
                      value=result.machine.value,
                      inline=True)
      embed.add_field(name=":round_pushpin: Gym:",
                      value=result.gym.value,
                      inline=False)
      embed.add_field(name=":scroll: Notes:", value=result.notes, inline=False)

      if result.machine == workouts.Machine.ERG:
        randomString = random.choice(motivationals.row) + " #PatriotNation"
      else:
        randomString = random.choice(motivationals.list) + " #PatriotNation"

      embed.set_footer(text=randomString)

      await message.channel.send(embed=embed)

  #Skyline workout command
  if message.content.lower().startswith("$sky") or message.content.lower().startswith("$skyline"):
    #Skyline machine specific workout
    command = message.content.split()[1:]
    if len(command) == 1:
      target = command[0]
      target = target.upper()

      if target in workouts.machinesList:
        matchingWorkouts = [
          w for w in workouts.list
          if w.machine.name == target and w.gym == workouts.Gym.SKY
        ]
        if not matchingWorkouts:
          embed = discord.Embed(title="", description="", color=0x0c7c04)
          embed.add_field(
            name=
            ":gear: There are currently no workouts using this machine/equipment at Skyline. Please try again.",
            value="",
            inline=True)
          await message.channel.send(embed=embed)
        else:
          result = random.choice(workouts.list)
          while result.machine.name != target or result.gym != workouts.Gym.SKY:
            result = random.choice(workouts.list)

          embed = discord.Embed(title=":muscle: Your Skyline " + target +
                                " Workout is: ",
                                description=result.name,
                                color=0x0c7c04)

          if result.gym == workouts.Gym.RAC:
            embed.set_thumbnail(
              url=
              "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg"
            )
          elif result.gym == workouts.Gym.AFC:
            embed.set_thumbnail(
              url=
              "https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
          elif result.gym == workouts.Gym.SKY:
            embed.set_thumbnail(
              url=
              "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
            )
          else:
            randomLink = random.choice(imageLinks)
            embed.set_thumbnail(url=randomLink)

          embed.add_field(name=":gear: Machine:",
                          value=result.machine.value,
                          inline=True)
          embed.add_field(name=":round_pushpin: Gym:",
                          value=result.gym.value,
                          inline=False)
          embed.add_field(name=":scroll: Notes:",
                          value=result.notes,
                          inline=False)
          if result.machine == workouts.Machine.ERG:
            randomString = random.choice(motivationals.row) + " #PatriotNation"
          else:
            randomString = random.choice(
              motivationals.list) + " #PatriotNation"
          embed.set_footer(text=randomString)

          await message.channel.send(embed=embed)

      #user enters in target machine that is not in workout databank
      else:
        embed = discord.Embed(title="", description="", color=0x0c7c04)
        embed.add_field(
          name=
          ":gear: This machine is currently not in our databank. Please try again.",
          value="",
          inline=True)
        await message.channel.send(embed=embed)

    #any Skyline workout
    else:
      result = random.choice(workouts.list)
      while result.gym != workouts.Gym.SKY:
        result = random.choice(workouts.list)

      embed = discord.Embed(title=":muscle: Your Random Skyline Workout is: ",
                            description=result.name,
                            color=0x0c7c04)
      embed.set_thumbnail(
        url=
        "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
      )
      embed.add_field(name=":gear: Machine:",
                      value=result.machine.value,
                      inline=True)
      embed.add_field(name=":round_pushpin: Gym:",
                      value=result.gym.value,
                      inline=False)
      embed.add_field(name=":scroll: Notes:", value=result.notes, inline=False)

      if result.machine == workouts.Machine.ERG:
        randomString = random.choice(motivationals.row) + " #PatriotNation"
      else:
        randomString = random.choice(motivationals.list) + " #PatriotNation"

      embed.set_footer(text=randomString)

      await message.channel.send(embed=embed)

  #only bodyweight movements, by default there are no exercises that are bodyweight that are associated with a gym so nothing with a gym tag will be included here.
  if message.content.lower().startswith("$bodyweight"):
    result = random.choice(workouts.list)
    while result.machine != workouts.Machine.NONE:
      result = random.choice(workouts.list)

    imageLink = random.choice(imageLinks)

    embed = discord.Embed(title=":muscle: Your Random Bodyweight Workout is: ",
                          description=result.name,
                          color=0x0c7c04)
    embed.set_thumbnail(url=imageLink)
    embed.add_field(name=":gear: Machine:",
                    value=result.machine.value,
                    inline=True)
    embed.add_field(name=":round_pushpin: Gym:",
                    value=result.gym.value,
                    inline=False)
    embed.add_field(name=":scroll: Notes:", value=result.notes, inline=False)
    randomString = random.choice(motivationals.list) + " #PatriotNation"
    embed.set_footer(text=randomString)

    await message.channel.send(embed=embed)

  #only steady state rowing movements, by default these are all ERG pieces
  if message.content.lower().startswith("$steadystate"):
    result = random.choice(workouts.list)
    while not result.name.startswith("Steady State"):
      result = random.choice(workouts.list)

    embed = discord.Embed(
      title=":rowboat: Your Random Steady State Workout is: ",
      description=result.name,
      color=0x0c7c04)

    if result.gym == workouts.Gym.RAC:
      embed.set_thumbnail(
        url=
        "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg")
    elif result.gym == workouts.Gym.AFC:
      embed.set_thumbnail(
        url="https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
    elif result.gym == workouts.Gym.SKY:
      embed.set_thumbnail(
        url=
        "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
      )
    else:
      randomLink = random.choice(imageLinks)
      embed.set_thumbnail(url=randomLink)

    embed.add_field(name=":round_pushpin: Gym:",
                    value=result.gym.value,
                    inline=False)
    embed.add_field(name=":scroll: Notes:", value=result.notes, inline=False)

    randomString = random.choice(motivationals.row) + " #PatriotNation"
    embed.set_footer(text=randomString)

    await message.channel.send(embed=embed)

  #only give workouts pertaining to target machine
  if message.content.lower().startswith("$machine"):
    command = message.content.split()[1:]
    if len(command) == 1:
      target = command[0]
      target = target.upper()

      if target in workouts.machinesList:
        matchingWorkouts = [
          w for w in workouts.list if w.machine.name == target
        ]

        if not matchingWorkouts:
          embed = discord.Embed(title="", description="", color=0x0c7c04)
          embed.add_field(
            name=
            ":gear: There are currently no workouts using this machine/equipment in our databank. Please try again.",
            value="",
            inline=True)
          await message.channel.send(embed=embed)

        else:
          result = random.choice(workouts.list)
          while result.machine.name != target:
            result = random.choice(workouts.list)

          embed = discord.Embed(title=":muscle: Your " + target +
                                " Workout is: ",
                                description=result.name,
                                color=0x0c7c04)

          if result.gym == workouts.Gym.RAC:
            embed.set_thumbnail(
              url=
              "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg"
            )
          elif result.gym == workouts.Gym.AFC:
            embed.set_thumbnail(
              url=
              "https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
          elif result.gym == workouts.Gym.SKY:
            embed.set_thumbnail(
              url=
              "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
            )
          else:
            randomLink = random.choice(imageLinks)
            embed.set_thumbnail(url=randomLink)

          embed.add_field(name=":gear: Machine:",
                          value=result.machine.value,
                          inline=True)
          embed.add_field(name=":round_pushpin: Gym:",
                          value=result.gym.value,
                          inline=False)
          embed.add_field(name=":scroll: Notes:",
                          value=result.notes,
                          inline=False)
          if result.machine == workouts.Machine.ERG:
            randomString = random.choice(motivationals.row) + " #PatriotNation"
          else:
            randomString = random.choice(
              motivationals.list) + " #PatriotNation"
          embed.set_footer(text=randomString)

          await message.channel.send(embed=embed)

      #user enters in target machine that is not in workout databank
      else:
        embed = discord.Embed(title="", description="", color=0x0c7c04)
        embed.add_field(
          name=
          ":gear: This machine is currently not in our databank. Please try again.",
          value="",
          inline=True)
        await message.channel.send(embed=embed)

    #user enters in $machine with no target machine
    else:
      embed = discord.Embed(title="", description="", color=0x0c7c04)
      embed.add_field(
        name=
        ":gear: There must be a machine target after the command, such as '$machine erg'. Please try again.",
        value="",
        inline=True)
      await message.channel.send(embed=embed)

  #list machines at target gym command
  if message.content.lower().startswith("$list"):
    command = message.content.split()[1:]

    if len(command) < 1: 
      embed = discord.Embed(title="", description="", color=0x0c7c04)
      embed.add_field(name=":gear: There must be a location target after the command, such as '$list rac'. Please try again.", value="", inline=True)
      await message.channel.send(embed=embed)

    if command[0].lower() == "rac":
      embed = discord.Embed(
        title=":gear: Machines and Equipment at the RAC :round_pushpin: ",
        description="This is a list of machines/equipment at the RAC. For a workout on a specific machine, use the machine commands listed in the command '$help machines': ",
        color=0x0c7c04)
      embed.set_thumbnail(
        url="https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg")
      embed.add_field(name=":gear: Machines and Equipment:",
                      value="",
                      inline=False)

      for machine in machines.RAC_machines:
        embed.add_field(name=machine, value="", inline=False)

      embed.set_footer(text="Big thanks to Becky Demus and the Mason Recreation staff for their help with this project! #PatriotNation")

      await message.channel.send(embed=embed)

    elif command[0].lower() == "afc":
      embed = discord.Embed(
        title=":gear: Machines and Equipment at the AFC :round_pushpin: ",
        description="This is a list of machines/equipment at the AFC. For a workout on a specific machine, use the machine commands listed in the command '$help machines': ",
        color=0x0c7c04)
      embed.set_thumbnail(
        url="https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
      embed.add_field(name=":gear: Machines and Equipment:",
                      value="",
                      inline=False)

      for machine in machines.AFC_machines:
        embed.add_field(name=machine, value="", inline=False)

      embed.set_footer(text="Big thanks to Becky Demus and the Mason Recreation staff for their help with this project! #PatriotNation")

      await message.channel.send(embed=embed)

    elif command[0].lower() == "sky" or command[0].lower() == "skyline":
      embed = discord.Embed(
        title=":gear: Machines and Equipment at Skyline :round_pushpin: ",
        description="This is a list of machines/equipment at Skyline. For a workout on a specific machine, use the machine commands listed in the command '$help machines': ",
        color=0x0c7c04)
      embed.set_thumbnail(
        url="https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg")
      embed.add_field(name=":gear: Machines and Equipment:",
                      value="",
                      inline=False)

      for machine in machines.SKY_machines:
        embed.add_field(name=machine, value="", inline=False)

      embed.set_footer(text="Big thanks to Becky Demus and the Mason Recreation staff for their help with this project! #PatriotNation")

      await message.channel.send(embed=embed)

  #locate gym nearest to target building
  if message.content.lower().startswith("$nearest"):
    command = message.content.split()[1:]

    if len(command) < 1:
      embed = discord.Embed(title="", description="", color=0x0c7c04)
      embed.add_field(
        name=
        ":round_pushpin: There must be a location target after the command, such as '$nearest innovation hall'. Please try again.",
        value="",
        inline=True)
      await message.channel.send(embed=embed)

    location = command[0]
    location = location.lower()

    if location in buildings.nearRAC:
      embed = discord.Embed(title=":round_pushpin: The nearest gym to " +
                            location.capitalize() + " is:",
                            description="",
                            color=0x0c7c04)
      embed.add_field(name=workouts.Gym.RAC.value,
                      value="4350 Banister Creek Ct, Fairfax, VA 22030",
                      inline=True)
      embed.set_thumbnail(
        url=
        "https://recreation.gmu.edu/wp-content/uploads/2012/10/Rac-photo.jpg")
      await message.channel.send(embed=embed)

    elif location in buildings.nearAFC:
      embed = discord.Embed(title=":round_pushpin: The nearest gym to " +
                            location.capitalize() + " is:",
                            description="",
                            color=0x0c7c04)
      embed.add_field(name=workouts.Gym.AFC.value,
                      value="4520 Patriot Cir, Fairfax, VA 22030",
                      inline=True)
      embed.set_thumbnail(
        url="https://recreation.gmu.edu/wp-content/uploads/2012/10/afc.jpg")
      await message.channel.send(embed=embed)

    elif location in buildings.nearSKY:
      embed = discord.Embed(title=":round_pushpin: The nearest gym to " +
                            location.capitalize() + " is:",
                            description="",
                            color=0x0c7c04)
      embed.add_field(name=workouts.Gym.SKY.value,
                      value="4400 University Drive MS 6C10, Fairfax, VA 22030",
                      inline=True)
      embed.set_thumbnail(
        url=
        "https://i.pinimg.com/originals/fa/94/16/fa94169a9c6807cc6ca17c9f2b9f0965.jpg"
      )
      await message.channel.send(embed=embed)

    else:
      embed = discord.Embed(title="", description="", color=0x0c7c04)
      embed.add_field(
        name=
        ":round_pushpin: This building either could not be located or is not in our registry. Please try again.",
        value="",
        inline=True)
      await message.channel.send(embed=embed)


client.run(token)
