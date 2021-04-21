from __future__ import print_function

print("pilih salah satu fungsionalitas sebagai berikut :")
print("1. gaji manager :")
print("2. gaji karyawan :")
print("3. keluar dari program")

def manager():
	h=int(input("hari kerja manager :"))
	gm=100000
	gaji=h*gm
	return gaji
	
def karyawan():
	h=int(input("hari kerja karyawan :"))
	gk=50000
	upah=h*gk
	return upah
	
while(3):
	pilihan=int(input("masukan pilihan anda :"))
	if(pilihan==3):
		print("Terima kasih Telah Menggunakan Program Kami ")
		break;
	elif(pilihan==1):
		G=manager()
		print("gaji manager adalah %i"%(G))
	else:
		K=karyawan()
		print("gaji karyawan adalah %i"%(K))
	