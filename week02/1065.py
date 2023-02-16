n = int(input())

def hansu(n):
    count = 0
    for i in range(1,n+1):
        array = list(map(int, str(i)))

        if i<100:
            count += 1
        elif (array[0] - array[1]) == (array[1] - array[2]):
            count += 1
    return count


print(hansu(n))
