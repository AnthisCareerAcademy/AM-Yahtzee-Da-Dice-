import copy
import random


def d1():
    return random.randint(1, 6)
d1()
def d2():
    return random.randint(1, 6)
d2()
def d3():
    return random.randint(1, 6)
d3()
def d4():
    return random.randint(1, 6)
d4()

def d5():
    return random.randint(1, 6)
d5()


def rolling():
    save_dice = []
    while len(save_dice) < 3:
        for i in range(1):
            prompt = input("Do you want to reroll the Dice (y/n)?")
            if prompt == "y":
                save = int(input(f"Which die/dice do you want to save out of these "
                         f"die/dice ({d1()}, {d2()}, {d3()}, {d4()}, {d5()})?"))

                if 0 < save <= 6:
                    save_dice.append(save)
                    print(save_dice)

rolling()
