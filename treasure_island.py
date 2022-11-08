print("Welcome to Treasure Island")
direction = input("Would you like to go left or right?").lower()
if direction == "left":
    print("game over, you died")
elif direction == "right":
    isSwim = input("Would you like to swim or wait?").lower()
    if isSwim == "swim":
        print("You died.")
    elif isSwim == "wait":
        door = input("What door would you like to enter? Red, Yellow, or Blue").lower()
        if door == 'yellow' or door == 'blue':
            print('you died')
        elif door == 'red':
            print('congrats! you win!')
        else:
            print("invalid response")
    else:
        print("invalid response")
else: 
    print("invalid response")