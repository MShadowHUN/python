ottel:int=0
hettel:int=0

print("Kezdő érték")
kezdo:int=int(input())

print("Végső érték")
vegso:int=int(input())

for i in range(kezdo,vegso, 1):
    if(i%5==0 and i%7==0):
        ottel+=i
        hettel+=i

    elif(i%5==0):
        ottel+=i
    
    elif(i%7==0):
        hettel+=i

if(ottel>hettel):
    print(f"{ottel}")
elif(ottel<hettel):
    print(f"{hettel}")
else:
    print("Egyenlőek")