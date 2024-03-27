def balance(transactions):
    balance = 0
    for item in transactions:
        if item[0] == 'D':
            balance += int(item[1])
        elif item[0] == 'W':
            balance -= int(item[1])
    return balance

N = int(input())
transactions = []

for i in range(N):
    transaction = input().split()
    transactions.append(transaction)

# TÃ­nh sá» tiá»n thá»±c
b = balance(transactions)

# In sá» tiá»n thá»±c
print(b)