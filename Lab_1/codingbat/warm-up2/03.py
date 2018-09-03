def string_bits(str):
    string = ""
    for i in range(len(str)):
        if i % 2 is 0:
            string += str[i]
    return string