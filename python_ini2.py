# set file path
file = 'C:/Users/Bkcox/Desktop/Rosalind/rosalind_problems/rosalind_py_p2/rosalind_ini2.txt'
# open file to read text file using "with" function so that process opens and closes efficiently
# assigns text file data as var "f"
with open(file) as f:
    # assigns strings as separate objects with next(f).split() by using the whitespace to differentiate
    # Converts string objects into integer objects and assigns them to the specified variables "x" and "y"
    y, z = [int(x) for x in next(f).split()]
    # combines integer variables into new integer variables for final answer
    ans = y**2 + z**2
    # prints answer
    print(ans)

# ALT CODE for further application
# if txt file contained more than one dimension
# create null matrix
# array = []
# begin with for loop
# for line of f:
# fill variable "array" line by line using append function
