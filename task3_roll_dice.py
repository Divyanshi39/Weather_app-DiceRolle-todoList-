import random
dice_art={1:("┌───────┐",
             "|       |",
             "|   ●   |",
             "|       |",
             "└───────┘"),
          2:("┌───────┐",
             "|●      |",
             "|       |",
             "|      ●|",
             "└───────┘"),
          3:("┌───────┐",
             "|●      |",
             "|   ●   |",
             "|      ●|",
             "└───────┘"),
          4:("┌───────┐",
             "|●     ●|",
             "|       |",
             "|●     ●|",
             "└───────┘"),
          5:("┌───────┐",
             "|●     ●|",
             "|   ●   |",
             "|●     ●|",
             "└───────┘"),
          6:("┌───────┐",
             "|●     ●|",
             "|●     ●|",
             "|●     ●|",
             "└───────┘")
}
dice=[]
total=0
totals=0
product=1
products=1
no_of_dice= int(input("how many number of dice?"))
for die in range(no_of_dice):
    dice.append(random.randint(1,6))

for die in range(no_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total+=die
    totals+=total
    print(f"totals:{totals}")
for die in dice:
    product*=die
    products*=product
    print(f"products:{products}")