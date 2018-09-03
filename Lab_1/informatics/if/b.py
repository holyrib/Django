a = int(input())
if  a%4 is 0 and (a%100 is not 0 or a%400 is 0):
	print("YES")
else:
	print("NO")