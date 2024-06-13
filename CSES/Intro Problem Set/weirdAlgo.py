x = int(input())

print(int(x), end=" ")
while(x!=1):
    if x%2 == 0:
        x/=2
        print(int(x), end=" ")
    else:
        x = 3*x+1
        print(int(x), end=" ")