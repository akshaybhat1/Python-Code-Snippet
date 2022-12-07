class Employee:
  def __init__(self, name, tech, age):
    self.name=name 
    self.tech=tech
    self.age=age 
  def greet(self):
    return f'Hi, {self.name} welcome to our company'
  def tasks(self, task):
    self.task=task+1
    return f'{self.name} has worked on {self.task} tasks'


class Founders(Employee):
  def __init__(self, name, tech, age, pos):
    self.name=name 
    self.age=age
    self.tech=tech
    self.position=pos
  def stocks(self, stock):
    self.stock=stock+10
    return f'{self.name} is a {self.position} and holds {self.stock} stocks'
 
jake=Employee('Jake','ruby', 35)
print(jake.greet())
print(jake.tasks(56))
print(jake.tech)
# print(jake.position)

richard=Founders('Richard', 'fullstack',26,'CEO')
print(richard.greet())
print(richard.tasks(89))
print(richard.position)
print(richard.stocks(150))