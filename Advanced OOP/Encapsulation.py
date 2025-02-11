class PlayerCharacter:
  membership = True  #Class Object Attribute

  def __init__(self , name , age):
    if(PlayerCharacter.membership):

      self.name = name #Class Attribute
      self.age = age

  def run(self):    #method
    return "hello" 
  def shout(self):
    return f"my name is {self.name}"

player1 = PlayerCharacter("Cindy",40) #Instantiating
player2 = PlayerCharacter("Tom",20)
player2.attack = 50

print(player1.run()) 
print(player1.name) 
print(player1.shout())  
























































    
















