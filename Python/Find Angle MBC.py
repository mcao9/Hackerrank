import math

AB = int(input())
BC = int(input())

def hypotnuse(AB, BC):
    return math.sqrt(AB ** 2 + BC ** 2)

print(str(round(math.degrees(math.acos(BC/hypotnuse(AB, BC))))) + '°')