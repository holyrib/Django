import math
a = int(input())
b = 0
for x in range(1, int(math.sqrt(a))):
	if a%x is 0: 
		b = b + 1
b = b*2
if a%math.sqrt(a) == 0: b = b + 1
print(b)
		
