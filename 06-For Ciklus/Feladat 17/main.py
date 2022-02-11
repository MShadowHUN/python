osszeg:int=0
szamokSzama:int=0
atlag:float=0

print("Kezdő érték")
kezdo:int=int(input())

print("Végső érték")
vegso:int=int(input())

for i in range(kezdo, vegso, 1):
    szamokSzama+=1
    osszeg+=i

atlag=osszeg/szamokSzama
print(f"{atlag}")