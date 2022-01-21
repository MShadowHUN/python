import os
import time
 
number: int = None 
data: str = ""
 

while(number == None or number <0 or number > 9):
    data = input("Kerem a szamot 0 és 9 között:")
    if(data.replace("-","").isnumeric()):
        number=int(data)
        if(number != None and (number <0 or number > 9)):
            print("\nA szám nincs 0 és 9 között!")
            time.sleep(3)
            os.system("cls")    
    else:
        print("\nNem szamot adott meg!")
        time.sleep(3)
        os.system("cls")
print(f"A beolvasott szám {number}")

