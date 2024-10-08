for num in range(1, 21):  
    if i % 2 == 0:  
        print(f"{num} is even")
    else:  
        print(f"{num} is odd")

# Ask the user for the lower and upper limits of the range
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

for i in range(lower_limit, upper_limit + 1): 
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


