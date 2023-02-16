#참고..
all_num = set(range(1,10000))
generator = set()

for num in all_num:
    for i in str(num):
        num += int(i)
    generator.add(num)
    
self_num = sorted(all_num - generator)

for j in self_num:
    print(j)

