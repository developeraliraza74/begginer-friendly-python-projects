import random

# Data lists
characters = [
    "a sleep-deprived software engineer", 
    "a bug-hunting developer", 
    "a coffee-powered coder", 
    "an overworked intern", 
    "a frustrated QA tester", 
    "a Stack Overflow copy-paste expert"
]

settings = [
    "a production server at 2 AM", 
    "a hackathon with zero sleep", 
    "a startup running out of funding", 
    "a meeting that could have been an email", 
    "a client call explaining 'simple' changes", 
    "a project deadline that was due yesterday"
]

twists = [
    "accidentally deleted the production database", 
    "fixed one bug but introduced five more", 
    "wrote code that works… but doesn’t know why", 
    "spent 4 hours debugging, only to realize it was a typo", 
    "forgot a semicolon and crashed the whole system", 
    "said 'it works on my machine' and broke everything"
]

objects = [
    "a rubber duck debugger", 
    "a keyboard covered in coffee stains", 
    "a commit message that just says 'fix'", 
    "a bug so weird even Google has no answers", 
    "a to-do list that never gets completed", 
    "a documentation page that makes no sense"
]

moods = ["chaotic", "hilarious", "painfully relatable", "absurd", "nerdy", "a total disaster"]

def generate_story():
    """Generates a random programmer-themed story."""
    mood = random.choice(moods)
    character = random.choice(characters)
    setting = random.choice(settings)
    twist = random.choice(twists)
    obj = random.choice(objects)
    
    return f"In a {mood} turn of events, {character} was in {setting} when they {twist} using {obj}."

# Generate and print the story
print(generate_story())
