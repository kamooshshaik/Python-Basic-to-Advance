# String = its a series of character

name = input("Enter your name: ")
result = len(name)    # number of characters starts with 0 1 2 3 4 
print(result)

resu = name.find("k")              #1st occurance of the give charcters (" " space, or " Type anything between") 0 1 2 3 4 5 6 7 (indexies)
print(resu)

resu = name.rfind("k")        # last occurance of the give charcters (r means reverse) 0 1 2 3 4 5 6 7 (indexies) ex: kamoosh shaik as name
print(resu)          # it will return -ve number if they cant find the letter.


# 1st letter capitilize
name = name.capitalize()
print(name)

# Upper case string (all letters)
name = name.upper()
print(name)

# Lower case (all letters lower case)
name = name.lower()
print(name)

# is digit method will return the true or false if string contains only digits if the string is a boolean
result = name.isdigit()  # if the string will containg both digits and letters it will return false
print(result)            # it return true if the string is only contains digits.


# is alpha it will return a boolean if the straing contains alphabitical character  ex: typing name without space it will return true
result = name.isalpha()  
print(result)


# Count = counting number of required characters
phone_num = input("Enter your phone nuber: ")
result = phone_num.count("3")
print(result)   

# replace method = we can replace the one character with other
result = phone_num.replace("3","2")
print(result)

print(help(str)) # it will give how many availble string to code in help menu in terminal

# Validate user input excercise
# 1. username is not more then 12 characters.
# 2. username must not contain spaces.
# 3. username must not contain digits.

username = input("Enter your name: ")

if len(username) <= 12:
    if username.find(" ") == -1:
        if username.isalpha():
            print(f"Welcome {username}!.")
        else:
            print("username must not contain digits")
    else:
        print("username must not contain spaces")
else:
    print("username is not more then 12 characters")
    
    
# or we can write like below
if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
