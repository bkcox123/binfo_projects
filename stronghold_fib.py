# Set path
file = 'C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_rabbits.txt'
# Opens file and closes after execution
with open(file) as f:
    # converts string in file into appropriate variables
    n, k = [int(x) for x in next(f).split()]
    # while loop that calcs new Fib value from previous two values, then shifts the old Fib values with new ones;
    # Dynamic programming is another method
    count = 2
    f_1 = 1
    f_2 = 1
    while count <= n:
        # Bunny making time
        F_n = f_1 + k * f_2
        # replace old Fib values with new ones
        f_2 = f_1
        f_1 = F_n
        # increase step by one
        count += 1
        # print out solution for Rosalind
        if count == n:
            print(F_n)
