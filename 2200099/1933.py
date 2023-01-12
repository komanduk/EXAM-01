N = int(input())
tmp = []
for n in range(1, N+1):
    if N%n == 0:
        tmp.append(n)
print(*tmp)