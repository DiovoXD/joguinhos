import random

def roll_dice():
    while True:
        number = random.randint(1, 6)
        print("the number is: ", number)

        roll_again = input("Roll the dice again?(yes/no): ")
        if roll_again.lower() != "yes":
            break  

roll_dice()
    