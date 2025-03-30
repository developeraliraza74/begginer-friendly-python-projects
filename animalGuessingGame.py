import random

no_of_questions = 0

score = 0

def again():
    replay = input("Do you want to play again : ").lower()
    if replay == 'yes':
        playQuiz()
    else:
        print("Thank you so much ")
        return


questions = [
    {"question": "Which is the largest animal in the world?", "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"], "answer": "Blue Whale"},
    {"question": "Which animal is known as the 'King of the Jungle'?", "options": ["Tiger", "Lion", "Bear", "Wolf"], "answer": "Lion"},
    {"question": "Which is the fastest land animal?", "options": ["Cheetah", "Horse", "Leopard", "Kangaroo"], "answer": "Cheetah"},
    {"question": "Which bird can mimic human speech?", "options": ["Parrot", "Eagle", "Crow", "Sparrow"], "answer": "Parrot"},
    {"question": "How many legs does a spider have?", "options": ["6", "8", "10", "12"], "answer": "8"},
    {"question": "Which mammal can fly?", "options": ["Bat", "Squirrel", "Owl", "Pigeon"], "answer": "Bat"},
    {"question": "Which animal is known for playing dead?", "options": ["Opossum", "Chameleon", "Rabbit", "Turtle"], "answer": "Opossum"},
    {"question": "Which sea creature has three hearts?", "options": ["Starfish", "Octopus", "Whale", "Seahorse"], "answer": "Octopus"},
    {"question": "What is the only marsupial found in North America?", "options": ["Kangaroo", "Koala", "Opossum", "Wombat"], "answer": "Opossum"},
    {"question": "Which animal is known as the 'Ship of the Desert'?", "options": ["Horse", "Camel", "Donkey", "Llama"], "answer": "Camel"},
    {"question": "Which animal is famous for its black and white stripes?", "options": ["Tiger", "Zebra", "Panda", "Skunk"], "answer": "Zebra"},
    {"question": "Which fish is known as the fastest in the ocean?", "options": ["Tuna", "Swordfish", "Sailfish", "Mackerel"], "answer": "Sailfish"},
    {"question": "What is the only continent where giraffes live in the wild?", "options": ["Asia", "Africa", "South America", "Australia"], "answer": "Africa"},
    {"question": "What is a baby goat called?", "options": ["Calf", "Foal", "Kid", "Cub"], "answer": "Kid"},
    {"question": "Which reptile can change its skin color?", "options": ["Iguana", "Chameleon", "Gecko", "Cobra"], "answer": "Chameleon"},
    {"question": "Which bird is a universal symbol of peace?", "options": ["Sparrow", "Dove", "Eagle", "Peacock"], "answer": "Dove"},
    {"question": "What is the slowest animal in the world?", "options": ["Snail", "Tortoise", "Sloth", "Earthworm"], "answer": "Sloth"},
    {"question": "Which of these animals is NOT a mammal?", "options": ["Dolphin", "Bat", "Crocodile", "Whale"], "answer": "Crocodile"},
    {"question": "Which animal is known for its powerful punch?", "options": ["Kangaroo", "Gorilla", "Mantis Shrimp", "Eagle"], "answer": "Mantis Shrimp"},
    {"question": "Which mammal lays eggs?", "options": ["Platypus", "Kangaroo", "Echidna", "A & C"], "answer": "A & C"},
    {"question": "What is the fastest bird in the world?", "options": ["Eagle", "Peregrine Falcon", "Hawk", "Vulture"], "answer": "Peregrine Falcon"},
    {"question": "Which animal sleeps the most per day?", "options": ["Sloth", "Koala", "Cat", "Bear"], "answer": "Koala"},
    {"question": "Which is the heaviest snake in the world?", "options": ["Anaconda", "Python", "Cobra", "Viper"], "answer": "Anaconda"},
    {"question": "Which animal has the longest tongue in proportion to its body?", "options": ["Anteater", "Chameleon", "Giraffe", "Frog"], "answer": "Chameleon"},
    {"question": "Which animal is known for laughing?", "options": ["Hyena", "Dolphin", "Parrot", "Chimpanzee"], "answer": "Hyena"},
    {"question": "What is a group of owls called?", "options": ["Pack", "Herd", "Parliament", "Flock"], "answer": "Parliament"},
    {"question": "Which sea creature glows in the dark?", "options": ["Jellyfish", "Starfish", "Octopus", "Seahorse"], "answer": "Jellyfish"},
    {"question": "Which animal can regenerate lost limbs?", "options": ["Octopus", "Salamander", "Starfish", "All of the above"], "answer": "All of the above"},
    {"question": "What is the largest living species of lizard?", "options": ["Iguana", "Komodo Dragon", "Monitor Lizard", "Gecko"], "answer": "Komodo Dragon"},
    {"question": "Which is the smallest bird in the world?", "options": ["Hummingbird", "Sparrow", "Robin", "Finch"], "answer": "Hummingbird"},
    {"question": "Which animal has the strongest bite force?", "options": ["Lion", "Crocodile", "Hyena", "Shark"], "answer": "Crocodile"},
    {"question": "Which animal is known for its ability to squeeze into small spaces?", "options": ["Octopus", "Snake", "Mouse", "Mole"], "answer": "Octopus"},
    {"question": "Which fish can generate electricity?", "options": ["Eel", "Piranha", "Stingray", "Shark"], "answer": "Eel"},
    {"question": "Which animal produces the loudest sound?", "options": ["Howler Monkey", "Elephant", "Blue Whale", "Lion"], "answer": "Blue Whale"},
    {"question": "Which animal has fingerprints similar to humans?", "options": ["Chimpanzee", "Koala", "Bear", "Dog"], "answer": "Koala"},
    {"question": "Which sea creature can live for hundreds of years?", "options": ["Tortoise", "Jellyfish", "Whale", "Lobster"], "answer": "Jellyfish"},
    {"question": "Which animal has the most bones in its body?", "options": ["Shark", "Python", "Human", "Bat"], "answer": "Python"},
    {"question": "What is the largest species of shark?", "options": ["Great White Shark", "Hammerhead Shark", "Whale Shark", "Mako Shark"], "answer": "Whale Shark"},
    {"question": "Which animal has blue blood?", "options": ["Lobster", "Octopus", "Horseshoe Crab", "All of the above"], "answer": "All of the above"},
    {"question": "Which insect has the longest lifespan?", "options": ["Ant", "Termite Queen", "Dragonfly", "Cicada"], "answer": "Termite Queen"},
    {"question": "Which animal can sleep while standing up?", "options": ["Horse", "Cow", "Giraffe", "All of the above"], "answer": "All of the above"},
    {"question": "Which animal has the best sense of smell?", "options": ["Dog", "Elephant", "Shark", "Bear"], "answer": "Bear"},
    {"question": "Which animal can survive being frozen?", "options": ["Frog", "Fish", "Tardigrade", "All of the above"], "answer": "All of the above"},
    {"question": "What is a baby kangaroo called?", "options": ["Cub", "Kit", "Joey", "Foal"], "answer": "Joey"}
]
 
 
def checkGuess(question):
    global no_of_questions
    global score
    attempts = 0
    correct_answer = question["answer"].lower()
    
    print(f"\n{question['question']}")
    no_of_questions += 1
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option} ")
    while attempts < 3:
        try:
            user_choice = int(input("Enter your choice : "))
            if 1 <= user_choice <= len(question["options"]):
                guess = question["options"][user_choice - 1].lower()
            else:
                print("Invalid Choice! please try again")
                continue
        except ValueError:
            print("Enter a number ")
            continue
        
        if(guess == correct_answer):
            print("✔ Correct Answer ")        
            score += 1
            return 
        else:
            attempts += 1
            if attempts < 3:
                print("Wrong Answer please try again : ")
            else:
                print(f"3 Attempts completed the answer is {correct_answer}")

def playQuiz():
    global no_of_questions, score
    no_of_questions = 0
    score = 0
    random.shuffle(questions)
     
    for question in questions[:5]:
       no_of_questions += 1
       checkGuess(question)
   
    print(f"\n🎯 Game Over! Your final score is: {score}/5")
    again()



playQuiz()

