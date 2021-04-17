from __future__ import print_function

print("=============================")
print("Selamat Datang Di Program Biodata")
print("==============================")
print("menu :")
print("1. Menyimpan biodata")
print("2. Tampilkan semua biodata")
print("3. Keluar Program")

def save():
	nama=input("Nama: ")
	lahir=input("Tanggal lahir: ")
	alamat=input("Asal daerah: ")
	teks="\nNama: ()\nTanggal lahir: ()\nAsal daerah: ()\n-----".format(nama,lahir,alamat)
	file_bio=open("data.txt","a")
	file_bio.write(teks)
	file_bio.close()
	return file_bio

def tampil():
	file_bio=open("data.txt","r")
	k=file_bio.read()
	file_bio.close()
	return k

while(2):
	pilihan=int(input("masukan pilihan :"))
	if(pilihan==3):
		print("..............................")
		print("Terimakasih telah bergabung")
		print("	Selamat tinggal	")
		print("..............................")
		break;
	elif(pilihan==1):
		j=save()
		print(j)
		lagi=input("Ingin menjalankan menu lagi: ")
		if(lagi=="no"):
			print("terima kasih telah bergabung dengan program")
			break;
		else:
			pilihan
	else:
		l=tampil()
		print(l)
		lagi=input("ingin menjalankan menu lagi: ")
		if(lagi=="no"):
			print("terima kasih telah bergabung dengan program")
			break;
		else:
			pilihan

























