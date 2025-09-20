number = int(input("Enter the size of the pattern:"))
x = 0
while(x < number):
    for i in range (1, number+1, 1):
        print("*", end="")
    print()
    x = x + 1