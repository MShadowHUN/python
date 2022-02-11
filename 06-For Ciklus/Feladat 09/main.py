print("Kezdő érték")
kezdo:int=int(input())

print("Vég érték")
vegso:int=int(input())

if(vegso % 2!=0):
    vegso -=1

for i in range(vegso, kezdo, -2):
    print(i)