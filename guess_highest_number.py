import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def choose_random_number():
    """Chooses a random number between 1 and 100"""
    num_array = []
    for num in range(1, 101):
        num_array.append(num)
    return random.choice(num_array)

def game_loop(guesses, lucky_number):
    while guesses > 0:
        player_guess = int(input("Make a guess: "))
        if player_guess == lucky_number:
            guesses -= 1
            return print(f"You win! The number was {lucky_number}")
        elif player_guess > lucky_number:
            guesses -= 1
            print("Too high")
            print(f"You have {guesses} left.")
        elif player_guess < lucky_number:
            guesses -= 1
            print("Too low.")
            print(f"You have {guesses} left.")
    print(f"You ran out of guesses. The number was {lucky_number}")

def start_game():
    """Loops through the game logic until user finds number or loses guesses"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        total_guesses = 10
    elif difficulty == 'hard':
        total_guesses = 5
    else:
        print("invalid response.")
    # choose random number
    winning_number = choose_random_number()
    game_loop(total_guesses, winning_number)

start_game()
    