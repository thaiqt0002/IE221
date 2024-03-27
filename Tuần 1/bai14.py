s = input().lower()
res = ''
for i in s:
    if i not in ["a", "o", "y", "e", "u", "i"]:
        res=res+ '.' + i
print(res)