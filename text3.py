
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

class Car():
  def exlaim(self):
    print("I'm a car!")

class Yugo(Car):
    def exlaim(self):
      print("I'm a Yugo, a not so fancy car")
    def NeedAPush(self):
      print('A little help here...')

giveMeACar = Car()
giveMeAYugo = Yugo()
giveMeACar.exlaim()
giveMeAYugo.exlaim()
giveMeAYugo.NeedAPush()

#one way to do properties
class Duck():
  def __init__(self, inputName):
    self.hiddenName = inputName
  def getName(self):
    print('getter')
    return self.hiddenName
  def setName(self, inputName):
    self.hiddenName = inputName
    print('setter')
  name = property(getName,setName)

fowl = Duck('Howard')

#with decorators
class Mouse():
  def __init__(self, inputName):
    self.__hiddenName = inputName
  @property
  def name(self):
    print('getter')
    return self.__hiddenName
  @name.setter
  def name(self, inputName):
    self.__hiddenName = inputName
    print('setter')

#class methods - methods that affect the class as a whole
class A():
  count = 0
  def __init__(self):
    A.count += 1
  def exclaim(self):
    print('I am an A')
  @classmethod
  def kids(cls):
    print('A has', cls.count, 'little objects.')
  
easyA = A()
breazyA = A()
CheesyA = A()
A.kids()

#static methods
class CoyoteWeapon():
  @staticmethod
  def commercial():
    print('This CoyotoeWeapon has been brought to you by Acme.')

CoyoteWeapon.commercial()

#typing
class Quote():
  def __init__(self,person,words):
    self.person = person
    self.words = words
  def who(self):
    return self.person
  def says(self):
    return self.words + '.'
  
class Question(Quote):
  def says(self):
    return self.words + '?'

class Exclamation(Quote):
  def says(self):
    return self.words +'!'

hunter = Quote('Elmer Fudd','I am hunting wabbits')
print(hunter.who(), 'says:',hunter.says())

hunted1 = Question('Bugs Bunny','What\'s up doc')
print(hunted1.who(), 'says:',hunted1.says())

hunted2 = Exclamation('Daffy Duck','It\'s rabbit season')
print(hunted2.who(), 'says:',hunted2.says())

class BabblingBrook():
  def who(self):
    return 'Brook'
  def says(self):
    return 'Babble'
brook = BabblingBrook()

def whoSays(obj):
  print(obj.who(), 'says:',  obj.says())

whoSays(hunter)
whoSays(hunted1)
whoSays(hunted2)
whoSays(brook)
