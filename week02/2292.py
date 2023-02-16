n = int(input())

count = 1

# 1단계인 경우
if n == 1:
    print(1)

# 1단계 이상인 경우
else:

    n -= 1
    while n>0:
        n -= 6 * count
        count += 1
    print(count)
