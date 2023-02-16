# 참고
t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    p = [j for j in range(1, n+1)]
    for a in range(k):
        for b in range(1,n):
            p[b] += p[b-1]

    print(p[-1])
