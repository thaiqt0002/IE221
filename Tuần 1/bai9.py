import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print("a phai khac 0")
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        if x1%1==0:x1=int(x1) 
        if x2%1==0:x2=int(x2) 
        print(f"PT co hai nghiem phan biet:\n\nx1 = {x1}\nx2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        if x%1==0:x=int(x) 
        print(f"PT co nghiem kep: x1 = x2 = {x}")
    else:
        print("PTVN")