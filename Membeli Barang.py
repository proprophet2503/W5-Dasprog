N, M = map(int, input(). split())

harga_barang = list(map(int, input().split(' ')))
uang_pecahan = list(map(int, input().split(' ')))

for i in range(len(harga_barang)):
    for j in range(len(harga_barang)):
        if harga_barang[j]>harga_barang[i]:
            harga_barang[j], harga_barang[i] = harga_barang[i], harga_barang[j]



for i in range(len(uang_pecahan)):
    for j in range(len(uang_pecahan)):
        if uang_pecahan[j]>uang_pecahan[i]:
            uang_pecahan[j], uang_pecahan[i] = uang_pecahan[i], uang_pecahan[j]


jumlah_harga = 0
jumlah_pecahan = 0

'''
cari jika bisa tidak ada minus atau plus maka harus dicari manual 
'''

for barang in harga_barang:
    if barang>=0:
        
        jumlah_harga+=barang
    
    
for uang in uang_pecahan:
    if uang < 0:
        
        jumlah_pecahan += uang

print(jumlah_pecahan-jumlah_harga)