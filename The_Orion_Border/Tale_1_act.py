import random
from act_1_events import ship
from act_1_events import mission_traveler,asteroid_impact,electric_storm,scrap_field
from Game_Over import master_game_over

act_one_event_list = (asteroid_impact, scrap_field)
event_manager_event_numeration = range(2)
event_manager_tale_list = random.sample(event_manager_event_numeration, 2)
print(event_manager_tale_list)
#=================Intro=================

print('Like many others, a new crew has formed to try reach the deepest parts of the Galaxy, The Orion Border.')
print('It\'s a dangeroys travel, where many had died traying. Make sure to have enough fuel and food for it.')

ship.exp_supplye()
act_one_event_list[event_manager_tale_list[0]]()
master_game_over()
ship.exp_supplye()
act_one_event_list[event_manager_tale_list[1]]()
master_game_over()
ship.exp_supplye()

