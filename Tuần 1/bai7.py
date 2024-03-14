x = int(input())
higher = 0
def fibo(i,x,a,b):
    if i == x:
        if (a>b):
            return(a)
        return b
    if (a > b):
        return(fibo(i+1,x,a, a+b))
    return (fibo(i+1, x, a+b, b))
    
    
    
if (x<1 or x>30):
    print('So', x, 'khong nam trong khoang [1,30].' )
elif x<=2:
    print(x)
else:
    higher = fibo(2,x,1,1)
    print(higher)  