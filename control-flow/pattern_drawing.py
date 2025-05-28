size_pattern = int(input("Enter the size of the pattern:"))
for i in range(1, size_pattern + 1):
  # Outer loop controls the number of rows
  for j in range(1, size_pattern + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()