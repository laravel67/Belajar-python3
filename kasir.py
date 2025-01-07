print("\n<=========SELAMAT DATANG DI WARUNG KAMI==========>")
pembeli=str(input("\nMasukkan nama pembeli :"))
print("Nama Pembeli: ", pembeli)

def fungsiMakanan():
    
    global totalmakan
    global porsi
    global makan
    global minum
    
    print("\n-----MENU MAKANAN------\n")
    print("1. Bakso------------------Rp.10.000,00")
    print("2. Mie Ayam---------------Rp.15.000,00")
    print("3. Mie Goreng------------ Rp.8.000,00")
    print("4. Nasi Goreng------------Rp.12.000,00")
    print("5. Gorengan---------------Rp.1.000,00")
    nomor=int(input("\nPilih Makanan: "))
    porsi=int(input("Jumlah Porsi : "))
    
    if nomor==1:
        totalmakan=porsi*10000
        print("{} Bakso = Rp. {:,}".format(porsi, int(totalmakan)))
        makan=("Bakso")
    elif nomor==2:
        totalmakan=porsi*15000
        print("{} Mie Ayam = Rp. {:,}".format(porsi, int(totalmakan)))
        makan=("Mie Ayam")
    elif nomor==3:
        totalmakan=porsi*8000
        print("{} Mie Goreng = Rp. {:,}".format(porsi, int(totalmakan)))
        makan=("Mie Goreng")
    elif nomor==4:
        totalmakan=porsi*12000
        print("{} Nasi Goreng = Rp. {:,}".format(porsi, int(totalmakan)))
        makan=("Nasi Goreng")
    elif nomor==4:
        totalmakan=porsi*1000
        print("{} Gorengan = Rp. {:,}".format(porsi, int(totalmakan)))
        makan=("Gorengan")
    else:
        print('Menu Tidak Tersedia!.')
        fungsiMakanan()
        
        
def fungsiMinuman():
    
    global totalminum
    global minuman
    global gelas
    
    print("\n-----MENU MINUMAN------\n")
    print("1. Es Teh-----------------Rp.5.000,00")
    print("2. Jus Jeruk--------------Rp.10.000,00")
    print("3. Kopi Susu--------------Rp.5.000,00")
    print("4. Lemon Tea--------------Rp.7.000,00")
    print("5. Pop Ice---------------Rp.5.000,00")
    
    nomor=int(input("\nPilih Minuman: "))
    gelas=int(input("Berapa Gelas : "))
    
    if nomor==1:
        totalminum=gelas*5000
        print("{} Es Teh = Rp. {:,}".format(gelas, int(totalminum)))
        minuman=("Es Teh")
    elif nomor==2:
        totalminum=gelas*10000
        print("{} Jus Jeruk = Rp. {:,}".format(gelas, int(totalminum)))
        minuman=("Jus Jeruk")
    elif nomor==3:
        totalminum=gelas*5000
        print("{} Kopi Susu = Rp. {:,}".format(gelas, int(totalminum)))
        minuman=("Kopi Susu")
    elif nomor==4:
        totalminum=gelas*7000
        print("{} Lemon Tea = Rp. {:,}".format(gelas, int(totalminum)))
        minuman=("Lemon Tea")
    elif nomor==4:
        totalminum=gelas*5000
        print("{} Pop Ice = Rp. {:,}".format(gelas, int(totalminum)))
        minuman=("Pop Ice")
    else:
        print('Menu Tidak Tersedia!.')
        fungsiMinuman()
        
fungsiMakanan()
fungsiMinuman()

total=totalmakan+totalminum

print("\nTotal Pembayaran: Rp. {:,}".format(int(total)))

uang=int(input("Uang Pembayaran: "))
kembalian=int(uang-total)
print("\nKembalin: Rp. {:,}".format(int(kembalian)))

print("\n============================")
print("\n============STRUK BELANJA===============")
print("\n========================================")
print("Nama Pembeli: ", pembeli)
print("\nMAKANAN: ")
print("\n>> ", makan)
print("\n>> ", porsi, " Porsi")
print("\n>> Rp. {:,}".format(totalmakan))

print("\nMINUMAN: ")
print("\n>> ", minuman)
print("\n>> ", gelas, " Gelas")
print("\n>> Rp. {:,}".format(totalminum))


print("\n--------------PEMBAYARAN----------------")
print("\nUang: Rp. {:,}".format(uang) )
print("\nKembalian: Rp. {:,}".format(kembalian) )
print("\nTotal Pembayaran: Rp. {:,}".format(total) )
print("\n====TERIMAKASIH TELAH BELANJA DI WARUNG KAMI==========\n")





        