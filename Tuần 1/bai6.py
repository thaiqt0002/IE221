m,n,h,w = map(int, input().split())

def phongbi(m,n,h,w):
    count = 0
    while m>h:
        h*=2
        count+=1
    while n>w:
        w*=2
        count+=1
    return(count)
    
print(int(min(phongbi(m,n,h,w),phongbi(n,m,h,w))))