print("Kezdő érték")
kezdo:int=int(input())

print("Végső érték")
vegso:int=int(input())

if(kezdo%2==0):
    kezdo+=1

for i in range(kezdo,vegso,2):
    print(i)