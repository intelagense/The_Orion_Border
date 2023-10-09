from Ship import Resources
from Ship import ship
import random

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
      fuel_expenses = random.randint(-1, -2)
      food_reward = random.choice([5, 10, 15])
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
