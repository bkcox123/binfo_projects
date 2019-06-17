# For later
import re
# First, auto-generate dictionary for codons based on text file
# Set path
codon_table = 'C:/Users/Bkcox/Documents/PycharmProjects/venv/codon_table.txt'
prot_d = {}
# Opens file and closes after execution
with open(codon_table) as codons:
    # read table line by line
    for line in codons:
        line = line.strip('\n')
        # split each line into list with four codon-protein matches
        codon_list = re.split(r'\s{2,}', line)
        # execute action on each codon-protein match
        for codon in codon_list:
            # Split codon-protein match into temporary list
            codon_match = codon.split()
            # Use temporary list to input codon as key and protein as element into a protein dictionary
            prot_d[codon_match[0]] = codon_match[1]
# Second, use read RNA seq in slides of three characters and compare to protein dictionary
# Set path
file = 'C:/Users/Bkcox/Documents/PycharmProjects/venv/Rosalind_data/rosalind_prot.txt'
Output = ''
# Opens file and closes after execution
with open(file) as f:
    # Read RNA seq from file
    RNA = f.readline()
    # Create list of codons from RNA seq
    RNA_split = re.findall('...', RNA)
    # Compare every set of three characters to protein dictionary keys, and generate a new string based on each key
    # element
    for c in RNA_split:
        key_val = prot_d.get(c)
        if key_val != 'Stop':
            Output = Output + key_val
    print(Output)


