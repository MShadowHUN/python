paros: int=0
paratlan:int=1

print("Kezdő érték=")
kezdo:int=int(input())

print("Végső érték=")
vegso:int=int(input())

for i in range(kezdo,vegso+1, 1):
    if(i%2==0):
        paros +=i
    else:
        paratlan *=i

print(f"A páros számok összege {paros}")
print(f"A pártalan számok szorzata {paratlan}")