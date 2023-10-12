from resources import Resources
from Dices import Dice
import random

ship = Resources(10,10,4,False,False,False,False,False,False)

def mission_traveler():
  
 print('A traveler is looking for a ship available to allow him travel to a nearby planet.')
 print('It says he\'s willing to pay for the trouble.')
 print('Accepting this request will use extra fuel.')
 print('\"yes\" = The expedition accepts the mission')
 print('\"not\" = The expedition ignores the mission')

 while True:
     m1 = input()
     print('\n')

     if m1 == 'yes':
      fuel_expenses = Dice.dice(2)
      food_reward = Dice.reward3(5,10,15)
      print('The job is done easely and without trouble. To do the trip the ship used ',fuel_expenses, 'units of fuel')
      print(food_reward, 'units of food has been given as a reward for the job.')
      print('\n')
      ship.fuel_used(fuel_expenses)
      ship.food_storage(food_reward)
      break
     elif m1 == 'not':
      print('The crew ignores the request and moves on.')
      print('\n')
      break
     else:
      print('Wrong imput, write \"yes\" or \"not\" to continue:')

def asteroid_impact():
 
 print('An asteroid is heading towards the ship!')
 
 asteroid_impact = Dice.dice(2) # this part decides the fate of the ship by rolling a d3
 if asteroid_impact == 0 and ship.hull_state is False: #The ship takes the shoot but the hull persist
  print('Luckily the hull was strong enough to endure the impact with no meaningfull damage.')
  print('\n')

 elif asteroid_impact == 0 and ship.hull_state is True: #The ship is too damaged to take the shoot, but the pilot manages to save the ship
  print('The pilot pulls out a quick move that alows the ship to avoid collision.')
  print('Sadly, such a maneuver cost 1 unit of fuel')
  ship.fuel_used(1)

 elif asteroid_impact >= 1 and ship.hull_state is True: #The ship takes the shoot and is too damaged to endure it
  asteroid_ship_save_roll = Dice.dice(2)
  if asteroid_ship_save_roll == 1: #Somehow the ship survives the impact, with a cost
     asteroid_crew_lost_impact = Dice.dice(2)
     print('The hull, even tough it\'s damaged, endured the hit, but')
     print('the incident took',asteroid_crew_lost_impact,' crew members lives.')
     ship.crew_remaining(asteroid_crew_lost_impact)
  elif asteroid_ship_save_roll == 2:
     #The impact was too much for the ship. "Game Over" baby
     ship.ship_game_over
     print('The asteroid goes through the ship like a bullet, causing catastrophic damage.')
  else:
    print('SHIP_ASTEROID_SAVE_THROW_ERROR') # Just in case I messed up something

 elif ship.hull_state is False:
    ship.hull_damage()
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

 while True:
    m3 = input()
    print('\n')

    if m3 == 'yes':
     print('The ship advances, heading towards the electrical anomaly.')
     print('As the expedition ship aproaches arcs of electricity move around the star dust of the anomaly.')
     anomaly_safe_roll = Dice.dice(2)
     if anomaly_safe_roll == 1:
       print('Electrical arks form around the ship like an angry storm.')
       print('Some of the systems in the ship spark when an arc hits the ship, but furter damage is avoided.')
       print('The ship manages to get out of the storm with just minor scratches that are fixed soon enough.')
       break
     if anomaly_safe_roll >= 2:
      if ship.reactor_state is False:
       print('¡One of the arcs hit the ship! damaging the electrical systems and the reactor.')
       ship.reactor_damage
       break
      if ship.reactor_state is True:
       print('¡One of the arcs hit the ship!')
       print('The already damaged reactor can not withstand the raw power of the storm, forcing a meltdown')
       ship.ship_game_over
       break
      else:
        print('ELECTRIC_STORM_SAVE_ROLL_ERROR')

    elif m3 == 'not':
     electric_storm_safety = Dice.dice(2)
     print('The ship moves around the edge of the anomaly, avoiding the danger.')
     print('Nonetheless, safety has come with the extra cost of ',electric_storm_safety,' units of fuel.')
     ship.fuel_used(electric_storm_safety)
     break

    else:
     print('Wrong imput, write \"yes\" or \"not\" to continue:')

