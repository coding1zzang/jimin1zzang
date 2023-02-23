# 참고
def sosu(x):

    if x == 1:
        return False
    
    for j in range(2, int(x**0.5) +1):
        if x % j == 0:
            return False
    
    return True


t = int(input())

for _ in range(t):
    num = int(input())

    for a in range(num//2, 0, -1):
        if sosu(a) and sosu(num-a):
            print(a, num-a)
            break
