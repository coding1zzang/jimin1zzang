t = int(input())

for i in range(t):
    num, str = input().split()

    final_string=''
    for j in str:
        final_string += j * int(num)
    print(final_string)
