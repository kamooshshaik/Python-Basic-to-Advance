# Python weight converter program

weight = float(input("Enter your Weight: "))
units = input("Units of weight kilograms or pounds (K OR L): ").upper()

if units == "K":
    result = weight * 2.025
    units = "lbs"
elif units == "L":
    result = weight / 2.025
    units = "kgs"
else:
    result = 0
    print(f"you have choosen wrong value {units}")
    
if result > 0:
    print(f"Your weight is {result}{units}")
else:
    print( )
