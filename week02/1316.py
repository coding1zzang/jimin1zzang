n = int(input())
count = 0

for i in range(n):
    word = input()
    answer = True

    for j in range(len(word)-1):
        if word[j] != word[j+1] and word[j] in word[j+1:]:
            answer = False
            break

    if answer == True:
        count += 1
    

print(count)
