from Ship import Ship

Ship.fuel = 10
Ship.food = 10
Ship.crew = 4
Ship.hull_state = False
Ship.hull_parts = False
Ship.reactor_state = False
Ship.reactor_parts = False
Ship.weapon_system = False

def exp_supplye():
 print('\n')
 print('=====SUPPLYES=====')
 print('⛽ Fuel=',Ship.fuel,' '+'🥫 Food=',Ship.food,' '+'👤 Crew=',Ship.crew)
 if Ship.weapon_system is True:
  print('WEAPON SYSTEM: ON-LINE')
 if Ship.hull_parts is True:
  print('Hull parts avaliable')
 if Ship.reactor_parts is True:
  print('Reactor parts avaliable')
 if Ship.hull_state is True:
  print('ALERT: Structural integrity compromised. The ships hull needs urgent repair.')
 if Ship.reactor_state is True:
  print('ALERT: Reactors fluctiations are unstable. Emergency repairs are encouraged.')
 print('\n')
 return