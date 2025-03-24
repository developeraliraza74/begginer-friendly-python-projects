import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

# try to add emojis 
emojis = {ROCK : "", PAPER : "", SCISSORS : ""}




choices = tuple(emojis.keys()) # tuple for selection

computer_selection = random.choice(choices) # computer have a choice to select one of the among

def get_user_selection(): # to get user selection
     while True:
        user_selection = input("rock, paper, scissor (r,p,s) : ").lower()
        if user_selection not in choices:
            print("Invalid Choice! Try again")
        else:
            return user_selection


def display_selections(user_selection): # to display the selections of computer and user
    print(f'You choose : {user_selection}')
    print(f'Computer choose : {computer_selection}')
          
def determine_winner(user_selection): # determine winners based on conditions 
        if(user_selection == computer_selection):

                print("Tie!")
                
        elif(user_selection == ROCK and computer_selection == SCISSORS or
            user_selection == SCISSORS and computer_selection == PAPER or
            user_selection == PAPER and computer_selection == ROCK):

            print("You win")

        else:

           print("You Lose")

def playGame(): # an initial function to play the actual game 
     while True:
        user_selection = get_user_selection()
        display_selections(user_selection)
        determine_winner(user_selection)
        
        replay = input("Do you want to play again (y/n): ")
        if replay == 'n':
                print("Thanks for Playing ")
                break
     




playGame()
