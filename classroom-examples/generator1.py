def countdown(n):
	while n > 0:
		yield n
		n-=1

j = countdown(5)
k = countdown(5000000000)

import sys
print(sys.getsizeof(j))
print(sys.getsizeof(k))