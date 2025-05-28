
size_pattern = int(input("Enter the size of the pattern: "))

row = 0
while row < size_pattern:
    for col in range(size_pattern):
        print("*", end="")
    print()  
    row += 1  
