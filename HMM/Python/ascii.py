def encoding(file):
    input = open(file)

    # абвгдежзийклмнопрстуфхцчшщґїьєюяі ’

    for line in input:
        row = list(line)

        for index in range(len(row)):
            row[index] = ord(row[index])

            if row[index] == 32: row[index] = 34 # " "
            elif row[index] == 8217: row[index] = 35 # "’"
            elif row[index] == 1169: row[index] = 27 # "ґ"
            elif row[index] == 1111: row[index] = 28 # "ї"
            elif row[index] == 1108: row[index] = 30 # "є"
            elif row[index] == 1110: row[index] = 33 # "і"
            else: row[index] = row[index] - 1071

    input.close()
    return row

def decoding(group):
    for index in range(len(group)):
        if group[index] == 34: group[index] = 32 # " "
        elif group[index] == 35: group[index] = 8217 # "’"
        elif group[index] == 27: group[index] = 1169 # "ґ"
        elif group[index] == 28: group[index] = 1111 # "ї"
        elif group[index] == 30: group[index] = 1108 # "є"
        elif group[index] == 33: group[index] = 1110 # "і"
        else: group[index] = group[index] + 1071

        group[index] = chr(group[index])

    return group