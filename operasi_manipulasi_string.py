# 1. Menyambung String

# nama_pertama=str(input("\nNama pertama: ")).strip()
# nama_tengah=str(input("\nNama tengah: ")).strip()
# nama_ahir=str(input("\nNama ahir: ")).strip()
# # Menggabung nama
# nama_lengkap=nama_pertama+' '+nama_tengah+' '+nama_ahir
# print("\nNama Lengkap: ",nama_lengkap)

# # Hitung Panjang
# panjang=len(nama_lengkap)
# print("\nPanjang Nama ", nama_lengkap, " Adalah :", panjang)

# # Cek apakah ada ada componen char atau string pada string

# print("\n====Cari Krakter atau huruf Pada Nama ",nama_lengkap, "====")
# huruf = str(input("\nMasukkan huruf: "))  # Huruf yang dicari
# get_string = huruf.lower() in nama_lengkap.lower()
# total = nama_lengkap.lower().count(huruf.lower())
# quest = f"Apakah ada huruf '{huruf}' pada nama '{nama_lengkap}'?"
# if get_string:
#     print(quest, "\nAda")
#     print(f"Jumlah huruf '{huruf}': {total}")
# else:
#     print(quest, "\nTidak Ada")


# # # Mengulang String
# print(20*"Mantap ketua\n ")

# # Indexis
# inputIndex=int(input("Ambil Index Ke: "))
# print("Index ke-",inputIndex, " adalah ", nama_lengkap[inputIndex])

# indexFirst=int(input("Dari Index ke-:"))
# indexLast=int(input("Sampai Index ke-: "))
# print("Huruf dari", nama_lengkap, "\nDari Index ke-",indexFirst,"\nsampai Index ke-:",indexLast,"\nAdalah : ",nama_lengkap[indexFirst:indexLast])
# totalList=int(input("Masukkan Rentang Index: "))
# print("Huruf dari", nama_lengkap, "\nRentang Index",totalList, " Adalah : ",nama_lengkap[indexFirst:indexLast:totalList])

# # Paling Kecil
# print("Paling Kecil:" +min(nama_lengkap))
# # Paling Besar
# print("Paling Besar:" +max(nama_lengkap))

# asc
ascii_code=ord(" ")
print("ASCII code dari spasi adalah: "+str(ascii_code))
data=int(input("Masukkan Angka:"))
print("Char dari ", data, " Adalah: ", chr(data))



