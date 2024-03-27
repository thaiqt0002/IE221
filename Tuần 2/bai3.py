import random

class Dice:
    num: int 
    
    def __init__(self):
        self.num = None

    def roll(self):
        self.num = random.randint(1, 6)
        return self.num

n = int(input("Enter the number of rolls: "))

dice = Dice()

frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
probability = {face: freq / n for face, freq in frequency.items()}

for _ in range(n):
    face = dice.roll()
    frequency[face] += 1
    
for face in range(1, 7):
    print(f"Mặt {face}: Tần suất = {frequency[face]}, tỉ lệ = {probability[face]}")