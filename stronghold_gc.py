# Set path
file = 'C:/Users/Bkcox/Documents/PycharmProjects/venv/Rosalind_data/rosalind_gc.txt'
# FASTA ID with current highest amount of GC content based on percentage
max_gc = 0
# GC content of current FASTA ID
gc_fasta = []
# Count of "G" and "C" in current line of genetic code
gc_cnt = []
# Count of all bases in current line of genetic code
base_cnt = []
# Stores gc percentages less than max
other_gc_perc = []
# Opens file and closes after execution
with open(file) as f:
    # List strings for iteration
    file_read = f.readlines()
    # pseudo code:
    # For each line, first ID whether it is FASTA ID or not; if it is, set a counter that goes until the next FASTA has
    # been found, add the FASTA to the output file and create a boolean variable that initiates a test for whether or
    # not the GC content has been improved
    # Iteratively examine strings line by line
    for line in file_read:
        # remove newline at end of string
        new_line = line.strip('\n')
        # Set for loop boundary for first line; Works because we know this is the first line is a gene ID
        if file_read.index(line) == 0:
            # Sets this ID as the original FASTA ID to check against gc_max
            fasta_ID = new_line.strip('>')
            continue
        if '>' in line:
            gc_fasta = sum(gc_fasta) * 100 / sum(base_cnt)
            # If this new percentage is higher than the current max percentage, then the max percentage will be replaced
            if gc_fasta > max_gc:
                max_gc = gc_fasta
                Output = fasta_ID
            gc_fasta = []
            base_cnt = []
            # Sets this ID as the new FASTA ID to check against gc_max; Remove ">" substring and assign set string as
            # potential answer
            fasta_ID = new_line.strip('>')
        # If line isn't FASTA, then begin listing gc amounts in string line by line
        else:
            # establish base count of line and add to a list
            base_cnt.append(int(len(new_line)))
            # establish GC count of line
            gc_cnt = sum(new_line.count(x) for x in ("G", "C"))
            # add to a list
            gc_fasta.append(gc_cnt)
        if line is file_read[-1]:
            gc_fasta = sum(gc_fasta) * 100 / sum(base_cnt)
            # Remove ">" substring and assign set string as potential answer
            # If this new percentage is higher than the current max percentage, then the max percentage will be replaced
            if gc_fasta > max_gc:
                max_gc = gc_fasta
                Output = fasta_ID
    print(Output)
    print(max_gc)