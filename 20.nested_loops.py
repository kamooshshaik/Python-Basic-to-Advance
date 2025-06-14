# nested loop = a loop within anothe loop (outer, inner)
#               outer loop:
#                   inner loop:

for x in range (1,10):
    print(x,end=" ")  # print horizontally


for x in range(3):  # for multliplication in no of times
    for y in range(1,10):  # inner loop
        print(y, end=" ")
    print()        # printing in new line


# printing rectangle using loops
row = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))
symbol = input("Enter a symbol to make rectangle: ")

for i in range(row):
    for j in range(columns):
        print(symbol, end="")
    print()