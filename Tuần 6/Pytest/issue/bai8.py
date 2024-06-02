# Check if a number is a nearly-lucky number.
def is_nearly_lucky_number(n):
    n = str(n)
    temp = str(n.count('4') + n.count('7'))
    return (temp.count('4') + temp.count('7') == len(temp))