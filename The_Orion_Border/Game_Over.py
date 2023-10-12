from act_1_events import ship
from score import score

def master_game_over():
 if ship.fuel <= 0 or ship.crew <= 0 or ship.game_over is True:
    print('Like many others before, the expedition never arrive to it\'s destination at the Orion Border')
    score()
    while True:
      try_again = input(str('¿Try again?(yes/not)'))
      if try_again == 'yes':
        print('')
      elif try_again == 'not':
        print('')
      else:
        print('Wrong input.')