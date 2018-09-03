a = int(input())
l = []
s = ""
s = s + " " + str(input())
l = s.split()
#print(l)
for x in range(0, len(l)):
	if x%2 == 0: print(l[x])
