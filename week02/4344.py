c = int(input())

for _ in range(c):
    array = list(map(int, input().split()))
    s = sum(array[1:])
    average = s/array[0]

    count = 0
    for j in array[1:]:
        if j > average:
            count += 1

    # 소수점 셋째 자리까지 출력하는법 : f string
    print(f'{count/array[0] * 100:.3f}%')
