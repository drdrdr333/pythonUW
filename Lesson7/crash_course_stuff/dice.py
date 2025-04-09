from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    
    def roll_dice(self):
        roll = randint(1, self.sides)
        print(f"You rolled a {roll}")
        return roll
    


d = Dice()

results_6_side = []

for i in range(10):
    results_6_side.append(d.roll_dice())

print(results_6_side)

t = Dice(10)

results_10_side = []

for i in range(10):
    results_10_side.append(t.roll_dice())
print(results_10_side)

tw = Dice(20)

results_20_side = []

for i in range(10):
    results_20_side.append(tw.roll_dice())

print(results_20_side)