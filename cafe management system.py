menu = {
    "pizza" : 1500,
    "burger": 350,
    "showarma" : 200,
    "coffee" : 450,
    "gur wali chai" : 100, 
}


order_total = 0

print("Welcome to Restaurant ")
print("Item  :     Price")
print(f"Burger : {menu['burger']}\nShowarma : {menu['showarma']}\nPizza : {menu['pizza']}\nCoffee : {menu['coffee']}\nGur Wali Chai : {menu['gur wali chai']}")

answer = "yes"
while answer == 'yes':
    item = 'burger'
    item = input("Please enter what we can serve you Today : ")

    if item in menu:
        order_total += menu[item]
    else:
        print(f'{item} is not available yet :-)')

    answer =  input("Do you wnat to order anyother itme (yes/no): ")



print(f'YOUr Total bill  is {order_total}')
print("Thank you so much for visiting...")
