k, t = map(int, input().split())

pass_count = t//k
locate = t%k
now = 0
if(pass_count%2 == 0):
    now = locate
else:
    now = k - locate
print(now)