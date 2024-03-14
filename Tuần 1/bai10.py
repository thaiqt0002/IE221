def calculate(n, citations):
    citations.sort(reverse=True)

    index = 0
    for i in range(n):
        if citations[i] >= i + 1:
            index = i + 1
        else:
            break

    return index

n = int(input())
citations = list(map(int, input().split()))

result = calculate(n, citations)
print(result)