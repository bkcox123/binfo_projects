# Set path
file = 'C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_ini3.txt'
# Opens file and closes after execution
with open(file) as f:
    # Creates a list with two sets of strings
    data = f.readlines()
    # Splits numbers in string into separate integers
    its = list(map(int, data[1].split()))
    # Create substrings based on integers from second line; Feels clunky, would rather use .join but not sure how
    output = data[0][its[0]:its[1]+1] + ' ' + data[0][its[2]:its[3]+1]