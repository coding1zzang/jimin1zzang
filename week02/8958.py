n = int(input())

for _ in range(n):
    array = list(input())
    count = 0
    final_sum = 0
    for answer in array:
        if answer == 'O':
            count += 1
            final_sum += count
        else:
            count = 0
    print(final_sum)
