import time

my_time = int(input("Enter the time in seconds: "))

for x in range (0,my_time):
    print(x)
    time.sleep(1)

print("time's up!!")

# reverse
for x in range (my_time,0,-1):
    print(x)
    time.sleep(1)

print("time's up!!")

# seconds , minutes, hours
for x in range (my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds}")
    time.sleep(1)

print("time's up!!")