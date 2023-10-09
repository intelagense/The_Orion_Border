class Resources:
    def __init__(self, fuel, food, crew, hull_state, hull_parts, reactor_state, reactor_parts, weapon_system):
        self.fuel = fuel
        self.food = food
        self.crew = crew
        self.hull_state = hull_state
        self.hull_parts = hull_parts
        self.reactor_state = reactor_state
        self.reactor_parts = reactor_parts
        self.weapon_system = weapon_system

    def fuel_storage(self,fuel_reward):
        self.fuel = self.fuel + fuel_reward
        return self.fuel
    def food_storage(self,food_reward):
        self.food = self.food + food_reward
        return self.food
    def crew_remaining(self,crew_lost):
        crew = crew - crew_lost
    def hull_damage(self):
        hull_state = True
    def hull_parts_(self):
        hull_parts = True
    def reactor_damage(self):
        reactor_state = True
    def reactor_parts_(self):
        reactor_parts = True     
    def fix_hull(self):
        if hull_state is True and hull_parts is True:
            hull_state = False
            hull_parts = False
    def fix_reactor(self):
        if reactor_state is True and reactor_parts is True:
            reactor_state = False
            reactor_parts = False

    def exp_supplye(self):
     print('\n')
     print('=====SUPPLYES=====')
     print('⛽ Fuel=',self.fuel,' '+'🥫 Food=',self.food,' '+'👤 Crew=',self.crew)
     if self.weapon_system is True:
       print('WEAPON SYSTEM: ON-LINE')
     if self.hull_parts is True:
      print('Hull parts avaliable')
     if self.reactor_parts is True:
      print('Reactor parts avaliable')
     if self.hull_state is True:
      print('ALERT: Structural integrity compromised. The ships hull needs urgent repair.')
     if self.reactor_state is True:
      print('ALERT: Reactors fluctiations are unstable. Emergency repairs are encouraged.')
     print('\n')

ship = Resources(10,10,4,False,False,False,False,False)

from act_1_events import mission_traveler

mission_traveler()