while True:
    # test case 의 개수가 정해지지 않았으므로 try - except
    # int 형 a, b 가 들어오는 경우 try 수행
    try: 
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
