# Basic - Print all integers from 0 to 150.
for x in range(0,151):
    print(x)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001):
    if (x % 5 ==0):
        print(x)

# Counting, the Dojo Way
for x in range(1,101):
    if(x % 5 == 0 and x % 10 == 0):
        print("Coding Dojo")
    elif(x % 5 == 0):
        print("Coding")
    else:
        print(x)

# Add odd integers from 0 to 500,00 and print the final sum
sum = 0

for x in range(1,500001):
    if(x % 2 != 0):
        # print(f"{x} is odd")
        sum = sum + x

print(sum)
