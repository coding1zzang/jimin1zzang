# 참고

word = input().upper()
remove_word = list(set(word)) # 중복 문자는 제거

c = []

for s in remove_word:
    cnt = word.count(s)
    c.append(cnt)

if c.count(max(c)) > 1 : # 가장 많이 사용된 알파벳이 여러개인 경우
    print('?')
else:
    max_value = c.index(max(c))
    print(remove_word[max_value])

