class Point:

    def __init__(self,x1,y1):
        self.x = x1
        self.y = y1

    def __add__(self,other):
        return Point((self.x + other.x),(self.y + other.y))
    
    def __str__(self):
        return f"{self.x} : {self.y}"
    
    


P1 = Point(1,2)
P2 = Point(11,22)

P3 = P1 + P2
print(P3.print_point())
