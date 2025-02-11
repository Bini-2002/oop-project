class PlayerCharacter:
  def __init__(self , name):
    self.name = name

  def run(self):    #method 1
    return "hallo" 

player1 = PlayerCharacter("Cindy") #Instantiating
player2 = PlayerCharacter("Tom")
player2.attack = 50

print(player1.run())
print(player1.name)
print(player2.attack)
    