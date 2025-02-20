import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():
    print("Welcome to the dice roller!")
    player1 = input("Enter your name: ")
    player2 = input("Enter your name: ")

    player1_roll = roll_dice()
    player2_roll = roll_dice()

    print(f"{player1} rolled a {player1_roll}")
    print(f"{player2} rolled a {player2_roll}")

    if player1_roll > player2_roll:
        print(f"{player1} wins!")
    elif player1_roll < player2_roll:
        print(f"{player2} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()