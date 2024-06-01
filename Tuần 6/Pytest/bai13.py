# Check the result of calculating a power with faster way.
def fast_power(m, n):
    if n == 0:
        return 1
    if n%2 == 0:
        return fast_power(m, n//2)**2 % 1000000007
    else:
        return fast_power(m, n//2)**2 * m % 1000000007