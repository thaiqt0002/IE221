n = int(input())
def gt(n):
    if n==0 or n==1:
        return 1
    return n*gt(n-1)
print(gt(n))