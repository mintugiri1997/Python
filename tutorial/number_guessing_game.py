import random

win_number = random.randint(1, 100)
guess_times = 1
game_over = False

guessed_number = int(input("Guess a number between 1 to 100 : "))

while not game_over:
    if guessed_number == win_number:
        print(f"You Win, guessed in {guess_times} time")
        game_over = True
    else:
        if guessed_number < win_number:
            print("You guessed low number")
        else:
            print("You guessed high number")

        guess_times += 1
        guessed_number = int(input("Try again, Guess a number between 1 to 100 : "))