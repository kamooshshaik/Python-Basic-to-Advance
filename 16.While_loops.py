# while loop = execute some code WHILE some condition remains true


name = input("Enter your name: ")
if name == "":
    print("You did not enter your name")
else:
    print (f"Hello {name}")

name = input("Enter your name: ")
while name == "":
    print("You did not entered your name")
    name = input("Enter your name: ")

print(f" Hello {name}")


age = int(input("Enter your age: "))
while age < 0:
    print("You age should not be negetive.")
    age = input("Enter your age: ")

print(f" Hello your age is  {age}")



food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"you like {food}.")
    food = input("Enter a food you like (q to quit): ")

print("Thank you bye")


num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 - 10: "))

print(f"yor Entered number is {num}.")