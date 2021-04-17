from __future__ import print_function

a=int(input("Masukan alas : "))
t=int(input("Masukan tinggi : "))

def luas_segitiga(a,t):
	luas=(a*t)/2
	return luas
	
def kell_segitiga(a,t):
	s=int(input("Masukan sisi miring : "))
	kell=a+t+s
	return kell
	
L=luas_segitiga(a,t)
K=kell_segitiga(a,t)

print("Luas Segitiga adalah %f"%(L))
print("keliling Segitiga adalah %f"%(K))






