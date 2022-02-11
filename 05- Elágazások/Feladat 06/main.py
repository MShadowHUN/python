print("x=")
x:int=int(input())

print("y=")
y:int=int(input())

print("z=")
z:int=int(input())

if(x<y and y<z):
    print(f"{x}, {y}, {z}")
elif(x<z and z<y):
    print(f"{x}, {z}, {y}")

if(y<x and x<z):
    print(f"{y}, {x}, {z}")
elif(y<z and z<x):
    print(f"{y}, {z}, {x}")

if(z<x and x<y):
    print(f"{z}, {x}, {y}")
elif(z<y and y<x):
    print(f"{z}, {y}, {x}")

if(x==y and x<z):
    print(f"{x}, {y}, {z}")
elif(x==y and x>z):
    print(f"{z}, {x}, {y}")

if(x==z and x<y):
    print(f"{x}, {z}, {y}")
elif(x==z and x>y):
    print(f"{y}, {x}, {z}")

if(z==y and x<z):
    print(f"{x}, {y}, {z}")
elif(z==y and x>z):
    print(f"{z}, {y}, {x}")
if(x==y and y==z):
    print(f"{x}, {y}, {z}")