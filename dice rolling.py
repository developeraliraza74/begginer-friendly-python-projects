# first attempt
# import random
# answer = ""

# def roll():
#     while True:
#         answer = input("Roll the dice (y/n) : ")
#         if(answer == 'y'):
#             print(f'({random.randint(1,6)}, {random.randint(1,6)})')
#             roll()
        
#         elif(answer == 'n'):
#             print("Thank You for playing my game :-)")
#             exit()
#         else:
#             print("invalid choice") 
#             roll()

# roll()


# second attempt

import random
totalDiceRolled = 0

while True:
    ans = input("dice the roll (y/n) : ").lower()
    if(ans == 'y'):
        print(f'({random.randint(1,6)}, {random.randint(1,6)})')
        totalDiceRolled += 1
    elif(ans == 'n'):
        print("Thanks for playing :-)")
        print(f"You rolled the dice {totalDiceRolled} times ")
        break
    else:
        print("Invalid Answer")


