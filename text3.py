
periodic_table = {'Hydrogen':1,'Helium':2}
print(periodic_table)
carbon = periodic_table.setdefault('Carbon',12)
carbon
Helium = periodic_table.setdefault('Helium',546)
Helium

from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']

from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam','spam','eggs','spam']:
  food_counter[food] += 1

for food, count in food_counter.items():
  print(food,count)

from collections import Counter
breakfast = ['spam','spam','eggs','spam']
breakfast_couner = Counter(breakfast)
breakfast_couner

lunch = ['eggs','eggs','bacon']
lunch_counter = Counter(lunch)
lunch_counter

breakfast_couner + lunch_counter

from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry','Ow!'),
    ('Curly','Nyuk nyuk!')
])

for stooge in quotes:
    print(stooge)

#stack + queue ++ deque
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
  
#itertools (http://bit/ly/py-itertools)
import itertools
for item in itertools.chain([1,2],['a','b']):
    print(item)
def multiply(a,b):
    return a*b

for item in itertools.accumulate([1,2,3,4]):
    print(item)

