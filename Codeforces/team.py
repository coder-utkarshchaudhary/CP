x = int(input())
question = []

for i in range(x):
    question.append(list(map(int, input().split(" "))))

count = 0
for i in question:
    if i[0]+i[1]+i[2] == 1:
        pass
    else:
        count+=1

print(count)