P, T = list(map(int, input().split()))
i = 0
p = P
cnt = 0
while P > T-1:
    T +=1
    cnt +=1
    if P < T:
        break
print(cnt, T, P)
