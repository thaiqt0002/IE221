s = str(input())

def is_lucky(i: int):
    if(i == 4 or i == 7):
        return 1
    return 0
    
def counts(s:str):
    count = 0
    for i in s:
        if(is_lucky(int(i))):
            count +=1
    return count


counted = counts(s)
if (is_lucky(counted)):
    print('YES')
else:
    print('NO')

    