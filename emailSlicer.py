
print("Welcome to Email Slicer by developeraliraza74\n")
email = input("Enter your email Address : ").strip() # strip removes all the retailing spaces 

username = email[:email.index("@")]  #: before means all the characters before a specific index
domainName = email[email.index("@")+1:] # : after means all the remaining characters after a specific characters

print(f'Your Name : {username} \nDomain Name : {domainName}')