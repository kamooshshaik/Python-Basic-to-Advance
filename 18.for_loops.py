# for loops = execute a block of cpde a fixed number of times.
#             you can iterate over a range , string, sequence, etc...

for x in range (1,11):
    print(x)
print("ok")

# print in reverse format
for x in reversed(range (1,11)):
    print(x)
print("ok")

# print in step format
for x in range (1,11,2):
    print(x)
print("ok")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
print("ok")


# skip the intermediate number
for x in range (1,21):
    if x == 13: # enter the number what you wants to skip
        continue
    else:
        print(x)

# break the printing from that number
for x in range (1,21):
    if x == 13: # enter the number what you wants to skip
        break
    else:
        print(x)


