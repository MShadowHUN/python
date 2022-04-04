print("x=")
x:int=int(input())

if((x%2==0) and (x%5==0)):
    print("A szám páros és osztható 5-tel")
elif(x%2==0):
    print("A szám páros")
if(x<0 and x>-10):
    print("A szám negatív egyjegyű")
elif(x<-9 and x>-100):
     print("A szám negatív kétjegyű")
elif(x<-100):
    print("A szám negatív több mint kétjegyű")