n, k= map(int, input().split())
s= input()
char=''
for j in range(k):
    char+= chr(65+j)
c= [s.count(i) for i in char]
print(k*min(c))