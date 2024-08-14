import random
def get_choices():
    player_choice = input("choose any(rock, paper, scissors):")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choice = {"player":player_choice, "computer":computer_choice}
    return choice
def check_win(player, computer):
    print(f"You choose {player}, computer choose {computer}")
    if player==computer:
        return "It's a tie"
    elif player=="rock" :
        if computer=="scissors":
            return " rock smashes scissors! you win"
        else:
            return "paper covers rock! you lose"
    elif player=="paper" :
        if computer=="rock":
            return " paper covers rock! you win"
        else:
            return "scissors cuts paper! you lose"
    elif player=="scissors" :
        if computer=="paper":
            return " scissors cuts paper! you win"
        else:
            return "rock smashes scissors! you lose"
choice = get_choices()
result = check_win(choice["player"], choice["computer"])
print(result)
    
    
    
    
          


