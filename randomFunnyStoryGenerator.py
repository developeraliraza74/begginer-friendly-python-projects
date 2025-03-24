import random

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
    "accidentally deletes the production database", 
    "fixes one bug but introduces five more", 
    "writes code that works… but doesn’t know why", 
    "spends 4 hours debugging, only to realize it's a typo", 
    "forgets a semicolon and crashes the whole system", 
    "says 'it works on my machine' and breaks everything"
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

# generating random story 

print(f'In a mood {random.choice(moods)} turn of events, {random.choice(characters)} was in {random.choice(settings)} when they {random.choice(twists)} using {random.choice(objects)}') 

