osszeg:int=0
szamokSzama:int=0
eloJelValto:int=1

print("Kezdő érték")
kezdo:int=int(input())

print("Végső érték")
vegso:int=int(input())

for i in range(kezdo,vegso+1,1):
    osszeg+=i*eloJelValto

    eloJelValto=eloJelValto*(-1)
print(f"{osszeg}")