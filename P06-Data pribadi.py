from __future__ import print_function

print("pilih salah satu fungsionalitas sebagai berikut :")
print("1. cara menyimpan data: ")
print("2. cara menampilkan semua biodata: ")
print("3. Keluar program: ")

def save():
	h=input("masukan nama :")
	i=input("masukan tanggal lahir :")
	j=input("masukan asal daerah :")
	teks="Nama: {}\nUmur: {}\nAlamat: {}".format(h,i,j)
	file_bio=open("daftar.txt","w")
	file_bio.write(teks)
	file_bio.close()
	return file_bio

def menampilkan():
	file_bio=open("daftar.txt","r")
	j=file_bio.read()
	file_bio.close()
	return j

while(2):
	pilihan=int(input("masukan pilihan anda :"))
	if(pilihan==3):
		print("selamat tinggal")
		break;
	elif(pilihan==1):
		simpan=save()
		print (simpan)
	else:
		k=menampilkan()
		print(k)