# Set path
file = 'C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_ini5.txt'
# Opens file for reading and opens output file for writing
with open(file) as f:
    with open('C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_ans5.txt', 'w') as g:
        # Creates a list of strings
        line = f.readline()
        # Sets count as a boolean operator that is toggled on and off. False means off.
        count = False
        for line in f:
            # Turns on count
            count = not count
            # Conditional statement checking if iteration count is odd
            if count % 2 != 0:
                # Write line into new next file
                g.write(line)