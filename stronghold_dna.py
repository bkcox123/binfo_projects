# Set path
file = 'C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_dna.txt'
# Opens file and closes after execution
with open(file) as f:
    # converts string in file into a string that can be read
    dna_string = f.read()
    # Counts the number of times each substring appears in string and converts integer into a string
    C_count = str(dna_string.count('C')); G_count = str(dna_string.count('G'))
    A_count = str(dna_string.count('A')); T_count = str(dna_string.count('T'))
    # Combines strings into proper format
    output = A_count + ' ' + C_count + ' ' + G_count + ' ' + T_count
    # prints output
    print(output)

