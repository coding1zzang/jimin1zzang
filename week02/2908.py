a, b = input().split()

# 숫자의 순서를 역순으로 바꾸는 코드 필요
# [::-1] 사용
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)
