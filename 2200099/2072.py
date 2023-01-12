T = int(input())
result = []
for t in range(1, T+1):
    number = list(map(int, input().split()))
    result = []
    for i in number:
        if i%2 != 0:
            result.append(i)
    print(f'#{t} {sum(result)}')

    