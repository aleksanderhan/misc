from time import clock
import random


def add1(a, b):
	return a + b

add2 = (lambda a, b: a + b)


n = 15000000
A = [random.random() for _ in range(n)]
B = [random.random() for _ in range(n)]
AUB = list(zip(A, B))


k = 50

dt_a1 = []
for i in range(k):
	t0 = clock()
	for a, b in AUB:
		add1(a, b)
	t1 = clock()
	dt_a1.append(t1-t0)


dt_a2 = []
for i in range(k):
	t2 = clock()
	for a, b in AUB:
		add2(a, b)
	t3 = clock()
	dt_a2.append(t3-t2)


print("normal:", sum(dt_a1)/k)
print("lambda:", sum(dt_a2)/k)
