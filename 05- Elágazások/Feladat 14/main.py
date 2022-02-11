print("x=")
x:int=int(input())

print("y=")
y:int=int(input())

print("z=")
z:int=int(input())

if(x%y==0 and x%z==0):
    print(f"{x} osztható {y}-nal és {z}-vel")
elif(x%y==0):
    print(f"{x} osztható {y}-nal")
elif(x%z==0):
     print(f"{x} osztható {z}-vel")
else:
    print(f"{x} nem oszható se {y}-naé se {z}-vel")