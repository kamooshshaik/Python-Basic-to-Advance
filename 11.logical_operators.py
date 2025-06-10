# Logical operators = evaluate multiple conditions (or , and , not)
#                or = at least one condition must be true
#               and = both conditions must be true
#               not = inverts the condition (not false, not true)

temp = float(input("Enter temperature in celsius:" ))
its_raining =  False

if temp > 35 or temp < 0 or its_raining:
    print(f"The outdoor event is canceled")
else:
    print("the out door event is scheduled")
    
    
temp = float(input("Enter temperature in celsius:" ))
its_sunny =  False

if temp >= 28 and its_sunny:
    print(f"Its hot outside temp is {temp}°C😡") # for an emojie (Windos + .)
    print(f"Its Sunny 🌞")
elif temp <= 0 and its_sunny:
    print(f"Its Cold outside temp is {temp}°C🥶") # for an emojie (Windos + .)
    print(f"Its Sunny 🌞") 
elif temp < 28 and temp > 0 and its_sunny:
    print(f"Its warm outside temp is {temp}°C 😎") # for an emojie (Windos + .)
    print(f"Its Sunny 🌞") 
elif temp >= 28 and not its_sunny:
    print(f"Its hot outside temp is {temp}°C😡") # for an emojie (Windos + .)
    print(f"Its Cloudy 😶‍🌫️") 
elif temp <= 0 and not its_sunny:
    print(f"Its Cold outside temp is {temp}°C🥶") # for an emojie (Windos + .)
    print(f"Its Cloudy 😶‍🌫️") 
elif temp < 28 and temp > 0 and not its_sunny:
    print(f"Its warm outside temp is {temp}°C 😎") # for an emojie (Windos + .)
    print(f"Its Cloudy 😶‍🌫️") 
else:
    print("the out door event is Canclled 😁")
    print(f"Its Cold ☃️")