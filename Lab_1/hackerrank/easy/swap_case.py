def swap_case(s):
    new = ""
    for x in s:
        if x.isupper(): new = new + x.lower()
        else: new = new + x.upper()
    return new