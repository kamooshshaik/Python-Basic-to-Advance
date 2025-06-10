#Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                         Print or assaign one of two values based on a condition 
#                         X if condition else Y

#Simple Conditional Expression
num = 10
a = 5
b = 7

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)

max_num = a if a > b else b
min_num = a if a < b else b

print(max_num)
print(min_num)



age = int(input("Enter your age: "))
status = "Adult" if age > 18 else "Child"
print(status)


temp = float(input("Enter current temperature: "))
temp_sta = "Hot Outside" if temp > 30 else "temperature is Ok"
print(temp_sta)

user_role = "Admin"

access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_level)