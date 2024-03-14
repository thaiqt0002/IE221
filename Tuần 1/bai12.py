def find(n):
    count = 0
    current_number = 1
    
    while True:
        current_str = str(current_number)
        count += len(current_str)
        if count >= n:
            print(current_str[n - (count - len(current_str)) - 1])
            return
        current_number += 1
        
n = int(input())
find(n)