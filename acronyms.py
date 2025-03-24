user_input = input("Enter a phrase : ")
text = user_input.split()

a = " "

for i in text:
    a += str(i[0]).upper()

print(f'Acronym of {user_input} is {a}')