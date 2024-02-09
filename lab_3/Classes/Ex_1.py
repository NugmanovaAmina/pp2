class Person:
  def __init__(self):
    self.string = input()

  def myfunc(self):
    print(self.string.upper())

p1 = Person()
p1.myfunc()