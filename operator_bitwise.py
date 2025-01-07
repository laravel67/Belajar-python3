a=9
b=5

# bitwise OR/AND/XOR

c=a|b
print("==========OR=========")
print("nilai : ", a, ' binary : ', format(a, '08b'))
print("nilai : ", b, ' binary : ', format(b, '08b'))
print("nilai : ", c, ' binary : ', format(c, '08b'))

c=a&b
print("==========AND=========")
print("nilai : ", a, ' binary : ', format(a, '08b'))
print("nilai : ", b, ' binary : ', format(b, '08b'))
print("nilai : ", c, ' binary : ', format(c, '08b'))


c=a^b
print("==========XOR=========")
print("nilai : ", a, ' binary : ', format(a, '08b'))
print("nilai : ", b, ' binary : ', format(b, '08b'))
print("nilai : ", c, ' binary : ', format(c, '08b'))


c=a^b
print("==========XOR=========")
print("nilai : ", a, ' binary : ', format(a, '08b'))
print("nilai : ", b, ' binary : ', format(b, '08b'))
print("nilai : ", c, ' binary : ', format(c, '08b'))

c = ~ b
print("==========XOR=========")
print('\nNilai b:',b,' dalam bntk binary:', format(b, '08b'))
print('---------------------------------------( ~ )')
print('Nilai c:',c,' dalam bntk binary:', format(c & 0xFF, '08b'))

# Sifthing
c=a>>2
print("==========>>=========")
print("nilai : ", c, ' binary : ', format(c, '08b'))

c=a<<1
print("==========<<=========")
print("nilai : ", c, ' binary : ', format(c, '08b'))

