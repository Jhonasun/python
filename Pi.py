# coding:utf-8
from math import sqrt
import random  

onhit = 2**20
hit1 = 0

for i in range(1,onhit):
	x,y = random.random(), random.random()
	if sqrt(x**2 + y**2) <= 1:
		hit1 += 1
pi = 4*(hit1/onhit)
print ("Pi = %.10f"%pi)
