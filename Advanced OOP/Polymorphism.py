class User( object ):
  def sign_in(self):
    return 'logged in'
  
  def attack(self):
    print('do nothing')


class Wizard(User):
  def __init__(self,name="",power=0):
    self.name = name
    self.power = power

  def attack(self):
    User.attack(self)
    return f"attacking with power of {self.power}"

class Archer(User):
  def __init__(self,name="",num_arrows=0):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f"attacking with arrows : arrow left - {self.num_arrows}")

Wizard1 = Wizard("Merlin", 60)
Archer1 = Archer("Robin", 30)

def player_attack(char):
  char.attack()

#player_attack(Wizard1)
#player_attack(Archer1) 
print(Wizard1.attack())

#To access both the User and Wizard methods: we gonna follow the following steps 






 




