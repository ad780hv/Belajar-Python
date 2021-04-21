from __future__ import print_function

try:
	x = int(input("Masukan angka: "))
	print("pemisah 50 dengan",x,"akan memberi kamu:", 50/x)
except valueError:
	print("input bukan bilangan bulat,silakan coba lagi....")
	