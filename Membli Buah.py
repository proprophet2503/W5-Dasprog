N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

beli_able = 0
for harga in A:
    if(K>= harga):
        beli_able+=1

print(beli_able)