def who_wins(s):

    count_R = s.count('R')
    count_B = s.count('B')

    if len(s) < 2 or (count_R == 0) or (count_B == 0):
        return "Lose"
    

    if count_R % 2 == 0 and count_B % 2 == 0:
        return "Lose"
    

    return "Win"


s = input().strip()

result = who_wins(s)
print(result)