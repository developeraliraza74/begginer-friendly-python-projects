# var1 = float(input("what is cgpa in float : "))
int_start_value = 1
int_stop_value = 5
int_step_value = 2
# print(range(int_start_value,int_stop_value,int_step_value)) range(starting, ending, difference)
# to get odd numbers 

# for i in range(1,50,2):
    #    print(i)

# Even Numbers 


# for i in range(50,2):
    #    print(i)
       
# print(var1)

'''Rhis'''

# print('''
# hello\r my name i\rs ws`s#W`sd`wswd3333edwe3w''')


# print("\xhh")


str = "            Ali is a good boy                        a"


# print(str[-4])

# print("My Nephew name is ", str)

# slice = str[0:5]
# print("Is Alnum ",str.isalnum())
# print("Is alpha",str.isalpha())
# print("Is ascii ",str.isascii())
# print("Is decimal",str.isdecimal())
# print("Is identifier",str.isidentifier())
# print("Is digit ",str.isdigit())
# print("Is  printable",str.isprintable())
# print("Is lower ", str.islower())
# print("Is Upper ", str.isupper())
# print("Is space ", str.isspace())
# str2 = str.lower()
# str3 = str.upper()
# str4 = str.capitalize()
# str5 = str.strip()
# print(str2)
# print(str3)
# print(str4)
# print(str5)









# lists in python 

list = [1,2, 1, 2, 3,3,3,4,4,5]


list.append(6) # add an element at the end 

list2 = [7,8,9]
indexElem = 6

list.extend(list2)  # add elements of new list to an existing list

# print(list.index(indexElem))


# print(f'the first index of {indexElem} is {list.index(indexElem)}')

list.insert(0,22) # insert an element (index, value)

# list.pop() # pop without argument remove the last index
# list.pop(3) # pop with argument means delete an element from a list on a specific index

# pop takes index while remove takes an element and remove the first element if it repeats 
# we can't use loop to remove all elements of a specific thing 
# list.remove(3) # remove must have a single argument (an element to delete)


# print(list, len(list))

# list2.remove()

# list.insert(0, "Ali Raza")
# list.insert(1, True)
# list.insert(2, list2)
# list2.insert(1, list2)
# list2[1].insert(0, list2)
length = len(list)
# for i in range(0,length):
#     print(list[i])

list.reverse() # to reverse all the elements of a list

list.sort() # just works with a list of same data type it can be of integars, strings or float

name_list = ["ali", "aali"]
name_list.sort()
# print(name_list)


float_list = [1.2,2.1,1.0]
float_list.sort()
# print(float_list)

bool_list = [True, False, False, False, True] # not supported for string and bool
bool_list.sort() # when sorting boolean list False comes first as F comes first and T comes later

# print(bool_list)

# print(list)
# print(f' 3 is {list.count(3)} times')

list.clear() # to delete all the elemenets of a list

# print(list)
# print(list)


# ==================      Tuples    ======================
'''Tuple is a list of comma separated values of any data type enclosed in square brackets 
The elements can be of different data types
Tuples are immutable
Most secured Collection is also known as tuple
'''

newTupple = (1,2,3,"Ali", True, 0.2, 0.4, 0.2, 0.2)


# count(elem) is used to count the repetition of an element
# print(newTupple.count(0.2))
# print(newTupple.index(2)) # to get the index of a specific value index(value)

# print(newTupple)







# ==================      Sets    ======================
'''Sets are unordered and well defined collection of elements
written in curly brackets
Unindexed: it means elements have not a proper index like tuple, list
Duplicate values not allowed
If duplicate values exists. It automatically removes the duplicates

'''

# Method 1 to create set
set1 = {1,2,3,1,3,3,3,3}

# Method 2 to create set 

set2 = set({1,2,3,3,5,6})
set1.add(9) # add an element in a set
set1.remove(9) # remove an element from a set
# set2.clear() # to remove all the elements of a set  :_) Takes no argument
# set1.discard(90) # discard even element is not available --> to avoid errors 


intersection_set = set.intersection(set1,set2) # returns the intersection 
union_set = set.union(set1, set2) # returns the union of sets

# isSubSet = print(set1.issubset(set2)) # to check if a set is a subset of another set --> subset.issubset(parentSet)

# print("Union of set 1 and set 2 is ", union_set)
# print("Intersection of set 1 and set 2 is ", intersection_set)

set2.pop() # takes no argument  --> remove 1st element from the set

set2.remove(6) # to remove a specific element from a set remove(value to be removed)



# print(set1)
# print(set2)



# ==================      Dictionaries    ======================

'''Unordered set of comma separated elements in the form of key value pairs
it allow duplicate values but not duplicate keys 
key and values must be strings

it is within curly braces {}
requirements within a dictionary?????
syntax : var = {name : "Ali", age: 20, fatherName : "Allah Yar",}
for blank dictionary var = {}
New or existing value of key can be changed 
If new the new key creates otherwise the value is updated

del dict[key] to delete a key from dictionary 
to add values in a dictionary   dict[key] = value

Dictionary Methods & Functions
Even a single space matters while making keys 
len(dict) for length of dictionary 
clear(dict) to make a dictionary empty 
dict.get(key) returns the value of a specific key 
dict.items()  returns a list containing a tuple for each key value pair 


'''


dict = {"name" : "Ali",
        "father" : "Allah Yar", }


dict["name"] = "Zaheer"
dict["age"] = 19

# del(dict["name"]) # delete a specific key 

# print(dict.get("name")) # returns the value of a specific key using get method
# print(dict.items()) # returns all the elements of a list in an ordered pairs (key, value), (key, value)
# print(dict.keys()) # It return all the keys of dictionary 
dict_keys = dict.keys()
dict_values = dict.values()
# dict.update("name") # takes two arguments Key and value


# print(dict_keys) # It return all the values of dictionary 
# print(dict_values)

# print(len(dict)) # print the length of a dictionary (Number of keys in a dictionary) 
# dict.clear() # to clear the complete dictionary 
# print(dict)



# ==================      Indentations     ======================

'''Indentations are very important
it applied on conditionals and loops to tell the interpreter what to execute depending upon the conditions'''

# comparison of three user given numbers in python

# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# c = int(input("Enter 3rd number : "))
# if(a>b and a>c):
#     print(a, " is greatest")
# elif(b>a and b>c):
#     print(b, " is the greatest")
# else:
#     print(c, " is the greatest")
    

#Loops in python

# for loop

# range function 
# for i in range(0,10):
#     print(i)



# i = ""
# while(i != "Ali"):
#     i = input("Enter Your Name: ")

# print("Welcome ", i)


# break statement


# check a number is prime or not

# count = 0
# num = int(input("Enter a number : "))
# for i in range(2,num, 1):
#     if(num % i ==0):
#       count += 1



# if(count == 0):
#     print(num, "Prime")
# else:
#     print(num, "not prime")


for i in [1,2,3,4,5,6]:
    if(i % 2 !=0):
        # break
        continue
    # print(i)





# ==================      Functions      ======================
'''block of code that is executed when it is called 
You can pass parameters to the functions and return values from a function
def function(): functino definition
function() fnction call
'''











# def add(a,b):
#     return "Hum koi ghulam hai Jo kho gy kr dengy "

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# print(add(a,b))



# ==================      File Handling      ======================

list = ["Hello I am ali ", "I love to code in python "]
file = open("ali.txt", "r+")
file.read()
file.writelines(list)
print(file.read())
# file.write("Hello")
if(file.close()):
    print("File is closed")

file.close()


# ==================      Object oriented programming      ======================

class Employee:
    name = ""
    empID = 0
    def __init__(self, name, empID):
        self.name = name
        self.empID = empID

    def printDetails(self):
        print("Your Name is ",self.name)
        print("Your Emp ID is ", self.empID)



class vehicle:
    model = ""
    color = ""
    brand = ""

    def __init__(self, model, color, brand):
        
        self.model = model
        self.color = color
        self.brand = brand 

    def printVehicleDetails(self):
            print("Car  brand is ", self.brand )
            print("Car  model is ", self.model )
            print("Car  brand is ", self.brand )
    @model.setter # setter
    def model(self, value):
        self.__model = value
    
    @property # getter
    def brand(self):
        return self.__brand

    @color.deleter # property-name.deter decorator
    def color(self, value):
        print('Deleting')
        del self.__color

class twoSeater(vehicle):
    country = ""
    owner = ""

    def __init__(self, model, color, brand, country, owner):
        self.country = country
        self.owner = owner
        self.model = model
        self.color = color
        self.brand = brand 

    def printDetails(self):
        print("Car  brand is ", self.brand )
        print("Car  owner is ", self.owner )
        print("Car  model is ", self.model )
        print("Car  brand is ", self.brand )
        print("Car  country is ", self.country )
       

# e1 = Employee("Ali", 4)
# e1.printDetails()

lc400 = vehicle("lc400", "Black", "Honda")
lemberghini = twoSeater("lamborgini", "red", "lam", "Pakistan", "Ali Raza")



isSubClass = issubclass(vehicle,twoSeater)
# print(issubclass)
# lemberghini.printDetails()
 
# lc400.printVehicleDetails()


itter_list = iter(["Ali", "Umar", "Shehzad"])
# used to create an iterator over iterable
# print(next(itter_list))
# print(next(itter_list))
# print(next(itter_list))



def my_gen():
    n = 1
    print("This is printed first")
    yield n
    n += 1
    print("This is printed second")
    yield n 
    n += 1
    print("This is printed at last")
    yield n



my_gen()















# queries :
# how can we remove duplicates from a list
# requirements within a dictionary?????
# how update in dictionary works
# syntax of update
# file handling 
# getter setter deleter 
# decorator and generators
# iterators 
# inheritance and its levels
