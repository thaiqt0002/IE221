n = int(input())
tong = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        tong += i
        if (i != n // i and i != 1):
            tong += n // i
print(tong)