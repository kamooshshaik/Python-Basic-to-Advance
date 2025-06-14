# Python compound intrest calculator

# What Is Interest?
# Interest is the monetary charge for the privilege of borrowing money. Interest
# expense or revenue is often expressed as a dollar amount, while the interest
# rate used to calculate interest is typically expressed as an annual percentage
# rate (APR). Interest is the amount of money a lender or financial institution
# receives for lending out money. Interest can also refer to the amount of
# ownership a stockholder has in a company, usually expressed as a percentage.

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter your principal amount: "))
    if principal <= 0:
        print("Your principal amount should not be less then or equl to zero.")

while rate <= 0:
    rate = float(input("Enter your intrest rate in percentage %: "))
    if rate <= 0:
        print("Your intrest rate should not be less then or equl to zero.")

while time <= 0:
    time = int(input("Enter your time(years) in years: "))
    if time <= 0:
        print("Your time should not be less then or equl to zero.")

print(principal)
print(rate)
print(time)


# Calculate total
# P = Principal amount 
# R = rate of intrest
# T = number of time period elapsed

p = principal
r = rate
t = time

total = p * pow((1 + r/100),t)

print(f"Final amount for the your principal amount Rs.{principal} at the intrest rate of {rate} % for the {time} years is Rs.{total:.2f}.")


# method two

while True:
    principal = float(input("Enter the principle amount: "))
    if principal < 0:
        print("Principle can't be less than zero")
    else:
        break


while True:
    rate = float(input("Enter your intrest rate in percentage %: "))
    if rate < 0:
        print("Your intrest rate should not be less then or equl to zero.")
    else:
        break

while True:
    time = int(input("Enter your time(years) in years: "))
    if time < 0:
        print("Your time should not be less then or equl to zero.")
    else:
        break

print(principal)
print(rate)
print(time)


# Calculate total
# P = Principal amount 
# R = rate of intrest
# T = number of time period elapsed

p = principal
r = rate
t = time

total = p * pow((1 + r/100),t)

print(f"Final amount for the your principal amount Rs.{principal} at the intrest rate of {rate} % for the {time} years is Rs.{total:.2f}.")
