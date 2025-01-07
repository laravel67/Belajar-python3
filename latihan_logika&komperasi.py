print("Masukkan Angka yang bernilai\n kurang dari 3\n atau lebih besar dari 10\n")
inputUser=float(input("Masukkan Angka: "))

isKurangDari=(inputUser<3)
isLebihDari=(inputUser>10)
isCorrect=isKurangDari or isLebihDari
print("Kurang Dari 3 =", isKurangDari)
print("Lebih Dari 10 =", isLebihDari)
print("Angka yang anda masukkan adalah ", isCorrect)


print("Masukkan Angka yang bernilai\n lebih dari 3\n dan kurang dari 10\n")
inputUser=float(input("Masukkan Angka: "))

isKurangDari=(inputUser>3)
isLebihDari=(inputUser<10)
isCorrect=isKurangDari and isLebihDari
print("Kurang Dari 3 =", isKurangDari)
print("Lebih Dari 10 =", isLebihDari)
print("Angka yang anda masukkan adalah ", isCorrect)

print("Masukkan Angka dengan Ketentuan Sebagai berikut:\n Lebih daru 0,\n Kurang dari 5,\n Lebih dari 8,\n Kurang dari 11\n")

inputUser=float(input("Masukkan Angka: "))
isLebihDari=(inputUser>0)
iskurangDari=(inputUser<5)
isLebihDari=(inputUser>8)
iskurangDari=(inputUser<11)

print("Lebih Dari 0 =", isLebihDari)
print("Kurang Dari 5 =", iskurangDari)
print("Lebih Dari 8 =", isLebihDari)
print("Kurang Dari 11 =", iskurangDari)
isCorrect=iskurangDari or isLebihDari
print("Angka yang anda masukkan adalah ", isCorrect)



