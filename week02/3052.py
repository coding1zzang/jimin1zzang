# set : 중복을 제거해줌
array = []

for i in range(10):
    array.append(int(input())%42)

array = set(array)
print(len(array))
