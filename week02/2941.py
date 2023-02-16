word = input()

alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0

# 문제점 : 알파벳의 수가 다른데 어떻게 확인할 것인가?
# 각각의 알파벳과 공일한 변수를 찾아서 바꾸기
for i in alphabet:
    word = word.replace(i, '*')

print(len(word))
