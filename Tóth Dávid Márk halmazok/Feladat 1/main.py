print("Kezdő érték=")
kezdo:int=int(input())

print("Végső érték=")
vegso:int=int(input())

osszeg:int=0
szamokSzama:int=0
atlag:float=0
paratlanSzamokSzama:int=0
harommalOszhtatoSzamok:int=0

for i in range(kezdo,vegso,1):
    osszeg+=i
    szamokSzama +=1

    atlag= osszeg/szamokSzama

   
    if(i%3==0):
         harommalOszhtatoSzamok = i
         print(f"A {kezdo} és a {vegso} közti hárommal osztható számok:{harommalOszhtatoSzamok}") #Feladat 4
        
    if(i%2!=0):
        paratlanSzamokSzama +=1 #Feladat 3
    if((i%2==0 and i%11==0)or (i%2!=0 and i%7==0)):
        print(f"A {kezdo} és a {vegso} közt van olyan szám mely páros és osztható tizeneggyel vagy páratlan és osztható héttel.") #Feladat 5
else:
    print(f"A {kezdo} és a {vegso} közt nincs olyan szám mely páros és osztható tizeneggyel vagy páratlan és osztható héttel.")

print(f"A {kezdo} és a {vegso} közti számok összege: { osszeg }.") #Feladat 1
print(f"A {kezdo} és a {vegso} közti számok átlaga: {atlag }.") #Feladat 2
print(f"A {kezdo} és a {vegso} közti páratlan számok száma {paratlanSzamokSzama}.") #Feladat 3