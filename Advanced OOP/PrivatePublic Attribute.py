#There is no true privavcy in python OOP like Java

class PlayerCharacter:
  membership = True  

  def __init__(self , name , age):
    if(PlayerCharacter.membership):

      self.name = name 
      self.age = age

  def run(self):    
    return "hello" 
  def shout(self):   
    return f"my name is {self.name}"

player1 = PlayerCharacter("Cindy",40) 
player2 = PlayerCharacter("Tom",20)

player1.name = "!!!"
player1.shout = "BOOOO"

print(player1.shout)
 

























































    
















