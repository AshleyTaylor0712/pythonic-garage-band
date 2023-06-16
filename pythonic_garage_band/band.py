class Band:

  instances = []

  def __init__(self, name, members):
    self.name = name
    self.members = members
    Band.instances.append(self)

  def play_solos(self):
    solos = []
    for musician in self.members:
      solos.append(musician.play_solo())
    return solos
  
  def __str__(self):
    return f"Band: {self.name}"
  
  def __repr__(self):
    return f"{self.__class__.__name__} instances.name {self.name}= "
  
  @classmethod
  def to_list(cls):
    return cls.instances

class Musician:
  def __init__(self, name, instrument, solo):
    self.name = name
    self.instrument = instrument
    self.solo = solo
  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"
  def __repr__(self):
    return f"{self.__class__.__name__} instance. Name = {self.name}"
  def play_solo(self):
    return self.solo
  
  
class Guitarist(Musician):
  def __init__(self, name):

    super().__init__(name, "guitar", "face melting guitar solo")
  def get_instrument(self):
    return self.instrument
  
class Bassist(Musician):
  def __init__(self, name):
    super().__init__(name, "bass", "bom bom buh bom")
  def get_instrument(self):
    return self.instrument

class Drummer(Musician):
  def __init__(self, name):
    super().__init__(name, "drums", "rattle boom crash")
  def get_instrument(self):
    return self.instrument
  

  
# if __name__ == '__main__':
