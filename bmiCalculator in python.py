height = float(input("Enter your height in cm : "))
weight = float(input("Enter your weight in kg : "))


feet = int(height)  # Extract feet (integer part)
inches = (height - feet) * 10  # Extract inches (decimal part * 10)

total_inches = (feet * 12) + inches  # Convert to total inches
height_m = total_inches * 0.0254  # Convert inches to meters
    

bmi = (weight * 703) / ((height_m ** 2))

print("Your BMI is : ", bmi)




