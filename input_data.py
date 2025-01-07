nama=input("Masukkan Nama Anda: ")
nim=int(input("Masukkan Nim Anda : "))
nilai=float(input("Masukkan Nilai Anda : "))
nilai_bool=bool(int(input("Apakah sudah benar : ")))

print("Nama : ", nama, " Tipe data adalah : ", type(nama))
print("Nim : ", nim, " Tipe data adalah : ", type(nim) )
print("Nilai: ", nilai, " Tipe data adalah : ", type(nilai))
print("Konfirmasi: ", nilai_bool, " Tipe data adalah : ", type(nilai_bool))


if nilai >=80:
    print("Selamat Anda lulus")
else:
    print("Mohon maaf anda belum lulus")
