N, baris, kolom = map(int, input().split())

siswa  = []
barisin = []
kolomin = []

for i in range (1, N+1):
    absen_siswa, barisnya, kolomnya = map(int, input().split())
    siswa.append(absen_siswa)
    barisin.append(barisnya)
    kolomin.append(kolomnya)


print(siswa)
print(barisin)
print(kolomin)
for i in range (0, N):
    ada_sebelah = False
    for j in range(0, N):
        if (kolomin[i] - 1 == kolomin[j] and barisin[i]==barisin[j]) or (kolomin[i] + 1 == kolomin[j] and barisin[i]==barisin[j]) :
            print(siswa[j])
            ada_sebelah = True
            break

    if not (ada_sebelah):
        print(0)







           