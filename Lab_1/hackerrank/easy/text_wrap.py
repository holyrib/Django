def wrap(string, max_width):
    new = ""
    for x in range(0, len(string)):
        if (x + 1)%max_width is not 0:
            new = new + string[x]
        elif x is 0: new = new + string[x]
        else:
             new = new + string[x]
             print(new)
             new = ""
    return ""