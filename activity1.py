class Point:
    def __init__(self,x1=0,y1=0):
        self.x = x1
        self.y = y1

    def print_point(self):
        return f"{self.x} : {self.y}"
    

P1 = Point(10,20)
P2 = Point(11,21)

# P3 = P1 + P2

print(P1.print_point())
print(P2.print_point())

# print(P3.print_point(44,55))