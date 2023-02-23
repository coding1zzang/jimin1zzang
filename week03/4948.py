# 참고
import math

m = 123456

sosu = [True for _ in range(2 * m + 1)] 
sosu[0], sosu[1] = False, False


for i in range(2, int(math.sqrt(2 * m) + 1)):

    if sosu[i]: 
        j = 2 

        while i * j <= 2 * m: 
            sosu[i * j] = False 
            j += 1 


while True:
    n = int(input())
    if n == 0:
        break

    count = 0

    for i in range(n+1, 2 * n + 1): 

        if sosu[i]: 
            count += 1 

    print(count) 
