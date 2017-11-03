#///made by steel99xl
import time
global x
global s
global c
c = 1
x = c
print(c)
while x > 0:

	if x % 2 == 0: #even 
		x = x/2
	else: 
		x = (3*x+1)

	if x == 1:
		c += 1
		x = c
		print("       ")
		print(c)
	else:
		c = c
