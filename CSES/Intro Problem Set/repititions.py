x = input()
max_count=1
count = 1

for i in range(len(x)-1):
    if x[i] == x[i+1]:
        count+=1
        if (count > max_count):
            max_count = count
    else:
        count=1

print(max_count)