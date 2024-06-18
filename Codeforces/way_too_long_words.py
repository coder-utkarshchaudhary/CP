x = int(input())
words = list()
for i in range(x):
    words.append(input())

for idx, i in enumerate(words):
    if len(i) > 10:
        words[idx] = i[0]+str(len(i)-2)+i[-1]

for j in words:
    print(j)