print ("Введите число a")
a = int(input())
print ("Введите число b")
b = int(input())
print ("Введите число c")
c = int(input())
if (a % b == c):
    print ("Число a даёт остаток c при делении на число b")
else:
    print ("Число a не даёт остаток c при делении на число b")
if (a*c + b == 0):
    print ("Число c является решением линейного уравнения ax + b = 0")
else:
    print ("Число c не является решением линейного уравнения ax + b = 0")
