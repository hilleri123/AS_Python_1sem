import math

def DegToRad(D):
    return D * math.pi / 180
#пример 
angle = float(input("Введите угол в градусах: "))
print("В радианах:", DegToRad(angle))
