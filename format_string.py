name="Murtaki"
format_string=f"Hello {name}"
print(format_string)

# Boolean
boolean=True
format_string=f"boolean={boolean}"
print(format_string)

#angka
angka=2000.5
format_string=f"Angka={angka}"
print(format_string)

#Bilangan Bulat
angka=15
format_string=f"Angka Bulat={angka:d}"
print(format_string)

#Bilangan Bulat Dengan Ordo Ribuan
bilangan=200000
format_string=f"Jutaan ={bilangan}"
print(format_string)

#Bilangan Desimal
desimal=2007.8923
format_string=f"Desima={desimal:.1f}"
print(format_string)

#Leading Zero
leading=2007.8923
format_string=f"Leading Zero={leading:010.3f}"
print(format_string)

# Angka Plus dan Minus
plus=10
minus=-10
formar_plus=f"Format Angka Plus={plus:+d}"
formar_minus=f"Format Angka Minus={minus:+d}"
print(formar_plus)
print(formar_minus)

# Format Persentase
percentage=0.035
format_percentage=f"Format Persentase={percentage:.2%}"
print(format_percentage)

# Melakukan Operasi didalam aritmatika
harga=1000
jumlah=5
formar_string=f"Total harga:=Rp.{harga*jumlah:,}"
print(formar_string)

# Format Angka Binary,Octal,Hex
angka=255
format_binary=f"Format Angka Binari={bin(angka)}"
format_octa=f"Format Angka Oktal={oct(angka)}"
format_hex=f"Format Angka Hex={hex(angka)}"
print(format_binary)
print(format_octa)
print(format_hex)




