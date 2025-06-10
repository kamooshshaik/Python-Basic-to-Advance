# Input =  A function that prompts the user to enter data 
#          Returns the entered data as a string


name = input("What is your name: ")
age = int(input("How old are you: "))
age = age + 1

print(f"Hello {name}")
print(f"You are {age} years old.")


# Excercise - 1 (Calculation of Area of rectangle)
length = float(input("Enter length of rectangle (l) in meters : "))
width = float(input("Enter width of Rectangle (b) in meters : "))
area = length * width

print(f"Area of a Rectangle is {area}m².") # for square symbol (Alt + 0178) and (CTRL + /) for select and make comment.


# Excercise - 2 (Shopping cart program)
item = input("What item would you like to buy?: ")
price = float(input("What was the price?: "))
quantity = int(input("How many would you like to buy?: "))

total = price * quantity

print(f"You are brought a {quantity} x {item}/sPizza"  )
print(f"you are buying a {item}s at an total cost of Rs.{total}.")
