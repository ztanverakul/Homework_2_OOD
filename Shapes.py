class Shape:
  def __init__(self, database):
    self.database = database

  def SortShape(self):
    self.database.sort(key=len)

  def DisplayShape(self):
    for i in range(0, len(self.database)):
      print("the shape is a", self.database[i])
  
  def DatabaseSize(self):
    print("The number of shapes in the database is", len(self.database))

class Circle(Shape):
  def getname():
    return('Circle')

class Triangle(Shape):
  def getname(): 
    return('Triangle')

class Square(Shape):
  def getname():
    return('Square') 

database = []

database.append(Circle.getname())
database.append(Triangle.getname())
database.append(Square.getname())

currentinst = Shape(database)
currentinst.SortShape()
currentinst.DatabaseSize()
currentinst.DisplayShape()
