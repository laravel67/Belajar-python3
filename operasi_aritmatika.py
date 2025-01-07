#penjumlahahan
a=10
b=3

jumlah= a+b
kurang= a-b
kali=a*b
bagi=a/b
sisa_bagi=a%b
pangkat=a**b
floor_devision=a//b

print("<============Penjumlahan==============>")
print(a, "+", b, '= ',jumlah)
print("<============Pengurangan==============>")
print(a, "-", b, '= ',kurang)
print("<============Perkalian==============>")
print(a, "x", b, '= ',kali)
print("<============Pembagian==============>")
print(a, ":", b, '= ',bagi)
print("<============Penjumlahan==================>")
print(a, "%", b, '= ',sisa_bagi)
print("<============Ekponen/Pangkat==============>")
print(a, "pangkat", b, '= ',pangkat)
print("<============Pembulatan Kebawah==============>")
print(a, "//", b, '= ',floor_devision)

x=3
y=2
z=4
#Prioritas Operasi/ operational precendece
print("<============Prioritas Operasi==============>")
hasil=x ** y * z + x / y - z % x // z
print(x,"**",y,"*",z,"+",x,"/",y,"-",z,"%",x,"//",z)
print("Hasil adalah : ", hasil)

