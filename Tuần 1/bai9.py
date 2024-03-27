a = float(input())
b = float(input())
c = float(input())

b/=2
delta = b**2 - a*c 
vt = -b/a

if(delta > 0):
    vp = delta**0.5/a
    x1 = -vt+vp
    x2 = -vt-vp
    if (a>0):
        print('PT co hai nghiem phan biet:\n\nx1 =',int(x1) if x1.is_integer() else x1, '\nx2 =',int(x2) if x2.is_integer() else x2)
    else: 
        print('PT co hai nghiem phan biet:\n\nx1 =',int(x2) if x2.is_integer() else x2, '\nx2 =',int(x1) if x1.is_integer() else x1)

    
elif (delta == 0):
    x = vt
    print('PT co nghiem kep: x1 = x2 =', int(x) if x.is_integer() else x)
else:
    print('PTVN')
    