def front3(str):
    front_end = 3
    if len(str) < front_end:
      front_end = len(str) 
    return str[:front_end]*3