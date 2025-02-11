class User( object ):
  def sign_in(self):
    return 'logged in'

class Wizard(User):
  def __init__(self,name="",power=0):
    self.name = name
    self.power = power

  def attack(self):
    print(f"attacking with power of {self.power}")

class Archer(User):
  def __init__(self,name="",num_arrows=0):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f"attacking with arrows : arrow left - {self.num_arrows}")


Wizard1 = Wizard()
Archer1 = Archer()

wizard = Wizard("Merlin", 50)
archer = Archer("Robin", 500)

wizard.attack()
archer.attack()
print(wizard.sign_in())
print(archer.sign_in())




 




