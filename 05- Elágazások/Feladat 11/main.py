print("x=")
x:int=int(input())

if(x%2==0):
    print("páros")
else:
    print("páratlan")

if(x>=0):
    print("pozitív")
else:
    print("negatív")
    
if(x%5==0):
    print(f"{x} oszható 5-tel")
else:
    print(f"{x} nem oszható 5-tel")