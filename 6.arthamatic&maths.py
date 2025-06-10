# Arthamatic operators

#Addition operator
friends = 10
friends = friends + 1
print(friends)

friends = 10
friends += 1  # Augumetated assignment operator
print(friends)


#substraction operator
friends = 10
friends = friends - 2 
print(friends)

friends = 10
friends -= 2 # Augumetated assignment operator
print(friends)

# Multiplication
friends = 10
friends = friends * 3
print(friends)

friends = 10
friends *= 3
print(friends)

# division operator
friends = 10
friends = friends / 4
print(friends)

friends = 10
friends /= 4
print(friends)

# Exponent operator
friends = 10
friends = friends ** 2
print(friends)

friends = 10
friends **= 2
print(friends)

# Remainder 
friends = 12
friends = friends % 3
print(friends)

friends = 10
friends %= 3
print(friends)

# Built in math

x = 3.14
y = -4
z = 5

#Round off
round_off = round(x)
print(round_off)

# Absolute value of the number
absolute = abs(y)
print(absolute)

# power function
power = pow(z, 2) # It means Z^2
print(power)

# Max function
maximum = max(x, y, z)
print(maximum)

# Min function
minimum = min(x,y,z)
print(minimum)

# Importing math
import math

print(math.pi)
print(math.e)
print(math.sqrt(16))


# Celing function -> always the round of the floating value to up
x = 8.11
celing = math.ceil(x)
print(celing)

# Floor function -> always the round of the floating value to up
x = 8.11
floor = math.floor(x)
print(floor)


# Excercise - 1 -> to calculate the circurference of the circle
radius = float(input("Enter the radius of the circle in meters: "))
cicurf = 2 * radius * math.pi

print(f"The circumference of the circle is {cicurf} m.")

# Excercise - 2 -> to calculate the area of the circle
area = math.pi * pow(radius , 2)
print(f"The area of the circle is {area} m².")

# Excercise - 3 -> to calculate the hypotenuse of the right angle triangle
side1 = float(input("Enter base of the triangle in meters: "))
side2 = float(input("Enter height of the triangle in meters: "))
hypotenuse = math.sqrt(pow(side1,2) + pow(side2,2))
print(f"The hypotenuse of the triangle is {hypotenuse} m.")