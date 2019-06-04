# Set path
file = 'C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_rna.txt'
# Opens file and closes after execution
with open(file) as f:
    # converts string in file into a string that can be read
    dna_string = f.read()
    # replaces "T" with "U"
    rna_string = dna_string.replace('T', 'U')
    print(rna_string)