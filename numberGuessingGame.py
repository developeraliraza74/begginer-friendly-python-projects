import random
generatedNum = random.randint(1,100) 

attempts = 0
while True:
    try: 
        userNum = int(input("Enter a number b/w (1 to 100) : "))
    

        if(generatedNum > userNum):
            print ("too low")
            attempts += 1
        elif (generatedNum < userNum):
            print("too high")
            attempts += 1
        else:
            print(f"Congratulations! You guessed it {generatedNum}")
            print(f'You guessed the {generatedNum} in {attempts} attempts')
            break
    except ValueError:
        print("Please enter a number ")

   