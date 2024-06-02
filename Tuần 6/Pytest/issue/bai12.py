import numpy as np

# Check whether matrix B is the rotated form of matrx A
def rotate_matrix(A, B):
    A = np.array(A, int)
    B = np.array(B, int)
    flag = False
    for k in range(1, 4+1):
        if np.array_equal(B, np.rot90(A, k)):
            flag = True
            break
    return flag