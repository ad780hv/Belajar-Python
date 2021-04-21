from __future__ import print_function

keep_asking = True

while keep_asking:
	try:
		x = int(input("100: "))
		print(50/x)
	except ValueError:
		print("inputan bukan integer. Tolong coba lagi...")
	