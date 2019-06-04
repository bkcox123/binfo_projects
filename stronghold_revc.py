# Set path
file = 'C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_revc.txt'
# Opens file and closes after execution
with open(file) as f:
    # converts string in file into a string that can be read
    dna_string = f.read()
    # Reverse string
    rev_dna = dna_string[::-1]
    # Create a translation table using the str function
    table = str.maketrans('TACG', 'ATGC')
    # print your solution
    print(rev_dna.translate(table))


# ALT CODE:
# I also created a dictionary that matched each nucleotide to its complementary base. From there,I mapped it out and
# replaced each character key with its corresponding element based on the order of the DNA string.
# nucl = {'G': 'C', 'A': 'T', 'C': 'G', 'T': 'A'}
# output = "".join([nucl.get(ch, ch) for ch in rev_dna])
