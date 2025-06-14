# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

Credit_number = "1234-5678-9012-3456"

print(Credit_number[1])   # indixing number it will print 0 1 2 3 4 5 6 . . . . .

print(Credit_number[0:4]) # what if we required 1st 4 digits to print
# or we can do like
print(Credit_number[:4]) # what if we required 1st 4 digits to print

print(Credit_number[5:9]) # what if we required middle  4 digits to print

print(Credit_number[5:]) # what if we required middle to end

print(Credit_number[-1]) # what if we required from back 1st digit or last digit

#Step

print(Credit_number[: : 2]) # Step approach it will print every number after 2 places

# Printing last four digits of our credit card number

last_four = Credit_number[-4:]
print(f"Your credit card number is XXXX-XXXX-XXXX-{last_four}.")

# Reversing the string or reversing the credit card number
Credit_number = Credit_number[: : -1]

print(Credit_number)