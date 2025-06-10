# input() = A function that prompts the user to enter the data 
#           Returns  the entered data as a string

name = input("Enter Your name : ")
age = int(input("Enter your age: "))

print(f"Hello {name}")
age = age + 1   # This is only possible if the age is in integer form.
print(f"Your {age} years old")


# Excercise - 1 -> Rectangular area calculation
length = float(input("Enter a length of a rectangular:" ))
width = float(input("Enter width of a rectangular: "))

area = length * width

print(f"Area of a rectangular is {area}m².") # for square symbol turn number lock + alt +0178.

# Excercise - 2 -> Shopping cart Programm

item = input("what would you like to buy: ")
price = float(input("Enter the price of the product: "))
quantity = int(input("Enter no of products: "))

print(f"You have brought total of {item} x {quantity}/s")
print(f"You need to pay the amount of Rs.{price * quantity}/-.")


