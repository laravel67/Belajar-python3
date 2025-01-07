#Konversi Celcius ke satuan lain
print("\n PROGRAM KONVERSI TEMPERATUR SUHU \n")
#celcius
celcius=float(input('Masukkan suhu dalam celcius : '))

print("Suhu Celcius adalah ", celcius,"°C")
#reamur
reamur=(4/5)* celcius
print("Suhu reamur adalah ", reamur,"°R")
#Fahrenheit
fahrenheit=((9/5)* celcius)+32
print("Suhu Fahrenheit adalah ", fahrenheit,"°F")
#Kelvin
kelvin=celcius+273
print("Suhu Kelvin adalah ", kelvin,"K")

print("=====Fahrenheit ke kelvin=====")
fahrenheit = float(input("Masukan Suhu Fahrenheit : "))
celcius    = (5/9) * (fahrenheit - 32)
kelvin     = (celcius + 273)
print("Suhu dalam Kelvin : ", kelvin)

print("=====kelvin ke fahrenheit======")
kelvin     = float(input("Masukan Suhu Dalam kelvin : "))
celcius    = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit : ", fahrenheit)