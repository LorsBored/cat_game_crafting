
item = ""

C1 = 0
C2 = 0
C3 = 0
R = 0
E = 0
L = 0
M1 = 0
M2 = 0
M3 = 0
token = 0

def Common1(i):
  global C1
  global M1
  global token
  C1 += i
  M1 += i * 4
  token += 35 * i
def Common2(i):
  global C2
  global M2
  global token
  C2 += i
  M2 += i * 4
  token += 35 * i
def Common3(i):
  global C3
  global M3
  global token
  C3 += i
  M3 += i * 8
  token += 35 * i
def Rare(i):
  global R
  global token
  R += i
  token += 150 * i
  Common1(3 * i)
  Common2(2 * i)
  Common3(2 * i)
def Epic(i):
  global E 
  global token
  E += i
  token += 200 * i
  Rare(2 * i)
  Common2(4 * i)
  Common3(4 * i)
def Legendary(i):
  global L
  global token
  L += i
  token += 400 * i
  Epic(3 * i)
  Common1(8 * i)


while item != "end":
  item = input("item to craft: ").title()
  if item == "Reset":
    C1 = 0
    C2 = 0
    C3 = 0
    R = 0
    E = 0
    L = 0
    M1 = 0
    M2 = 0
    M3 = 0
    token = 0
    continue
  elif item == "End":
    continue
  elif item == "Total":
    print("Material 1: " + str(M1))
    print("Material 2: " + str(M2))
    print("Material 3: " + str(M3))
    print("Common 1: " + str(C1))
    print("Common 2: " + str(C2))
    print("Common 1: " + str(C3))
    print("Rare: " + str(R))
    print("Epic: " + str(E))
    print("Legendary: " + str(L))
    print("Tokens: " + str(token))
    continue
  else:
    num = int(input("number of times to craft: "))
  if item == "Legendary":
    Legendary(num)
  elif item == "Epic":
    Epic(num)
  elif item == "Rare":
    Rare(num)
  elif item == "Common1":
    Common1(num)
  elif item == "Common2":
    Common2(num)
  elif item == "Common3":
    Common3(num)
  else:
    print("error try again")