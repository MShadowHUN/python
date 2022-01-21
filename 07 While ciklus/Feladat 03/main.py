import random
tip:int=None
szam:int=random.randint(0,9)
tippekSzama:int=1
temp:str=""

while(tip!=szam and tippekSzama<=5):
    temp=""
    while(temp=="" or temp.isspace() or not temp.isnumeric()):
        temp=input(f"Kérem az {tippekSzama}. tippet:")
        if(temp.isnumeric()):
            tip=int(temp)
            tippekSzama+=1
        else:
            print("Nem számot adott meg tippnek")
if(tip==szam):
    print(f"Gratulálunk, eltalálta a számot: {szam}")
else:
    print(f"Sajnos nem találta el a számot: {szam}")