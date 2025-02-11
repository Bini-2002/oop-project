class PlayerCharacter:
  membership = True  #Class Object Attribute

  def __init__(self , name , age):
    if(PlayerCharacter.membership):
      self.name = name #Class Attribute
      self.age = age
  def run(self):    #method 1
    return "hallo" 
  def shout(self):
    return f"my name is {self.name}"
  
  @classmethod  #hepls to add things on the __init__ methods
  def adding_things(cls , num1 , num2):
    return cls("Teddy" , num1+num2)
  
  
  

player1 = PlayerCharacter("Cindy",40) #Instantiating
player2 = PlayerCharacter("Tom",20)
player3 = PlayerCharacter.adding_things(2,3)

print(player3.name)
    