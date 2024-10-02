item = ""

cotton = 0
log = 0
rock = 0
quartz = 0
string = 0
wood = 0
ribbon = 0
metal = 0
needles = 0
sparkles = 0
bronze = 0
silver = 0
gold = 0
amethyst = 0
pendant = 0
necklace = 0
orb = 0
water = 0
fire = 0
waterstone = 0
firestone = 0
elementstone = 0
artifact = 0
coins = 0

def c_string(i):
  global cotton
  global string
  global coins
  cotton += 3 * i
  string += i
  coins += 50 * i

def c_wood(i):
  global wood
  global log
  global coins
  wood += i
  log += i * 3
  coins += 50 * i

def c_ribbon(i):
  global ribbon
  global coins
  c_wood(2 * i)
  c_string(2 * i)
  ribbon += i
  coins += 100 * i

def c_metal(i):
  global metal
  global rock
  global coins
  metal += i
  rock += i * 3
  coins += 100 * i

def c_needles(i):
  global needles
  global coins
  c_metal(4 * i)
  c_ribbon(i)
  needles += i
  coins += 200 * i

def c_sparkles(i):
  global sparkles
  global coins
  c_needles(2 * i)
  c_ribbon(2 * i)
  sparkles += i
  coins += 300 * i

def c_bronze(i):
  global rock
  global bronze
  global coins
  bronze += i
  rock += i * 4
  coins += 200 * i

def c_silver(i):
  global silver
  global coins
  c_bronze(i * 3)
  c_sparkles(i)
  silver += i
  coins += 300 * i

def c_gold(i):
  global gold
  global coins
  c_silver(2 * i)
  c_sparkles(2 * i)
  gold += i
  coins += 500 * i

def c_amethyst(i):
  global amethyst
  global quartz
  global coins
  amethyst += i
  quartz += i * 10
  coins += 300 * i

def c_pendant(i):
  global pendant
  global coins
  c_amethyst(i * 7)
  c_silver(i * 2)
  pendant += i
  coins += 500 * i

def c_necklace(i):
  global necklace
  global coins
  c_pendant(i * 3)
  c_gold(i * 2)
  necklace += i
  coins += 800 * i

def c_orb(i):
  global orb
  global quartz
  global coins
  orb += i
  quartz += i * 20
  coins += 300 * i

def c_water(i):
  global water
  global coins
  c_orb(i * 2)
  c_silver(i)
  water += i
  coins += 800 * i

def c_fire(i):
  global fire
  global coins
  c_orb(i * 6)
  c_gold(i)
  fire += i
  coins += 1000 * i

def c_waterstone(i):
  global waterstone
  global coins
  c_water(i * 2)
  c_ribbon(i * 10)
  waterstone += i
  coins += 1500 * i

def c_firestone(i):
  global firestone
  global coins
  c_fire(i)
  c_sparkles(i * 2)
  firestone += i
  coins += 1500 * i

def c_elementstone(i):
  global elementstone
  global coins
  c_firestone(i)
  c_waterstone(i)
  elementstone += i
  coins += 5000 * i

def c_artifact(i):
  global artifact
  global coins
  c_elementstone(i)
  c_necklace(i)
  artifact += i
  coins += i * 10000

def reseting():
  global cotton; cotton = 0
  global log; log = 0
  global rock; rock = 0
  global quartz; quartz = 0
  global string; string = 0
  global wood; wood = 0
  global ribbon; ribbon = 0
  global metal; metal = 0
  global needles; needles = 0
  global sparkles; sparkles = 0
  global bronze; bronze = 0
  global silver; silver = 0
  global gold; gold = 0
  global amethyst; amethyst = 0
  global pendant; pendant = 0
  global necklace; necklace = 0
  global orb; orb = 0
  global water; water = 0
  global fire; fire = 0
  global waterstone; waterstone = 0
  global firestone; firestone = 0
  global elementstone; elementstone = 0
  global artifact; artifact = 0
  global coins; coins = 0

def total():
  print("cotton: " + str(cotton))
  print("log: " + str(log))
  print("rock: " + str(rock))
  print("quartz: " + str(quartz))
  print('string: ' + str(string))
  print('wood: ' + str(wood))
  print('ribbon: ' + str(ribbon))
  print('metal: ' + str(metal))
  print('needles: ' + str(needles))
  print('sparkles: ' + str(sparkles))
  print('bronze: ' + str(bronze))
  print('silver: ' + str(silver))
  print('gold: ' + str(gold))
  print('amethyst: ' + str(amethyst))
  print('pendant: ' + str(pendant))
  print('necklace: ' + str(necklace))
  print('orb: ' + str(orb))
  print('water: ' + str(water))
  print('fire: ' + str(fire))
  print('waterstone: ' + str(waterstone))
  print('firestone: ' + str(firestone))
  print('elementstone: ' + str(elementstone))
  print('artifact: ' + str(artifact))
  print('coins: ' + str(coins))
  

