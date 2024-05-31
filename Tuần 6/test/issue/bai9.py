# Check with input (tre, dep, gau, giau), whether it is right or wrong.
def check_logic_of_life(tre, dep, gau, giau):
    out = 1
    if (tre == 1 and dep == 0) or (dep == 1 and gau == 0) or (dep == 0 and gau == 1 and giau == 0):
        out = 0
    return out