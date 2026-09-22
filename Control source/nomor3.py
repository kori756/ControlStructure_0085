nomor_fibonachi = int (input ("masukkan angka:"))

a, b = 0, 1

for i in range (nomor_fibonachi):
    print (a, end = "")
    a, b = b, a + b