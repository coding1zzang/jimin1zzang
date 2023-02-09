import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    
    #f-string 사용, {} 안에는 변수
    print(f'Case #{i+1}: {a+b}')
    
    
