print("Sorok száma=")
sor:int=int(input())

for i in range(0, sor+1, 1):
    for j in range(sor-i,0, -1):
        print(j, end=" ")
    print()