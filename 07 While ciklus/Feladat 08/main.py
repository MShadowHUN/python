import os
import time
import webbrowser

szam:int=-1
data:str=""

while(szam<0):
    data=input("1:Pepsi cola, 2: Citromos ice tea, 3: Narancslé, 4:Baracklé, 33: Surprise, 44:Surprise, 66:Surprise")
    if(data.isnumeric):
        szam=int(data)
    else:
        print("Nem számot adott meg vagy a szám mínusz")
        time.sleep(3)
        os.system('cls')

if(szam==1):
    print("Ön a Pepsi kólát választotta. Egészségére")
elif(szam==2):
    print("Ön a citromos ice teát választotta. Egészségére")
elif(szam==3):
    print("Ön a naracslevet választotta. Egészségére")
elif(szam==4):
    print("Ön a baracklevet válaszotta. Egészségére")
elif(szam==33):
    webbrowser.open("https://www.youtube.com/watch?v=43HCYSXZ9GI")
elif(szam==44):
    webbrowser.open("https://www.youtube.com/watch?v=KR48Q5U0AGA")
elif(szam==66):
    print("The time has come....Execute order 66.")
else:
    print("Ilyen számú ital nincs a listán")