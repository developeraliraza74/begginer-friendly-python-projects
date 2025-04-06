def celsius_to_farenheight(celsius):
    f = float(celsius)
    c = (f-32) * 5/9
    return c

def farenheight_to_celsius(farenheight):
    c = float(farenheight)
    f = (c * 9/5) + 32
    return f



print("Celsius to Farenheight Converter")
print("1. Celsius to Farenheight")
print("2. Farenheight to Celsius")
choice = int(input("Enter your choice: "))

if choice == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    farenheight = celsius_to_farenheight(celsius)
    print(f"{celsius}C is {farenheight}F")
elif choice == 2:
    farenheight = float(input("Enter the temperature in Farenheight: "))
    celsius = farenheight_to_celsius(farenheight)
    print(f"{farenheight}F is {celsius}C")
else:
    print("Invalid choice")

