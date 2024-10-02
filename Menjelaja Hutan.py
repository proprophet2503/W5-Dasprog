rows, cols, jumlah_gerakan = map(int, input().split())
hutan_emas = []

for i in range (rows):
    temp = list(map(int, input().split()))
    hutan_emas.append(temp)

gerakan = list(input())
# print(hutan_emas)
# print(hutan_emas[1][2]+hutan_emas[2][1])

row_sekarang = 0
col_sekarang = 0
jumlah_emas = hutan_emas[row_sekarang][col_sekarang]  
        

tetapdi_hutan = True
for arah_gerakan in gerakan:

    if(arah_gerakan == 'R' and col_sekarang + 1 <cols):
        col_sekarang+=1
        jumlah_emas = jumlah_emas + 3 + hutan_emas[row_sekarang][col_sekarang]
        
   
    elif(arah_gerakan == 'L' and col_sekarang - 1 >= 0):
        col_sekarang-=1
        jumlah_emas = jumlah_emas - 2+ hutan_emas[row_sekarang][col_sekarang]
   
    
    elif(arah_gerakan == 'D' and row_sekarang +1 <rows):
        row_sekarang+=1
        jumlah_emas = jumlah_emas - 2+ hutan_emas[row_sekarang][col_sekarang]
   
    
    elif(arah_gerakan == 'U' and row_sekarang - 1 >= 0):
        row_sekarang-=1
        jumlah_emas = jumlah_emas + 3 + hutan_emas[row_sekarang][col_sekarang]
      
    else:
        tetapdi_hutan = False

    if (tetapdi_hutan == False):
        print(jumlah_emas)
        print("gerakanmu salah bung!")
        break
    
    

if (tetapdi_hutan):
     print(jumlah_emas)
        
'''
berarti bisa gerak di pathnya
tapi gabisa input gerakannya


'''


