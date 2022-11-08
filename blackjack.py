import random
cards = [11, 2, 3, 4, 10]

def determine_winner(player_cards, computer_cards):
    """Takes two sets of cards and see which sum is higher"""
    player_sum = sum(player_cards)
    computer_sum = sum(computer_cards)
    if player_sum > computer_sum:
        return "You Win!"
    elif computer_sum > player_sum:
        return "You Lose."
    elif player_sum == computer_sum:
        return "Draw."

def black_jack_game(): 
    """Runs the entire Black Jack game."""
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip() == 'y':
        lost = False
        # Set initial cards for player and computer
        player_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards), random.choice(cards)]
        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        hit = 'y'
        # Let player keep picking cards.
        while hit == 'y':
            if input("Type 'y' to get another card, type 'n' to pass: ").lower().strip() == 'n':
                break
            else:
                player_cards.append(random.choice(cards))
                if sum(player_cards) > 21:
                    for num in range(0, len(player_cards)):
                        if player_cards[num] == 11:
                            player_cards[num] = 1
                    if sum(player_cards) > 21:        
                        print("BUST.")
                        lost = True
                        hit == 'n'
                        break
                print(f"Your cards: {player_cards}")
                print(f"Computer's first card: {computer_cards[0]}")
        # If the player has not busted, let the computer pick cards
        if not lost:
            while sum(computer_cards) < 17:
                computer_cards.append(random.choice(cards))
            if sum(computer_cards) > 21:
                print(f"Your final hand: {player_cards}")
                print(f"Computer final hand: {computer_cards}")
                print("You Win!")
                black_jack_game()
            # If computer hasn't busted, determine the winner
            else:
                outcome = determine_winner(player_cards, computer_cards)
                print(f"Your final hand: {player_cards}")
                print(f"Computer final hand: {computer_cards}")
                print(outcome)
                black_jack_game()
        else:
            black_jack_game()

black_jack_game()
        
