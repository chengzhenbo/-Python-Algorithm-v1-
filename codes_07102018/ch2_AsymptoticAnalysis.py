#coding=utf-8
from pylab import *
import numpy as np
def test1():
	n = arange(0.0, 10.0, .01)
	t1 = n*n 
	t2 = 1.1 * n ** 2 + (n ** 1.5 + 10) * sin(n * 10 + 1.5) + 30

	fig, ax = plt.subplots()
	ax.plot(n, t1, '--',label='T1(n)')
	ax.plot(n, t2, label='T2(n)')

	legend = ax.legend(loc='upper center', shadow=True)

	xlabel('n')
	ylabel('T(n)')
	grid(True)
	savefig("t1_t2_10.pdf")
	show()
def test2():
	n = arange(0.0, 10000.0, 0.1)
	t1 = n*n 
	t2 = 1.1 * n ** 2 + (n ** 1.5 + 10) * sin(n * 10 + 1.5) + 30

	fig, ax = plt.subplots()
	ax.plot(n, t1, '--',label='T1(n)')
	ax.plot(n, t2, label='T2(n)')

	legend = ax.legend(loc='upper center', shadow=True)

	xlabel('n')
	ylabel('T(n)')
	grid(True)
	savefig("t1_t2_10000.pdf")
	show()

def test3():
	n = arange(0.0, 5.0, .001)
	t1 = np.log2(n) 
	t2 = n
	t3 = 2**n

	print(t3)

	fig, ax = plt.subplots()
	ax.plot(n, t1, label='log(n)')
	ax.plot(n, t2, label='n')
	ax.plot(n, t3, label='2^n')


	legend = ax.legend(loc='upper center', shadow=True)

	xlabel('n')
	ylabel('T(n)')
	grid(True)
	savefig("t1_t2_t3_1000.pdf")
	show()

if __name__ == "__main__": 
	test1()
