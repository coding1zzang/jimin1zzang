total = int(input())
num = int(input())

price = 0
for _ in range(num):
    a, b = map(int, input().split())
    price += a*b

if price == total:
    print("Yes")
else:
    print("No")
