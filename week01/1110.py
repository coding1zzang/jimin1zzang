N = int(input())
answer = N
count = 0
while True:
    a = N // 10
    b = N % 10
    result = a + b
    N = 10*b + result%10
    count += 1
    if N == answer:
        break
print(count)
