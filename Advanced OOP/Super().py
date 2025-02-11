class User( object ):
  def __init__(self,email):
    self.email = email
   
  def sign_in(self):
    return 'logged in'
  
  def attack(self):
    print('do nothing')


class Wizard(User):
  def __init__(self,name="",power=0 , email = "null"):
    super().__init__(email)
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

Wizard1 = Wizard("Merlin", 60,"merlin@gmail.com")
  
print(Wizard1.email)

#Introspection
print(dir(Wizard1))

#Dunder Method







 




