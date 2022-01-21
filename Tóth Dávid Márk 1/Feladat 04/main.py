print("a=")
a:int=int(input())

print("b=")
b:int=int(input())

print("c=")
c:int=int(input())

print("d=")
d:int=int(input())

osszeg:int= a + b
kulonbseg:int=c - d
hanyados:float= osszeg / kulonbseg

print(f"({a} + {b}) / ({c}-{d})= {hanyados}")