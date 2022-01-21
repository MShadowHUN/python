#csomagok importálása
import os
#import keyboard
import time

#változók definiálása

#a szám amit be kell olvasni
#kezdőértéke None, miivel a while ciklusban ki tudom ezt használni az ismétlések vizsgálatára,
#vagyis a ciklust mindaddig futtatjuk, még a number  változónak nem lesz szám értéke.
number:int=None
    #segéd változó, a beolvasott értéket fogja tárolni
data:str=""

#while ciklus, ami mind addig fog futni még a number változó nem kap szám értéket, 
#azaz az értéke nem None lesz.
while(number==None):
    #beolvasás a konzolróll és a beolvasott értéket eltároljuk a data változóba
    data=input("Kérem a számot")
    #megvizsgáljuk, hogy a beolvasott érték(sting) számra alakítható e
    #mindegy, hogy ez a szám int vagy float típusú
    #isdigit() -> bool változót ad vissza
    if(data.isdigit()):
        #ha az is digit() függvény értéke igaz, akkor számot írt be a felhasználó
        #amit mi BIZTOS át tudunk alakítani szám típussá
        number=int(data)
    #az isdigit() függvény értéke hamis, azaz a felhasználó nem számot írt ne
    #így a number változó értéke továbbra is None marad, azaz a felhasználó nem számot írt be
    #a ciklust ismételni kell
    else:
        print("\nNem számot adott meg!")
        #a programot futtató szálat (thread) elaltatjuk 3 másodpercre
        time.sleep(3)
        #letöröljük a képernyőt
        os.system("cls")


        #print("\nA a folytatáshoz nyomja meg az ENTER billenyűt.")
        #egy végtelen WHILE ciklust írunk, mivel arra fogunk várni, hogy a felhasználó
        #lenyomja a kért billentyűzetet (ENTER)
        #while(True):
            #figyeljük, hogy a felhasználó lenyomta e az ENTER gombot
         #   if(keyboard.is_pressed('enter')):
            #letöröljük a képernyőt
         #       os.system("cls")
            #kilépünk a belső (végtelen) while ciklusból
         #       break

#kiírjuk a beolvasott számot
print(f"A beolvasott szám {number}")