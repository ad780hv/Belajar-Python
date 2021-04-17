class mahasiswa: #nama kelas

	jmlMhs=0	#pembagian data kelas

	def __init__ (self,nama,prodi):	#method/fungsi
		self.nama = nama           #instance
		self.prodi = prodi
		mahasiswa.jmlMhs += 1
	
	def tampilProfil(self):
		print("Nama : ", self.nama)
		print("Prodi : ", self.prodi)
		print()

mhs1 = mahasiswa('Adhi','Teknik Informatika')
mhs1.tampilProfil()
