from math import sqrt
a,b,c = map(float, input().split())

x = 0
x = pow(a,5) - 2*sqrt(abs(b)) + a*b*c
print(f"{x:.2f}")