# Set path
file = 'C:/Users/Bkcox/Documents/PycharmProjects/venv/Rosalind_data/rosalind_hamm.txt'
# Opens file and closes after execution
with open(file) as f:
    # List strings for iteration
    file_read = f.readlines()
    # Set genes up as separate strings
    ref_gene = file_read[0]
    comp_gene = file_read[1]
    # zip strings together for easy list comprehension function
    genes = zip(ref_gene, comp_gene)
    # Calculate the length of the list generated when selecting iterations where the first strings did not match the
    # second string
    different = len([c for c, d in genes if c != d])
    print(different)
