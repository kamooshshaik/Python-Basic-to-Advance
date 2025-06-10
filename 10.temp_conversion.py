# Python Temperature converter program

units = input("Enter temperarture units in celsius of fahrengeit (C/F): ").upper()
temp = float(input("Enter temperature: "))

if units == "C":
    result = ((temp * 9)/5) + 32
    units = "°F"   # (alt + 0176) for °.
    print(f"The temperature is {result}{units}")
elif units == "F":
    result = (temp - 32 ) * (5/9)
    units = "°C"   # (alt + 0176) for °.
    print(f"The temperature is {result}{units}")
else:
    print(f"The selection {units} is In valid")