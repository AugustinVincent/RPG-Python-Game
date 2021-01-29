import sys
import math
from random import randint 

#  CHARACTER
class character : 
  def __init__(self, name, posX, posY, health, maxHealth, experience, experienceNeeded,  level, attacks,  inventory):
    self.name = name
    self.posX = posX
    self.posY = posY
    self.health = health
    self.maxHealth = maxHealth
    self.experience = experience
    self.experienceNeeded = experienceNeeded

    self.level = level
    self.attacks = attacks
    self.inventory = inventory

class inventory : 
  def __init__(self, offense, defense, potion, gold):
    self.offense = offense
    self.defense = defense
    self.potion = potion
    self.gold = gold

class hit:
      def __init__(self, name, dammage):
        self.name = name
        self.dammage = dammage

#                      name | posX | posY | health | maxHealth | exp | expNeeded | lvl | attacks | inventory
character = character('name',  0   ,  0   , 50     , 50   ,    0 ,    100      , 1, 'attacks',  inventory(0,0,0,0))

attackList = []

attackList.append(hit('Coup de boomerang', 10))
attackList.append(hit('Coup de tatane ', 7))
attackList.append(hit('Lance de fourchette', 5))
attackList.append(hit('Rapage de rape a parmesan', 2))

character.attacks = attackList

def expUpdate(monster) :
  if (character.experience < character.experienceNeeded):
    character.experience += monster.experienceWon

  if (character.experience > character.experienceNeeded) :
      character.level += 1
      character.experienceNeeded = math.floor(character.experienceNeeded * 1.2)
      character.experience = math.floor(character.experience - character.experienceNeeded)
      character.inventory.offense += 1
      character.inventory.defense += 1
      character.health += 10
      character.maxHealth == round(character.maxHealth * 1.5)
      if (character.experience > character.experienceNeeded) :
        print('You have level up, you got :')
        print('+ 1 of offense')
        print('+ 1 of defense')
        print('+',round(character.maxHealth * 1.5),' of max health')
        print('+ 10 of health')
        return expUpdate(monster)

  print('You are at ', character.experience, ' on ', character.experienceNeeded , '. You are level', character.level)

#  MAP


elementList = []
mapZoneList = []

class map : 
  def __init__(self, name, topLimit, bottomLimit, leftLimit, rightLimit, description):
    self.name = name
    self.topLimit = topLimit
    self.bottomLimit = bottomLimit
    self.leftLimit = leftLimit
    self.rightLimit = rightLimit
    self.description = description




#Start          name   | posX | posY | description 
spawn = map('Fortnite', 2, -2, -2, 2, "You are in your hometown : Fortnite")
mapZoneList.append(spawn)
# North
knuckles =map('Knuckles',4, -4, -4, 4 , "You are in uganda : Ugandan land of the Knuckles")
mapZoneList.append(knuckles)
# East
forrestOfGuilt = map('Forrest of guilt',6, -6, -6, 6 , "You are in the dark and steamy Forrest of guilt, where plenty have lost their lives.")
mapZoneList.append(forrestOfGuilt)
# South
lenovo = map('Lenovo',8, -8, -8, 8 , "Welcome to the advanced city of lenovo, lights and technology roams the place !")
mapZoneList.append(lenovo)
# West
fartTown = map('Fart Town',10, -10, -10, 10 , "You are in Fart Town, the smell is astrocious and the dark fog makes it hard to see.")
mapZoneList.append(fartTown)
# ---------------------------------------------------------------------------------------------------------------------------------------

def  location() :
  print('')
  print("Pos X :" ,character.posX, "Pos Y :" ,character.posY , ".", 'The Boss is in ; Pos X :', boss.posX, 'Pos Y : ', boss.posY, '.y')
  for obj in mapZoneList :

    if (character.posY <= obj.topLimit and character.posY >= obj.bottomLimit
        and character.posX <= obj.rightLimit and character.posX >= obj.leftLimit) :

        if (character.posY > obj.topLimit - 2 or character.posY < obj.bottomLimit + 2
        or character.posX >  obj.rightLimit - 2 or character.posX < obj.leftLimit + 2) :

          if (character.posY != 0 and character.posX != 0) :
            print(obj.description)
  if (character.posY == 0 and character.posX == 0):
    print(spawn.description)

# Monsters

#  MONSTER


class monster:
          def __init__(self, name, level, posX, posY, hp, defense, offense, experienceWon, attacks, elementType ):
            self.name = name
            self.level = level
            self.posX = posX
            self.posY = posY
            self.hp = hp
            self.defense = defense
            self.offense = offense
            self.experienceWon = experienceWon
            self.attacks = attacks
            self.elementType = elementType




def isThereTheBoss() :
  for obj in elementList:
    if (obj.posX == character.posX and obj.posY == character.posY and obj.elementType == 'boss'):
      print('You are fighting the Boss')
      fight(obj)

class monsterHit:
        def __init__(self, name, dammage):
            self.name = name
            self.dammage = dammage

def monsterHits(attack1, attack2, attack3, attack4) :

  monstHitList = []




  monstHitList.append(monsterHit(attack1[0], attack1[1]))
  monstHitList.append(monsterHit(attack2[0], attack2[1]))
  monstHitList.append(monsterHit(attack3[0], attack3[1]))
  monstHitList.append(monsterHit(attack4[0], attack4[1]))
  
  return monstHitList




def monsterPosition() :
  monsterPosX = randint(-10,10)
  monsterPosY = randint(-10,10)
  monsterPositions = []

  for obj in elementList :
    if (monsterPosY == obj.posY and monsterPosX == obj.posX) :
      return monsterPosition()
   
  monsterPositions.append(monsterPosX)
  monsterPositions.append(monsterPosY)
  return monsterPositions



#                      name | level | posX | posY | hp | defense | offense | experienceWon | attacks 
boss = monster('The boss of the area',100 , 10, 10,  200,20, 20, 10000, monsterHits(['Boss attaque 1', 2], ['Boss attack 2', 3], ['Boss attack 3', 1], ['Boss attack 4', 3]), 'boss')
elementList.append(boss)
#                      name | level | posX | posY | hp | defense | offense | experienceWon | attacks 
#1 - 8
monsterPos = monsterPosition()
chalon = monster('Chalon',3 ,                monsterPos[0], monsterPos[1],  30,2, 3, 400, monsterHits(['skuuuuu', 2], ['kaemameaea', 3], ['paf', 1], ['pouuufff', 3]), 'monster')
elementList.append(chalon)

monsterPos = monsterPosition()
thouinx = monster('Thouinx',5 ,              monsterPos[0], monsterPos[1],  55, 4, 5,690, monsterHits(['thouuinxaaa', 2], ['thchouinn', 2], ['paftchouin', 2], ['pouftchouin', 4]), 'monster')
elementList.append(thouinx)

monsterPos = monsterPosition()
lolo = monster('Lolo',6 ,                    monsterPos[0], monsterPos[1],  69, 6, 8,600, monsterHits(['rararrara', 3], ['warrrrrzzz', 2], ['wouf', 5], ['woufwoouf', 4]), 'monster')
elementList.append(lolo)

monsterPos = monsterPosition()
mattice = monster('Mattice',8 ,              monsterPos[0], monsterPos[1],  85, 9, 7,800, monsterHits(['mioaauuuu', 4], ['pchuuuu', 5], ['plaaaaa', 7], ['Couche', 4]), 'monster')
elementList.append(mattice)

monsterPos = monsterPosition()
jeremie = monster('Jeremie',10,              monsterPos[0], monsterPos[1],  95, 8, 11,900, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(jeremie)

monsterPos = monsterPosition()
mapamboli = monster('Mapamboli',13 ,         monsterPos[0], monsterPos[1],  115, 10, 16,1100, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(mapamboli)

monsterPos = monsterPosition()
monsterMunch = monster('Monster Munch',15 , monsterPos[0], monsterPos[1],  135, 15, 14,2500, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(monsterMunch)

monsterPos = monsterPosition()
lexpert = monster('Lexpert',17 ,            monsterPos[0], monsterPos[1],  169, 16, 18,4200, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(lexpert)

#8 - 16
monsterPos = monsterPosition()
chalon = monster('Chalon',3 ,                monsterPos[0], monsterPos[1],  30,2, 3, 400, monsterHits(['skuuuuu', 2], ['kaemameaea', 3], ['paf', 1], ['pouuufff', 3]), 'monster')
elementList.append(chalon)

monsterPos = monsterPosition()
thouinx = monster('Thouinx',5 ,              monsterPos[0], monsterPos[1],  55, 4, 5,690, monsterHits(['thouuinxaaa', 2], ['thchouinn', 2], ['paftchouin', 2], ['pouftchouin', 4]), 'monster')
elementList.append(thouinx)

monsterPos = monsterPosition()
lolo = monster('Lolo',6 ,                    monsterPos[0], monsterPos[1],  69, 6, 8,600, monsterHits(['rararrara', 3], ['warrrrrzzz', 2], ['wouf', 5], ['woufwoouf', 4]), 'monster')
elementList.append(lolo)

monsterPos = monsterPosition()
mattice = monster('Mattice',8 ,              monsterPos[0], monsterPos[1],  85, 9, 7,800, monsterHits(['mioaauuuu', 4], ['pchuuuu', 5], ['plaaaaa', 7], ['Couche', 4]), 'monster')
elementList.append(mattice)

monsterPos = monsterPosition()
jeremie = monster('Jeremie',10,              monsterPos[0], monsterPos[1],  95, 8, 11,900, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(jeremie)

monsterPos = monsterPosition()
mapamboli = monster('Mapamboli',13 ,         monsterPos[0], monsterPos[1],  115, 10, 16,1100, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(mapamboli)

monsterPos = monsterPosition()
monsterMunch = monster('Monster Munch',15 , monsterPos[0], monsterPos[1],  135, 15, 14,2500, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(monsterMunch)

monsterPos = monsterPosition()
lexpert = monster('Lexpert',17 ,            monsterPos[0], monsterPos[1],  169, 16, 18,4200, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(lexpert)

 # 16-24

monsterPos = monsterPosition()
chalon = monster('Chalon',3 ,                monsterPos[0], monsterPos[1],  30,2, 3, 400, monsterHits(['skuuuuu', 2], ['kaemameaea', 3], ['paf', 1], ['pouuufff', 3]), 'monster')
elementList.append(chalon)

monsterPos = monsterPosition()
thouinx = monster('Thouinx',5 ,              monsterPos[0], monsterPos[1],  55, 4, 5,690, monsterHits(['thouuinxaaa', 2], ['thchouinn', 2], ['paftchouin', 2], ['pouftchouin', 4]), 'monster')
elementList.append(thouinx)

monsterPos = monsterPosition()
lolo = monster('Lolo',6 ,                    monsterPos[0], monsterPos[1],  69, 6, 8,600, monsterHits(['rararrara', 3], ['warrrrrzzz', 2], ['wouf', 5], ['woufwoouf', 4]), 'monster')
elementList.append(lolo)

monsterPos = monsterPosition()
mattice = monster('Mattice',8 ,              monsterPos[0], monsterPos[1],  85, 9, 7,800, monsterHits(['mioaauuuu', 4], ['pchuuuu', 5], ['plaaaaa', 7], ['Couche', 4]), 'monster')
elementList.append(mattice)

monsterPos = monsterPosition()
jeremie = monster('Jeremie',10,              monsterPos[0], monsterPos[1],  95, 8, 11,900, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(jeremie)

monsterPos = monsterPosition()
mapamboli = monster('Mapamboli',13 ,         monsterPos[0], monsterPos[1],  115, 10, 16,1100, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(mapamboli)

monsterPos = monsterPosition()
monsterMunch = monster('Monster Munch',15 , monsterPos[0], monsterPos[1],  135, 15, 14,2500, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(monsterMunch)

monsterPos = monsterPosition()
lexpert = monster('Lexpert',17 ,            monsterPos[0], monsterPos[1],  169, 16, 18,4200, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(lexpert)

#24-32

chalon = monster('Chalon',3 ,                monsterPos[0], monsterPos[1],  30,2, 3, 400, monsterHits(['skuuuuu', 2], ['kaemameaea', 3], ['paf', 1], ['pouuufff', 3]), 'monster')
elementList.append(chalon)

thouinx = monster('Thouinx',5 ,              monsterPos[0], monsterPos[1],  55, 4, 5,690, monsterHits(['thouuinxaaa', 2], ['thchouinn', 2], ['paftchouin', 2], ['pouftchouin', 4]), 'monster')
elementList.append(thouinx)

lolo = monster('Lolo',6 ,                    monsterPos[0], monsterPos[1],  69, 6, 8,600, monsterHits(['rararrara', 3], ['warrrrrzzz', 2], ['wouf', 5], ['woufwoouf', 4]), 'monster')
elementList.append(lolo)

mattice = monster('Mattice',8 ,              monsterPos[0], monsterPos[1],  85, 9, 7,800, monsterHits(['mioaauuuu', 4], ['pchuuuu', 5], ['plaaaaa', 7], ['Couche', 4]), 'monster')
elementList.append(mattice)

jeremie = monster('Jeremie',10,              monsterPos[0], monsterPos[1],  95, 8, 11,900, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(jeremie)

mapamboli = monster('Mapamboli',13 ,         monsterPos[0], monsterPos[1],  115, 10, 16,1100, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(mapamboli)

monsterMunch = monster('Monster Munch',15 , monsterPos[0], monsterPos[1],  135, 15, 14,2500, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(monsterMunch)

lexpert = monster('Lexpert',17 ,            monsterPos[0], monsterPos[1],  169, 16, 18,4200, monsterHits(['PNL', 5], ['congo', 4], ['bortdaue', 7], ['42', 8]), 'monster')
elementList.append(lexpert)

# SHOP

class shops :
  def __init__(self, posX, posY, text) :
    self.posX = posX
    self.posY = posY
    self.text = text
  elementType = 'shop'


spawnNorthShop = shops(  0,  2, "North shop")
elementList.append(spawnNorthShop)

spawnEastShop = shops(  2,  0, "East shop")
elementList.append(spawnEastShop)

spawnSouthShop = shops(  0, -2, "South shop")
elementList.append(spawnSouthShop)

spawnWestShop = shops( -2,  0, "West shop")
elementList.append(spawnWestShop)




knucklesNorthShop = shops(  0,  4, "North shop")
elementList.append(knucklesNorthShop)

knucklesEastShop = shops(  4,  0, "East shop")
elementList.append(knucklesEastShop)

knucklesSouthShop = shops(  0, -4, "South shop")
elementList.append(knucklesSouthShop)

knucklesWestShop = shops( -4,  0, "West shop")
elementList.append(knucklesWestShop)




forestNorthShop = shops(  0,  6, "North shop")
elementList.append(forestNorthShop)

forestEastShop = shops(  6,  0, "East shop")
elementList.append(forestEastShop)

forestSouthShop = shops(  0, -6, "South shop")
elementList.append(forestSouthShop)

forestWestShop = shops( -6,  0, "West shop")
elementList.append(forestWestShop)




lenovoNorthShop = shops(  0,  8, "North shop")
elementList.append(lenovoNorthShop)

lenovoEastShop = shops(  8,  0, "East shop")
elementList.append(lenovoEastShop)

lenovoSouthShop = shops(  0, -8, "South shop")
elementList.append(lenovoSouthShop)

lenovoWestShop = shops( -8,  0, "West shop")
elementList.append(lenovoWestShop)




    



def isThereAShop() :
  for shop in elementList : 
    if (character.posX == shop.posX and character.posY == shop.posY and shop.elementType == 'shop') :
      print('Welcome in the ', shop.text, ', buy something !')
      print('You have', character.inventory.gold, ' gold')
      print('1. Buy offense : +1 offense')
      print('2. Buy defense : +1 defense')
      print('3. Buy potion : Heal yourself completely')
      print('4. Exit shop')

      answer = choiceNumber(4)
      if (answer == 1) :
        if (character.inventory.gold > 0) :
          character.inventory.gold -=1
          character.inventory.offense +=1
          return isThereAShop()

        else : 
          print('You have no gold')
          return isThereAShop()
      if (answer == 2) :
        if (character.inventory.gold > 0) :
          character.inventory.gold -=1
          character.inventory.defense +=1
          return isThereAShop()

        else : 
          print('You have no gold')
          return isThereAShop()
      if (answer == 3) :
        if (character.inventory.gold > 0) :
          character.inventory.gold -=1
          character.inventory.potion +=1
          return isThereAShop()

        else : 
          print('You have no gold')
          return isThereAShop()

      if (answer == 4) : 
        return



# POTION + ITEMS


def itemPosition() :
  itemPosX = randint(-10,10)
  itemPosY = randint(-10,10)
  itemPositions = []

  for obj in elementList :
    if (itemPosY == obj.posY and itemPosX == obj.posX) :
      return itemPosition()
   
  itemPositions.append(itemPosX)
  itemPositions.append(itemPosY)
  return itemPositions

      


class potions :
  def __init__(self, healthGiven, posX, posY):
    self.healthGiven = healthGiven
    self.posX = posX
    self.posY = posY
  elementType = 'potion'


for i in range(50) :
  pos = itemPosition()
  potion = potions(5,pos[0], pos[1])
  elementList.append(potion)

def isThereAPotion() :
  for potion in elementList : 
    if (character.posX == potion.posX and character.posY == potion.posY and potion.elementType == 'potion') :
      print('')
      print('You found a potion, it went directly into your inventory')
      elementList.remove(potion)
      character.inventory.potion += 1
      print('')

# ARMOR



class armors :
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
  elementType = 'armor'




for i in range(50) :
  pos = itemPosition()
  armor = armors(pos[0], pos[1])
  elementList.append(armor)

def isThereAnArmor() :
  for armor in elementList : 
    if (character.posX == armor.posX and character.posY == armor.posY and armor.elementType == 'armor') :
      print('')
      print('You found an armor, it went directly into your inventory')
      elementList.remove(armor)
      character.inventory.defense += 1
      print('')

# SWORD



class swords :
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
  elementType = 'sword'




for i in range(50) :
  pos = itemPosition()
  sword = swords(pos[0], pos[1])
  elementList.append(sword)


def isThereASword() :
  for sword in elementList : 
    if (character.posX == sword.posX and character.posY == sword.posY and sword.elementType == 'sword') :
      print('')
      print('You found a sword, it went directly into your inventory, your offense has been upgraded')
      elementList.remove(sword)
      character.inventory.offense += 1
      print('')

# GOLDS

class golds :
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
  elementType = 'gold'

# gold = golds(itemPosition()[0], itemPosition()[1])


for i in range(200) :
  pos = itemPosition()
  gold = golds(pos[0], pos[1])
  elementList.append(gold)



def isThereAGold() :
  for gold in elementList : 
    if (character.posX == gold.posX and character.posY == gold.posY and gold.elementType == 'gold') :
      print('')
      print('You found a gold coin, it went directly into your inventory')
      character.inventory.gold += 1
      elementList.remove(gold)
      print('')






# Mieux gerer le positionnement des monstres
def monstersPosition(pos) :
  monsterPosX = randint(-10,10)
  monsterPosY = randint(-10,10)
  for obj in elementList :
    if (monsterPosY == obj.posY and monsterPosX == obj.posX) :
       return monstersPosition(monster)
    else :
      if (pos == 'x'):
         return monsterPosX
      if (pos == 'y') :
         return monsterPosY





def choiceNumber(numberOfChoices):
  number = int(input())
  if (number > 0 and number <= numberOfChoices) :
    print('-------------------------------------------------------------------------------')
    return number
  else : 
    print('Choose again')
    return choiceNumber(numberOfChoices)



#MAIN MENU
def mainMenu() :
  print("--------RPG GAME--------")
  print("1. Play")
  print("2. About")
  print("3. Exit")
  print("Which number would you like to choose?")

  answer = choiceNumber(3)
  if (answer == 1) :
    startGame()
  if (answer == 2) :
    About()
  if (answer == 3) :
    Exit()



def startGame() :
  print('')
  print("Welcome to your hometown village 'Fortnite Village', the place where you were born. Who are you? What are you called?")
  print("Name :")
  character.name = str(input())
  print('')
  print('Welcome ' , character.name , ' !')
  print("Your village has been recently attacked by gremlins, they have become one of the most powerful armies in the kingdom,") 
  print("however they suffered too many losses and had to run away from Fortnite Village. It is said they are in the North East of Kanye also called Fart Town ")
  print("you better get ready for a fight against the  Gremlin king aka 'Voster', hurry up and save the kingdom. You're our only hope !") 
  print('')
  print("To be prepared, you should scavange the roaming areas and get stronger, will you accept this quest?")
  print("1. Y")
  print("2. N")
  interaction()


def About():
  print ("Credit : Arthur Thouin & Augustin Vincent & Lowenn Ragot")
  print ("That's about it, thanks for playing")
  print ("")
  print ("copyright although I doubt someone wants to steal our game")
  print ("")
  print ("contact us if you want to :")
  print ("Instagram : @voster__ / @augustin.vct / @arthurthn ")
  print ("Twitter : @voster_ / @augustinvct / @arthurthn ")
  print ("linkedin : Lowenn Ragot / Augustin Vincent / Arthur Thouin")
  print ("We're going to bring you back to the main menu, if you want to play the game !")
  mainMenu()

def Exit() :
  print("Thank you for everything, have a good day") 
  sys.exit(0)

#JEU

#Beginning of the game

def interaction() :
  answer = choiceNumber(2)
  if (answer == 1) :
    print("That's the spirit !")
    print('')
  elif (answer == 2) :
    print("I mean... You don't have much of a choice ._.'")
    print('')
    print("...")
    print('')
  print("Whatever, you are in the middle of Kanye, which direction would you wish to go to? Kanye North, Kanye East, Kanye South, Kanye West?")
  print('')
  print("Before you choose, don't forget to grab yourself this level 1 gold,level 1 defense and 5 gold coins") 
  character.inventory.level = 1
  character.inventory.offense = 1
  character.inventory.defense = 1
  character.inventory.gold = 5

  action()


def printStats() :
  print('Your stats :' )
  print('')
  print('HP : ', character.health, '/', character.maxHealth)
  print('Level : ', character.level)
  print('Experience : ', character.experience, '/', character.experienceNeeded)
  print('Offense : ', character.inventory.offense)
  print('Defense : ', character.inventory.defense)
  print('Healing potion : ', character.inventory.potion )
  print('Gold : ', character.inventory.gold)
  print('')



def action() :
  printStats()
  location()
  print('')
  print("Which side would you wish to go to?")
  print("1. North")
  print("2. East")
  print("3. South")
  print("4. West")
  numberOfChoice = 4
  if (character.inventory.potion > 0) :
    numberOfChoice = 5
    print('5. Use a potion')
  else : 
    numberOfChoice = 4
  answer = choiceNumber(numberOfChoice)

  if (answer == 1) :

    if (character.posY < 10) :
     character.posY += 1
    else :
      print("You can't go there, it's the edge of the world !")
  elif (answer == 2) :

    if (character.posX < 10) :
      character.posX += 1
    else :
      print("You can't go there, it's the edge of the world !")
  elif (answer == 3) :

    if (character.posY > -10) :
      character.posY -= 1
    else :
      print("You can't go there, it's the edge of the world !")
  elif (answer == 4) :

    if (character.posX > -10) :
     character.posX -= 1
    else :
      print("You can't go there, it's the edge of the world !")
  
  elif (answer == 5) :
    print('You drunk a potion, you are noow full health')
    character.inventory.potion -= 1
    character.health = character.maxHealth

  isThereAPotion()
  isThereAnArmor()
  isThereASword()
  isThereAGold()

  isThereAShop()
  isThereAMonster()
  isThereTheBoss()
  action()
  


def isThereAMonster() :
  for obj in elementList:
    if (obj.posX == character.posX and obj.posY == character.posY and obj.elementType == 'monster'):
      fight(obj)
    

def fight(monster) : 
  print("You are going to fight", monster.name,". " , monster.name , "is level", monster.level , "and has" , monster.hp , "HP")
  print("He has", monster.offense,"attack and " , monster.defense , "defense.")
  fightChoice(monster)

def characterAttack(monster, attackNumber) :
  print("You used ", character.attacks[attackNumber].name ,"on ",  monster.name)
  monster.hp = monster.hp - (character.attacks[attackNumber].dammage * character.inventory.offense) / monster.defense
  if (monster.hp > 0) :
      print("You have inflicted ", round((character.attacks[attackNumber].dammage * character.inventory.offense) / monster.defense)," damage on ",  monster.name, '. Hes has ', round(monster.hp), ' HP remaining')
  elif( monster.hp <= 0) :
    print("You have inflicted ", round((character.attacks[attackNumber].dammage * character.inventory.offense) / monster.defense)," damage on ",  monster.name, '.', monster.name, 'is dead !')


def fightChoice(monster) :
  print("------------------------------------------------------------------------------------")
  print("What would you like to do?")
  print("1. ", character.attacks[0].name)
  print("2. ", character.attacks[1].name)
  print("3. ", character.attacks[2].name)
  print("4. ", character.attacks[3].name)
  print("5. Runaway" )
  answer = choiceNumber(5)
  while (answer > 5 and answer <= 0) :
    print("Choose again")
  if (answer == 1) :
    characterAttack(monster, 0)
  elif (answer == 2) :
    characterAttack(monster, 1)
  elif (answer == 3) :
    characterAttack(monster, 2)
  elif (answer == 4) :
    characterAttack(monster, 3)
  elif (answer == 5) :
    action()
  if (monster.hp > 0):
    monsterAttack = monster.attacks[randint(0,3)]
    character.health = character.health - (monsterAttack.dammage * monster.offense) / character.inventory.defense
    print(monster.name, "inflicted", round((monsterAttack.dammage * monster.offense) / character.inventory.defense), 'damage')
    print('You have ', round(character.health), 'hp')
    if (character.health <= 0) :
      Exit()
    fightChoice(monster)
  elif (monster.elementType == 'monster') :
    print('You won !')
    elementList.remove(monster)
    expUpdate(monster)
    action()
  elif (monster.elementType == 'boss') :
    print('You finished the game, well done you are the fck boss my man ')
    Exit()

mainMenu()
