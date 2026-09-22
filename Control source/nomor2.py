nomor_1 = int (input ("masukkan nomor pertama: "))
nomor_2 = int (input ("masukkan nomor kedua: "))
nomor_3 = int (input ("masukkan nomor ketiga: "))

if nomor_1 > nomor_2 and nomor_1 > nomor_3:
    print ("nomor terbesar adalah: ", nomor_1)
elif nomor_2 > nomor_1 and nomor_2 > nomor_3:
    print ("nomor terbesar adalah:", nomor_2)
elif nomor_3 > nomor_1 and nomor_3 > nomor_2:
    print ("nomor terbesar adalah:", nomor_3)
else:
    print ("nomor terbesar sama")
    




