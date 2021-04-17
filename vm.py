from __future__ import print_function

class Orang:
	def __init__(self,nama,nik):
		self.nama= nama
		self.nik= nik
	
	def tampildata(self):
		print('nama',self.nama)
		print('nik',self.nik)

dt = Orang('','')
	
cc=input("nama :")
dd=input("nik :")
	
print()

class Mahasiswa(Orang):
	def __init__(self):
		Orang.__init__(self)
		print("mahasiswa")
		
ii=input("nim: ")
uu=input("belajar: ")
print()
		
