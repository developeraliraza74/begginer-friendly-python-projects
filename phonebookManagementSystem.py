phonebook = {}

def addContact():
    name = input("Enter person Name : ")
    if name in phonebook:
        print(f'\n\n{name} already exists Please try entering another name ')
    else:  
        number = int(input("Enter Contact Number : "))
        phonebook[name] = number


def searchContact():
    name = input("Enter person Name : ")
    if name in phonebook:
        print(f'\n \n{name} : {phonebook[name]}')
    else:
        print(f'{name} not in Your Contact List')
    
def deleteContact():
    name = input("Enter person Name : ")
    if name in phonebook:
        print(f'\n \n{name} : {phonebook[name]}')
        del(phonebook[name])
    else:
        print(f'\n{name} not in your Contact List')
def displayList():
    length = len(phonebook)
    for i in range(0,length):
        print(i)

    
def menu():
    print("1. New Contact \n2. Search by Name \n3. Delete a contact \n4. Contact List")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        addContact()
        menu()
    elif(choice == 2):
        searchContact()
        menu()
    elif(choice == 3):
        deleteContact()
        menu()
    elif(choice == 4):
        displayList()
        menu()


menu()