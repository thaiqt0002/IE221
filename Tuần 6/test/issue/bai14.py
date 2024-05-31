# Calculate mean of a list.
def find_mean(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    return sum / len(A)