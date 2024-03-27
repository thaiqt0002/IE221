rows = 5
cols = 5

locate_row = 0
locate_col = 0
    
array = [[0 for j in range(cols)] for i in range(rows)]

for i in range (rows):
    row_values = list(map(int, input().split()))
    for m, value in enumerate(row_values):
        if value==1:
            locate_row = i
            locate_col = m
    array.append(row_values)

step = abs(locate_row-2) + abs(locate_col-2)
print(step)