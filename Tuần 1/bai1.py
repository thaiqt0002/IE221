a, b = map(int, input().split())

max = int(((a+b) + abs(a-b))/2)
min = int(((a+b) - abs(a-b))/2)

print('max = ', max)
print('min = ', min)