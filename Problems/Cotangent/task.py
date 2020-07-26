import math

def cotangent(a):
    return round(math.cos(a) / math.sin(a), 10)
    
    
angle = int(input())
print(str(cotangent(math.radians(angle))))
