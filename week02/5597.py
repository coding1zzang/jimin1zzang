# 참고
array = [i for i in range(1,31)]


for i in range(28):
    student = int(input())
    array.remove(student)

print(min(array))
print(max(array))
