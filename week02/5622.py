word = input().upper()

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
total_time = 0

for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            total_time += dial.index(j) + 3

print(total_time)
