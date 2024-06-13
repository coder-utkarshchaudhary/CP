x = int(input())

if (x==1):
    print("1")
elif (x==2 or x==3):
    print("NO SOLUTION")
elif (x==4):
    print("3 1 4 2")
else:
    if (x%2 == 0):
        for i in range(x//2):
            print(f"{i+1} {i+1+x//2}", end=" ")
    else:
        for i in range(x//2):
            print(f"{i+1} {i+1+x//2+1}", end=" ")
        print(f"{x//2+1}")