paros:float=0
paratlan:float=0
atlag:float=0

print("Kezdő érték")
kezdo:int=int(input())

print("Végső érték")
vegso:int=int(input())

for i in range(kezdo,vegso, 1):
    if(i%2==0):
        paros+=i
    else:
        paratlan+=i

atlag=(paros+paratlan)/2
print(f"{atlag}")