# type data =angka/integer
data_angka=1
print("Type data dari ", data_angka, ", adalah ", type(data_angka))
#type data float
data_float=10.5
print("Type data dari ", data_float, ", adalah ", type(data_float))
#type data string
data_string="Murtaki"
print("Type data dari ", data_string, ", adalah ", type(data_string))
#type data boolean
data_boolean_true=True
data_boolean_false=False
print("Type data dari ", data_boolean_true, ", adalah ", type(data_boolean_true))
print("Type data dari ", data_boolean_false, ", adalah ", type(data_boolean_false))

#tipe data khusus
data_complex=complex(5,10)
print("Type data dari ", data_complex, ", adalah ", type(data_complex))

#type bahasa C
from ctypes import c_double
data_c_double=c_double(100.50)
print("Type data dari ", data_c_double, ", adalah ", type(data_c_double))







