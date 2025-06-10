#Typecasting = the process of converting a variable from one data type to another data type
#              str(), int(), float(), bool()

name = "Kamoosh"
age = 25
cpi = 8.03
student = True

# Checking data type
print(type(name))
print(type(age))
print(type(cpi))
print(type(student))

# Converting one data type to another
# converting float to int.
cpi = int(cpi)
print(type(cpi))
print(cpi)

# converting int to str.
age = str(age)
print(type(age))

print(age)
# adding 1 at the end of 25 it become 251 because its cnverted to string.
age += "1"
print(age)

# converting str to bool.
name = bool(name)
print(name) # output will be true , if string is an empty " " output will be false.
