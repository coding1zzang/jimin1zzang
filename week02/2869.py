a, b, v = map(int, input().split())
day = 0

#math.ceil 로도 풀이 가능

# ** 막대 길이에서 달팽이가 낮에 움직이는 거리를 뺌
# 여기에 달팽이가 하루동안 움직이는 거리로 나눔
if (v-b)%(a-b) > 0:
    print((v-a) // (a-b) + 2)
else:
    print((v-a) // (a-b) + 1)



