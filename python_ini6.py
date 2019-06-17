# Set path
file = 'C:/Users/Bkcox/Desktop/Rosalind/Rosalind/rosalind_ini6.txt'
# Create empty dictionary
d = {}
# Opens file and closes after execution
with open(file) as f:
    # converts string in file into a string that can be read
    string = f.read()
    # for loop that reads every word split by whitespace;
    # split() default automatically separates words by whitespace
    for word in string.split():
        # conditional statement that assigns an initial value of 0 to a word
        # not in keys
        if word not in d.keys():
            d[word] = 0
        # Adds to the value assigned to a particular key; if the value has not been
        # entered before, the previous line of code will have started the value at 0, which
        # means the word will always start with a value of one and will go up with every
        # future hit.
        d[word] += 1
    # prints each key with its corresponding value for easier viewing
    for key, value in d.items():
        print(key)
        print(value)