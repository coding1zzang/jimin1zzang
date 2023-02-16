n = int(input())
count = 0

while n >= 0:
    # 5로 나누어 떨어짐
    if n % 5 == 0:
        count += int(n//5)
        print(count)
        break

    # 3으로 계속 나누고 count 1 올리기
    n -= 3
    count += 1

# 나눌 수 없는 경우
else:
    print(-1)
