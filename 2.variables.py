# Variable = A container for a value ( string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings = a string is a series of characters they can include the numbers but we treat its as characters
first_name = "Bro"
food = "gulabjamun"
email = "kamooshbaba786@gmail.com"

print(first_name)
print(f"Hello {first_name}") # to add extra comment to our output
print(f"i like {food}")
print(f"my email is {email}")

# integer = a integer is a whole numbers, a integer should not be in quots "" because its a integer techenically.
#           another example is interger can be a quantity and amount of people.
age = 25
quantity = 8
no_of_students = 60

print(f"you are {age} years old!")
print(f"i am buying {quantity} apples!")
print (f"in my class has {no_of_students} students. ")


# Float = a float is a number but it contains a decimal portion.
price = 10.99
gpa = 8.03
distance = 10.87
print(f"the price of a chocklate is ${price}.")
print(f"my gpa is {gpa}.")
print(f"Distance from my home to college is {distance}km")


# boolean = a boolean is either True of False (1st letter should be capital).

is_student = True
graduation = False

print(f"are you a student? : {is_student}")
print(f"are you completed you graduation? : {graduation}")


if is_student:
    print("You are a student")
else:
    print("you are not a student")
    
    
if graduation:
    print("You are completed your graduation")
else:
    print("you are not completed your graduation")
