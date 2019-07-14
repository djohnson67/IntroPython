def get_desription():
  '''return random weather, just like the pros'''
  from random import choice
  possibilities = ['rain', 'snow','sleet', 'fog','sun','who know\'s']
  return choice(possibilities)