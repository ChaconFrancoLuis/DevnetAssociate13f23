
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
      pi = 3.14 # (Will hardcode pi in this example)
      circumferenceValue = pi * self.radius * 2
      return circumferenceValue

    def printCircumference(self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

    def Area(self):
        pi = 3.14
        areaValue = pi * self.radius ** 2
        return areaValue

    def printArea(self):
        myArea = self.Area()
        print ("Area of a circle with a radius of " + str(self.radius) + " is " + str(myArea))



