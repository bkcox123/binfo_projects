# Set path
file = 'C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_ini4.txt'
# Opens file and closes after execution
with open(file) as f:
    # Creates a list of strings and transform into integers
    data = f.readlines()
    intgs = list(map(int, data[0].split()))
    # Create null array
    numarray = []
    # Ensures that range function in for loop will be inclusive of the stop value
    intgs[1] += 1
    # For loop that runs through each number in the range between integer "a" and integer "b"
    for number in range(intgs[0], intgs[1]):
        # Conditional statement that checks if the remainder ("%" command) of the number divided by 2 is not equal to 0
        if (number % 2) != 0:
            # Adds number to array
            numarray.append(number)
    # Sums together all values in array
    output = sum(numarray)