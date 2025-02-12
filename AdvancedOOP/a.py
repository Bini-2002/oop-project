class PlayerCharacter:
  membership = True  #Class Object Attribute

  def __init__(self , name , age):
    if(PlayerCharacter.membership):

      self.name = name #Class Attribute
      self.age = age

  def run(self):    #method
    return "hello" 
  def shout(self): #Abstracted from the user how it is built 
    return f"my name is {self.name}"

player1 = PlayerCharacter("Cindy",40) #Instantiating
player2 = PlayerCharacter("Tom",20)

player1.name = "!!!"
player1.shout = "BOOOO"
#But here the "shout" atribute is changed.
print(player1.shout)
 

























































    
















