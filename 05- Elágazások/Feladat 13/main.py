print("x=")
x:int=int(input())

if(x>=0 and x<=9):
    print("egyjegyű")
elif(x>=10 and x<=99):
    print("kétjegyű")
elif(x>=100 and x<=999):
    print("háromjegyű")
else:
    print("A szám több mint 3 jegyű vagy negatív")