import random

while True:
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    exit="exit"

    player=None
    while player not in choices:
        player=input("Enter rock,paper or scissors: ").lower()
        if player not in choices:
            print("Invalid input. Please enter rock,paper or scissors:")
        

    if player == computer:
        print(f"Both players selected {player,computer}. It's a tie!")
    elif player!=computer:
        print("Computer: ",computer)
        print("player: ",player)
        if computer=="rock":
            if player=="scissors":
                print("Rock smashes scissors! Computer wins!")
            elif player=="paper":
                print("Paper covers rock! Player wins!")
        elif computer=="paper":
            if player=="rock":
                print("Paper covers rock! Computer wins!")
            elif player=="scissors":
                print("Scissors cuts paper! Player wins!")
        elif computer=="scissors":
            if player=="paper":
                print("Scissors cuts paper! Computer wins!")
            elif player=="rock":
                print("Rock smashes scissors! Player wins!")
        
    player_1=print(input("exit or play: ").lower())
    if player_1!="play":
            print("You are about to exit the game ")
            break
    else:
            continue
    continue

