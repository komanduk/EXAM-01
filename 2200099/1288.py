T = int(input())
tmp = {0,1,2,3,4,5,6,7,8,9}
cnt = 0
for t in range(1,T+1):
    n = int(input())
    s = list(map(int,str(n)))
    y = []
    y_ = set(y)
    for i in range(0, 9999):
        if tmp != y_:
            y.append(i)
            cnt += 1
            y.sort()
            y_ = set(y)
        if tmp == y_:
            break
print(cnt, y_ )