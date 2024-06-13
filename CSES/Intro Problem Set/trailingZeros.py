x = int(input())
zeros, i=0, 1

while pow(5,i) <= x:
    zeros+=x//pow(5,i)
    i+=1

print(zeros)