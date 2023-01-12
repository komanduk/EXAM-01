# list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list[:4])
# print(list[4:])

T = int(input())
tmp = []
y = []
m = []
d = []
for t in range(1, T+1):
    tmp = list(map(int, input()))
    print(tmp)
    for y_ in tmp[:4]:
        y.append(y_)
        for y1 in y:
            y2 = y1 + y1
    for m_ in tmp[4:6]:
        m.append(m_)
    for d_ in tmp[6:8]:
        d.append(d_)
print(f'#{t} {y2}{m}{d}')
