def remove_extra(source_file, output_file):
    input = open(source_file)
    
    open(output_file, "w").close() # empty a file before appending (open and close again)
    output = open(output_file, "a")

    for line in input:

        line = line.lower()
        row = list(line)

        remove = [".", ",", ":", ";", "-", "!", "?", "\"", "–", "—", "…"]

        # replace invalid symbols with " "
        for index in range(len(row)):            
            if row[index] in remove: row[index] = " "

        # be careful with EOL
        while ("\n" in row): 
            if (row.index("\n") == 0): 
                row.remove("\n")
            else:
                row[row.index("\n")] = " "

        # delete all the extra " "
        index = 0
        while (index < len(row)-1):
            if row[0] == " ": row.pop(0)
            if row[index] == " " and row[index+1] == " ":
                row.pop(index)
            else:    
                index = index + 1

        # join cleaned line to an output file
        output.writelines(''.join(row))

    output.close()
    input.close()

def remove_spaces(source_file, output_file):
    input = open(source_file)

    open(output_file, "w").close() # empty a file before appending (open and close again)
    output = open(output_file, "a")

    for line in input:

        row = list(line)

        remove = [" ", "’", "'", "’"]
        removed_spaces = []

        # remove extra symbols
        index = 0
        while (index < len(row)):
            if row[index] in remove: 
                removed_spaces.append([index + len(removed_spaces), row[index]])
                row.pop(index)
            index = index + 1

        output.writelines(''.join(row))

    output.close()
    input.close()

    return removed_spaces

def insert_spaces(source_file, output_file, removed_spaces):
    input = open(source_file)

    open(output_file, "w").close()
    output = open(output_file, "a")

    for line in input:

        row = list(line)

        for i in range(len(removed_spaces)):
            row.insert(removed_spaces[i][0], removed_spaces[i][1])
    
        output.writelines(''.join(row))

    output.close()
    input.close()

def encrypt(source_file, output_file, alphabet, key):
    input = open(source_file)

    open(output_file, "w").close()
    output = open(output_file, "a")

    for line in input:

        row = list(line)

        index = 0
        while(index < len(row)):
            row[index] = alphabet[(alphabet.index(row[index]) + key) % len(alphabet)] 
            index += 1

        output.writelines(''.join(row))

    output.close()
    input.close()

def decrypt(source_file, output_file, alphabet, key):
    input = open(source_file)

    open(output_file, "w").close()
    output = open(output_file, "a") 

    for line in input:

        row = list(line)

        index = 0
        while(index < len(row)):
            row[index] = alphabet[(alphabet.index(row[index]) - key) % len(alphabet)] 
            index += 1

        output.writelines(''.join(row))

    output.close()
    input.close()

def push(source, output_file):
    open(output_file, "w").close()
    output = open(output_file, "a")

    output.writelines(''.join(source))

    output.close()

def count(source_file, alphabet, A):
    input = open(source_file)

    for line in input:

        row = list(line)

        index = 0
        while (index < len(row)-1):
            for i in alphabet:
                for j in alphabet:
                    if row[index] == i and row[index+1] == j:
                        A[alphabet.index(i)][alphabet.index(j)] += 1    
            index = index + 1

    input.close()

    return A