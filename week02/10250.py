t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    # 손님이 머물 층수 / 룸 넘버
    floor = n % h
    room = (n // h) + 1

    # 나누어 떨어지게 되면, 가장 높은 층에 머물어야 함
    if floor == 0:
        floor = h
        room -= 1
    
    print(floor * 100 + room)
