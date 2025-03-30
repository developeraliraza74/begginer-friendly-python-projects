import random
collection = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pass_length = int(input("Enter Password Length : "))

password = "".join(random.sample(collection, pass_length))

print(password)