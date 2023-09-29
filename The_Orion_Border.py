import random

# The number of jumps the ship will need to end the game
travel_time_goal = 10
# The combustible that the ship has
fuel_num = 10
# How many crew does the ship has
crew_num = 4
# How much food the ship has
food_num = 10
# Indicates if the hull of the ship is damaged
hull_damage = 2 # Hull damage will have 3 states of damage (0 = Game over, 1 = Hull damaged, 2 = normal)
# Indicates if the reactor of the ship is damaged
reactor_malfuction = 2 # reactor damage will have 3 states of damage (0 = Game over, 1 = reactor damaged, 2 = normal)
# Allows to fix the reactor if true
reactor_parts = False
# Allows to fix the hull if true
hull_parts = False
# Allows the ship to shoot at enemy ships
weapon_system = False
# Names of the different crew members
names = ('Rogers', 'Maria', 'Paul\'QuickHands\'', 'Andrew', 'Luna', 'Subaru', 'Kiho', 'Harnaf', 'Asuka', 'Strotnor', 'Nora')

# allows to call for the expedition supplye info 
def exp_supplye():
 print('\n')
 print('=====SUPPLYES=====')
 print('Fuel=',fuel_num,' '+'Food=',food_num,' '+'Crew=',crew_num)
 if weapon_system is True:
  print('WEAPON SYSTEM: ON-LINE')
 if hull_parts is True:
  print('Hull parts avaliable')
 if reactor_parts is True:
  print('Reactor parts avaliable')
 if hull_damage == 1:
  print('ALERT: Structural integrity compromised. The ships hull needs urgent repair.')
 if reactor_malfuction == 1:
  print('ALERT: Reactors fluctiations are unstable. Emergency repairs are encouraged.')
 print('\n')

# pause between actions to allow the player read more calmly
def pause():
  while True:
    pause_ip = input('Please, write \"continue\" to continue your adventure: ')

    if pause_ip == 'continue':
      print ('\n')
      break
    
    else:
      print('Wrong imput')
      return

# Resources consumption with every new event
def after_event():
   global food_num
   global fuel_num
   global crew_num

   fuel_num = fuel_num - 1
   if food_num - crew_num < 0: #In case the expedition gets out of food but there whas still some for part of the crew
    food_num = food_num - crew_num
    crew_num = crew_num + food_num
    food_num = 0
    return
   else:
    food_num = food_num - crew_num
    return

#=================Intro=================

print('Like many others, a new crew has formed to try reach the deepest parts of the Galaxy, The Orion Border.')
print('It\'s a dangeroys travel, where many had died traying. Make sure to have enough fuel and food for it.')
print('\n')
pause()

#=================Game Over=================
def game_over():
  global exp_supplye
  if fuel_num <= 0 or crew_num <= 0 or hull_damage <= 0 or reactor_malfuction <= 0:
    print(exp_supplye())
    print('The expedition never managed to arriva to it\'s destinatio')
    print('GAME OVER')
    
#=================ACT 1=================

# Mission: traveler in problems
def mission_traveler():

 global fuel_num
 global food_num

 print('A traveler is looking for a ship available to allow him travel to a nearby planet.')
 print('It says he\'s willing to pay for the trouble.')
 print('Accepting this request will use extra fuel.')
 print('\"yes\" = The expedition accepts the mission')
 print('\"not\" = The expedition ignores the mission')

 while True:
     m1 = input()
     print('\n')

     if m1 == 'yes':
      fuel_yes_m1 = random.randint(1, 3)
      food_reward_m1 = random.choice([5, 10, 15])
      print('The job is done easely and without trouble. To do the trip the ship used ',fuel_yes_m1, 'units of fuel')
      print(food_reward_m1, 'units of food has been given as a reward for the job.')
      print('\n')
      fuel_num = fuel_num - fuel_yes_m1
      food_num = food_num + food_reward_m1
      break

     elif m1 == 'not':
      print('The crew ignores the request and moves on.')
      print('\n')
      break

     else:
      print('Wrong imput, write \"yes\" or \"not\" to continue:')

# Asteroid hit
def asteroid_impact():
 
 print('An asteroid is heading towards the ship!')

 global hull_damage
 global crew_num
 global fuel_num
 
 asteroid_impact = random.choice([0,1,2]) # this part decides the fate of the ship by rolling a d3
 if asteroid_impact == 0 and hull_damage == 2: #The ship takes the shoot but the hull persist
  print('Luckily the hull was strong enough to endure the impact with no meaningfull damage.')
  print('\n')

 elif asteroid_impact == 0 and hull_damage == 1: #The ship is too damaged to take the shoot, but the pilot manages to save the ship
  print('The pilot pulls out a quick move that alows the ship to avoid collision.')
  print('Sadly, such a maneuver cost 1 unit of fuel')
  fuel_num = fuel_num - 1

 elif asteroid_impact >= 1 and hull_damage == 1: #The ship takes the shoot and is too damaged to endure it
  asteroid_ship_save_roll = random.choice ([1,2])
  if asteroid_ship_save_roll == True: #Somehow the ship survives the impact, with a cost
     asteroid_fatal_impact = random.choice([1,2])
     print('The hull, even tough it\'s damaged, endured the hit, but')
     print('the incident took',asteroid_fatal_impact,' crew members lives.')
     crew_num = crew_num - asteroid_fatal_impact
  elif asteroid_ship_save_roll == 2:
     #The impact was too much for the ship. "Game Over" baby
     print('The asteroid goes through the ship like a bullet, causing catastrophic damage.')
     hull_damage = hull_damage - 1
  else:
    print('SHIP_ASTEROID_SAVE_THROW_ERROR') # Just in case I messed up something

 elif hull_damage == 2:
    hull_damage = hull_damage - 1
    print('The hull was able to withstand the impact, but it got severely damaged from it.')
 else:
    print('ASTEROID_HIT_HULL_STATE_ERROR') # Just in case I messed up something

# Electric storm
def electric_storm():

 print('The scaners show that the ship is aproaching an electrical anomaly.')
 print('Going trough it would be the fastest way, but also the most dangerous.')
 print('Surrounding the anomaly would be the safest, but it would need more time and fuel')
 print('\"yes\" = The ship goes through the anomaly.')
 print('\"not\" = The ship surrounds the anomaly.')

 global fuel_num
 global reactor_malfuction

 while True:

    m3 = input()
    print('\n')

    if m3 == 'yes':
     print('The ship advances, heading towards the electrical anomaly.')
     print('As the expedition ship aproaches arcs of electricity move around the star dust of the anomaly.')
     electric_storm_save_roll = random.randint(1,3)
     if electric_storm_save_roll == 1:
       print('Electrical arks form around the ship like an angry storm.')
       print('Some of the systems in the ship spark when an arc hits the ship, but furter damage is avoided.')
       print('The ship manages to get out of the storm with just minor scratches that are fixed soon enough.')
       break
     if electric_storm_save_roll >= 2:
      if reactor_malfuction == 2:
       print('¡One of the arcs hit the ship! damaging the electrical systems and the reactor.')
       reactor_malfuction = reactor_malfuction - 1
       break
      if reactor_malfuction == 1:
       print('¡One of the arcs hit the ship!')
       print('The already damaged reactor can not withstand the raw power of the storm, forcing a meltdown')
       break
      else:
        print('ELECTRIC_STORM_SAVE_ROLL_ERROR')

    elif m3 == 'not':
     electric_storm_safety = random.randint(1,2)
     print('The ship moves around the edge of the anomaly, avoiding the danger.')
     print('Nonetheless, safety has come with the extra cost of ',electric_storm_safety,' units of fuel.')
     fuel_num = fuel_num - electric_storm_safety
     break

    else:
     print('Wrong imput, write \"yes\" or \"not\" to continue:')

# Scrap Field
def scrap_field():
 global hull_damage
 global hull_parts
 global reactor_parts
 global weapon_system

#This roll will determinate if the scrap field has a scrap dealer or not
 scrap_field_version = random.randint(1,2)
#This is the version where the scrap field is empty and the player will have to put it's ship at risk for the loot
 if scrap_field_version == 1:
   
  print('¡The ship has entered an area with a big scrap field!')
  print('The field can be explored with no need to use extra fuel since is close to the designated path of the ship.')
  print('Tough the debry seems very stable, going in with a faulty hull its greatly inadvisable.')
  print('\"yes\" = The ship goes into the scrap field to look for parts.')
  print('\"not\" = The ship keeps it\'s current course.')

  while True:
   global crew_num
   global food_num
   global fuel_num
   global hull_damage
   global hull_parts
   global reactor_parts
   global reactor_malfuction
   global weapon_system

   m3 = input()
   print('\n')
    
   if m3 == 'yes':
       if hull_damage == 1:
        print('Red lights and alarms go on around the ship as the damaged Hull tries to witsthand a storm of tiny pices of scrap.')
        print('A part of the ship despresurices trough the event, forcing the crew to move out of the scrap field.')
        scrap_impact = random.randint(1,2)
        print('After the incident ',scrap_impact,' bodys where recovered.')
        crew_num = crew_num - scrap_impact
        break
       elif hull_damage == 2:
        print('Even with the constant noise of small pices of scrap hiting at the hull the structure of the ship')
        print('is able to endure it with no issues.')
        print('The ship whas able to salvage something from the scrap field:')
        scrap_field_reward = random.choice([1,2,3])
        if scrap_field_reward == 1: #Electronic parts
          reactor_parts = True
          print('Reactor parts: they can be used to fix a damaged reactor')
          break
        elif scrap_field_reward == 2: #Hull parts
          hull_parts = True
          print('Hull parts: can be used to fix a ship\'s damaged hull')
          break
        elif scrap_field_reward == 3: #Weapon sistems online
          weapon_system = True
          print('Old artillery: can be instaled on a ships hull to provide protection')
          break
        else:
          print('SCRAP_FIELD_EVENT_REWARD: ERROR')
       else:
        print('SCRAP_FIELD_EVENT_ERROR')
   elif m3 == 'not':
      print('The ship continues the route passing nearby the scrap field')
      return
   else:
      print('Wrong imput, write \"yes\" or \"not\" to continue:')

#In this version a recycling ship is alredy on the scrap field and will trade with the player
 elif scrap_field_version == 2:

   #Price is 1 to 3 would be fuel as price, from 5 to 7 food
   price_list = (1,2,3,5,6,7)
   hull_scrap_price = random.sample(price_list,1)
   reactor_scrap_price = random.sample(price_list,1)
   artillery_scrap_price = random.sample(price_list,1)

   #This part is to indicate to the player if the price is in fuel or in food
   #It also storages the output of the trade in fuel and food to warn the player if buying the iteam will bankrump him
   for a in hull_scrap_price:
    if a <= 3:
      fuel_or_food_1 = 'fuel units'
      fuel_storage_1 = fuel_num - a
    elif a >= 5:
     fuel_or_food_1 = 'food units'
     food_storage_1 = food_num - a
    else:
     print('HULL_FOOD_OR_FUEL_ERROR')

   for b in reactor_scrap_price:
    if b <= 3:
     fuel_or_food_2 = 'fuel units'
     fuel_storage_2 = fuel_num - b
    elif b >= 5:
     fuel_or_food_2 = 'food units'
     food_storage_2 = food_num - b
    else:
     print('REACTOR_FOOD_OR_FUEL_ERROR')

   for c in artillery_scrap_price:
    if c <= 3:
     fuel_or_food_3 = 'fuel units'
     fuel_storage_3 = fuel_num - c
    elif c >= 5:
     fuel_or_food_3 = 'food units'
     food_storage_3 = food_num - c
    else:
     print('ARTILLERY_FOOD_OR_FUEL_ERROR')

   print('¡The ship has entered an area with a big scrap field!')
   print('The radar indicates that there is a ship nearby, and is sending a signal with the')
   print('following message:')
   print('\"¡Hey!¡We arrive here first!¡If you want scrap, pay for it!\"')
   print('\n')
   while True:
    exp_supplye()
    print('The recycling ship is offerinc the next items for sale.')
    print('Writhe the name of the item to buy it or \"exit\" if you want to finish trading.')
    print('=========SCRAP&PARTS=========')
    if hull_parts is False:
      print('Hull parts: ¡keep your crew alive with a healty hull! =>', a, fuel_or_food_1)
    elif hull_parts is True:
      print('Hull parts: -SOLD OUT-')
    else:
      print('HULL_SELLING_ERROR')
    if reactor_parts is False:
      print('Reactor parts: ¡Is the heart of your ship!¡Keep it pumping! =>', b, fuel_or_food_2)
    elif reactor_parts is True:
      print('Reactor parts: -SOLD OUT-')
    else:
      print('REACTOR_SELLING_ERROR')
    if weapon_system is False:
      print('Old artillery: ¡To keep the scum away!¡Or become the scum with it! =>', c, fuel_or_food_3)
    elif weapon_system is True:
      print('Reactor parts: -SOLD OUT-')
    else:
      print('WEAPONS_SELLING_ERROR')
    m3 = input()
    #Trade outputs... this is gonna be long
    #Trade output for the hull parts
    if m3 == 'Hull parts' or m3 == 'hull parts':
      if hull_parts is True:
        print('\n')
        print('¡I can\'t fit more of those in your ship! ¡pick something else!')
        print('\n')
      elif hull_parts is False: 
       if fuel_or_food_1 == 'food units' and food_storage_1 <= 0 or fuel_or_food_1 == 'fuel units' and fuel_storage_1 <= 0:
        print('\n')
        print('¡Can\'t affort it mate!')
        print('\n')
       elif fuel_or_food_1 == 'food units' and food_storage_1 > 0 or fuel_or_food_1 == 'fuel units' and fuel_storage_1 > 0:
        hull_parts = True
        if fuel_or_food_1 == 'fuel units':
         fuel_num = fuel_storage_1
         fuel_storage_2 = fuel_num - b
         fuel_storage_3 = fuel_num - c
        elif fuel_or_food_1 == 'food units':
         food_num = food_storage_1
         food_storage_2 = food_num - b
         food_storage_3 = food_num - c
    #Reactor parts selling code
    elif m3 == 'Reactor parts' or m3 == 'reactor parts':
      if reactor_parts is True:
        print('\n')
        print('¡I can\'t fit more of those in your ship! ¡pick something else!')
        print('\n')
      elif reactor_parts is False:
        if fuel_or_food_2 == 'food units' and food_storage_2 <= 0 or fuel_or_food_2 == 'fuel units' and fuel_storage_2 <= 0:
         print('\n')
         print('¡Can\'t affort it mate!')
         print('\n')
        elif fuel_or_food_2 == 'food units' and food_storage_2 > 0 or fuel_or_food_2 == 'fuel units' and fuel_storage_2 > 0:
          reactor_parts = True
          if fuel_or_food_2 == 'fuel units':
           fuel_num = fuel_storage_2
           fuel_storage_1 = fuel_num - a
           fuel_storage_3 = fuel_num - c
          elif fuel_or_food_2 == 'food units':
           food_num = food_storage_2
           food_storage_1 = food_num - a
           food_storage_3 = food_num - c
    #Trade output for the artillery parts
    elif m3 == 'Old artillery' or m3 == 'old artillery':
      if weapon_system is True:
        print('\n')
        print('¡I can\'t fit more of those in your ship! ¡pick something else!')
        print('\n')
      elif weapon_system is False:
        if fuel_or_food_3 == 'food units' and food_storage_3 <= 0 or fuel_or_food_3 == 'fuel units' and fuel_storage_3 <= 0:
         print('\n')
         print('¡Can\'t affort it mate!')
         print('\n')
        elif fuel_or_food_3 == 'food units' and food_storage_3 > 0 or fuel_or_food_3 == 'fuel units' and fuel_storage_3 > 0:
          weapon_system = True
          if fuel_or_food_3 == 'fuel units':
            fuel_num = fuel_storage_3
            fuel_storage_1 = fuel_num - a
            fuel_storage_2 = fuel_num - b
          elif fuel_or_food_3 == 'food units':
            food_num = food_storage_3
            food_storage_1 = food_num - a
            food_storage_2 = food_num - b
    #Ending trade
    elif m3 == 'Exit' or m3 == 'exit':
         print('\n')
         print('¡It has been a pleasure to do business!')
         print('\n')
         break
    else:
      print('wrong imput, please writhe the name of the parts you want to purchase or \'exist\' if you want to continue your journey:')

 else:
   print('SCRAP_FIELD_VERSION_ROLL_ERROR')

# Abandoned ship
def abandoned_ship():

 print('The ship radar has caught a strange lecture nearby.')
 print('It\'s origin seems to come from another ship.')
 print('It has it\'s lights off and doesn\'t respond to radio calls.')
 print('Seems like it\'s possible to send a team of 2 crew members to board it.')
 print('\n')
 print('Sending a team can be risky, but profitable.')
 print('\"yes\" = A team is send into the ship.')
 print('\"not\" = The expedition ignores the ship and moves on.')

 def abandoned_ship_scenario_1():
   global food_num
   global fuel_num

   food_reward_m4 = random.choice([5, 15])
   fuel_reward_m4 = random.choice([2, 4])
   print('The team searchs the ship, but nobody is found on board.')
   print('After an a few hours, the team returns with ',food_reward_m4,' units of food and ',fuel_reward_m4,' of fuel.')
   print('The team refuses to steep foot on that ship again as they say they feelt been watch during the mission.')
   food_num = food_num + food_reward_m4
   fuel_num = fuel_num + fuel_reward_m4

 def abandoned_ship_scenario_2():
   global crew_num

   print('The team goes into the ship with no issues. They report seen a room with the lights on')
   print('but when they aproach it, the communications are cut off.')

   print('After traying for a few hours to restablish communication unsuccessfully')
   print('the search team it\'s declared lost and the remaining crew decides to stay away from the ship')
   print('and continue theyr journey.')
   crew_num = crew_num - 2

 while True:
    m4 = input()
    print('\n')
 
    if m4 == 'yes':
     abandoned_ship_exploration_fates = [abandoned_ship_scenario_1, abandoned_ship_scenario_2]
     exploration_team_fate = random.choice(abandoned_ship_exploration_fates)
     exploration_team_fate()
     break

    elif m4 == 'not':
     print('It has been decided that it will be whiser to not board the ship.')
     break

    else:
     print('Wrong imput, write \"yes\" or \"not\" to continue:')

#Old fuel station
def old_fuel_station():
  global reactor_parts
  global fuel_num

  print('The expedition has entered a new system.')
  print('There is a fuel supply station nearby, but seems like it has been undermaintinance for a long time.')
  print('The hulk of the supply station floats silently around a gas giant.')
  print('Seems like it has been abandoned as the docks have signs saying \"Out of order\" and \"Condemned\".')
  print('There could still be fuel left inside of the station.')
  print('\n')
  print('Send a team to look for fuel?')
  print('\"yes\" = A team will be sent into the station to look for fuel.')
  print('\"not\" = The expedition will continue theyr journey with out stop.')

  while True:
   m5 = input()
   print('\n')
   if m5 == 'yes':
     fuel_station_exploration = random.randint(1,2)
     print('The expedition boards the fuel suply station.')
     print('They where able to find ', fuel_station_exploration,' of fuel.')
     print('\n')
     print('While exploring the station, the team noticed that the machinery is not damaged')
     print('and only need power.')
     if reactor_parts is False:
       print('Sadly, the reactor is missing some parts')
       print('and can not be fixed without them.')
       break
     elif reactor_parts is True:
       print('The reactor seems to be missing some parts.')
       print('The team could use the reactor parts stored at the ship to fix it.')
       print('\"yes\" = To use the reactor parts on fixtin the station reactor.')
       print('\"not\" = Leave the station with what the team alredy found.')
       while True:
         m5 = input()
         print('\n')
         if m5 == 'yes':
           reactor_parts = False
           print('A humming noise can be heard as the reactor, along with the rest of the station')
           print('comes back to life.')
           print('It only works for a few seconds before the screens all around the station alert')
           print('than a critical error has ocurred.')
           fuel_production = random.randint(3,6)
           print('Yet, ',fuel_production,' units of fuel where produced by the industrial machinery in')
           print('that short time lapse.')
           fuel_num = fuel_num + fuel_production
           break
         elif m5 == 'not':
           print('Reactor parts are a valuable resource. The crew decides')
           print('that is not worth use them to fix the station reactor.')
           print('The team lefts the station with that they already found.')
           break
         else:
           print('Wrong imput, write \"yes\" or \"not\" to continue:')
   elif m5 == 'no':
     print('The ship lefts behind the station, becoming just a tiny point in contrast of the')
     print('of the gas giant surface.')
     print('The expedition continues its journey.')
     break
   else:
       print('Wrong imput, write \"yes\" or \"not\" to continue:')

#radiation storm
def radiation_storm():
  global fuel_num
  global crew_num

  print('All screens on bord proyect a red alert with the next message:')
  print('DANGER: RADIATION WAVE IN COMMING, LOOK FOR SHELTER INMEDIATLY')
  print('\n')
  print('There is only 2 pods avaliable on bord that can shelter the crew from the wave.')
  print('Only 1 crew member can fit on a pod at the same time.')
  print('None the less, the ship could deploy a shield around the hulk to protect the crew')
  print('but to do it, the reactor will need 1 extra unit of fuel.')
  print('\n')
  print('¿Deploy shield?')
  print('\"yes\"= The shield will be deployed to protect the whole ship from the radiation wave.')
  print('\"not\"= The shield will not be deployed, and only 2 crew members will be safe from the radiation.')
  while True:
   m6 = input()
   if m6 == 'yes':
     print('\n')
     print('The reactor glows as it supplys the ship with the extra power needed to deploy the shield.')
     print('\n')
     print('The radiation lectures skyrocket out of the ships hull, going further byond safety limits.')
     print('Yet the shield reflects almost all of the radiation, leting through only a small')
     print('ammount, within the range of non-hazardous')
     fuel_num = fuel_num - 1
     break
   elif m6 == 'not':
     print('The smell of iron fills the ship, followed by a strange warm that engolfs anybody that')
     print('didn\'t find shelter on time.')
     print('\n')
     print('After a few hours, the ship automatic descontamination procedures are over and it\'t safe to go out of the pods again.')
     if crew_num > 2:
       radiation_fatalitys = crew_num - 2
       print('There where',radiation_fatalitys,' crew members that died from severe radiation poisoning')
       crew_num = crew_num - radiation_fatalitys
       break
     elif crew_num <= 2:
       print('Luckily, there where enough pods for the crew.')
       break
   else:
       print('Wrong imput, write \"yes\" or \"not\" to continue:')

#=================Tale Randomizer 1º act=================
   #Here are stored all the possible events for the first act of the game
first_act_possible_events = [scrap_field, old_fuel_station, radiation_storm, mission_traveler, asteroid_impact] #scrap_field, old_fuel_station, radiation_storm, mission_traveler, asteroid_impact
   #These gentleman will choose the events that will be plaid for the players Tale
event_1_selector = random.choice(first_act_possible_events)
event_2_selector = random.choice(first_act_possible_events)
event_3_selector = random.choice(first_act_possible_events)
event_4_selector = random.choice(first_act_possible_events)
   #These functions make sure that the events will not repeat them selfs in the same game
  
print('[[THIS IS event_1_selector]]') #Temporary adjustment to make sure all works well (DELETE THIS WHEN TEST OVER)
exp_supplye()
event_1_selector()
after_event()
pause()
while True:
    event_2_selector = random.choice(first_act_possible_events)
    if event_2_selector != event_1_selector:
       print('[[THIS IS event_2_selector]]') #Temporary adjustment to make sure all works well (DELETE THIS WHEN TEST OVER)
       exp_supplye()
       event_2_selector()
       after_event()
       game_over()
       pause()
       break
while True:
     event_3_selector = random.choice(first_act_possible_events)
     if event_3_selector != event_1_selector and event_3_selector != event_2_selector:
          print('[[THIS IS event_3_selector]]') #Temporary adjustment to make sure works well (DELETE THIS WHEN TEST OVER)
          exp_supplye()
          event_3_selector()
          after_event()
          game_over()
          pause()
          break
while True:
         event_4_selector = random.choice(first_act_possible_events)
         if event_4_selector != event_1_selector and event_4_selector != event_2_selector and event_4_selector != event_3_selector:
          print('[[THIS IS event_4_selector]]') #Temporary adjustment to make sure works well (DELETE THIS WHEN TEST OVER)
          exp_supplye()
          event_4_selector()
          after_event()
          game_over()
          pause()
          break
#Introduction to the 2º act
print('The expedition arrives to Novrobsk trade station, one of the')
print('last known civilized posts before reaching the borders of the explored galaxy.')
print('Byond this point only the unknow awhaits.')
print('\n')
print('The merchant post offers a variety of goods for the correct price')
#Extend trade post with FIXED prices
print('\n')
while True:
 exp_supplye()
 print('=========Novrobsk Trade Post=========')
 print('\n')
 print('Food: A cate filled with 4 food cans => [3 fuel units]')
 print('Fuel: A fuel tank storing 3 units of fuel => [4 food units]')
 print('Recruit: Someone desperate looking for work => [2 units of food and fuel]')
 print('\n')
 print('Writhe the name of the supply to buy or \"exit\" if you want to finish trading.')
 novrobsk_trade = input()
 if novrobsk_trade == 'food' or novrobsk_trade == 'Food':
  if fuel_num - 3 > 0:
   print('\n')
   print('A food crate has been added to the ship storage.')
   print('\n')
   fuel_num = fuel_num - 3
   food_num = food_num + 4
  elif fuel_num - 3 <= 0:
   print('\n')
   print('The expedition can\'t affort that.')
   print('\n')
  else:
    print('NOVROBSK_FOOD_TRADE_ERROR')
 elif novrobsk_trade == 'fuel' or novrobsk_trade == 'Fuel':
  if food_num - 4 > 0:
   print('\n')
   print('A fuel tank has been added to the ship storage.')
   print('\n')
   food_num = food_num - 4
   fuel_num = fuel_num + 3
  elif food_num - 4 <= 0:
   print('\n')
   print('The expedition can\'t affort that.')
   print('\n')
  else:
    print('NOVROBSK_FUEL_TRADE_ERROR')
 elif novrobsk_trade == 'recruit' or novrobsk_trade == 'Recruit':
   print('\n')
   print('A new member has joined the crew.')
   print('\n')
   crew_num = crew_num + 1
   food_num = food_num - 2
   fuel_num = fuel_num - 2
 elif novrobsk_trade == 'exit' or novrobsk_trade == 'Exit':
   print('\n')
   print('The expedition says farewell to Novrobsk station as they move towards')
   print('the unknow.')
   print('Having managed to arrive this far the crew seems enthusiastic')
   print('\n')
   after_event()
   break
 else:
   print('Wrong input. Please, writhe the name of the supply to buy or \"exit\" if you want to finish trading.')


print('The ship, beating all odds, has arrived to the Orion Border.')
game_over = True