# Complete the solve function below.
def solve(s):
    new = ""
    l = s.split()
    for x in l:
        new = new + str(x[0].capitalize()) + x[1:]
        new = new + " "
    return(new)

print(solve("hello  world  lol"))