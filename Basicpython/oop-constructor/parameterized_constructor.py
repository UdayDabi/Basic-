class Shape:
    def __init__(self):
        self.color = ''
        self.borderWidth = 0.0

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color

    def setBorderWidth(self, borderWidth):
        self.borderWidth = borderWidth

    def getBorderWidth(self):
        return self.borderWidth


# s = Shape("Red", 5)
# print("Color", s.getColor())
# print("BorderWidth", s.getBorderWidth())

 # by Set Get Method
s = Shape()
s.setColor("Blue")
s.setBorderWidth(10)
print("Color", s.getColor())         # Blue
print("BorderWidth", s.getBorderWidth())   # 10
