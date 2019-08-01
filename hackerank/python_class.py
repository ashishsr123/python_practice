class Box:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height

if __name__ == '__main__':
    x = Box(10,6)
    print("Area: ",x.area())