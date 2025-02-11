class PlayerCharacter:
  membership = True  #Class Object Attribute

  def __init__(self , name="anonymous" , age=0):
    if(age >18):        
      self.name = name #Class Attribute
      self.age = age

  def run(self):    #method 1
    return "hallo" 
  def shout(self):
    return f"my name is {self.name}"

player1 = PlayerCharacter("Cindy",40) #Instantiating
player2 = PlayerCharacter("Tom",20)
player2.attack = 50

print(player1.run()) 
print(player1.name) 
print(player1.shout())
    