print("a=")
a:int=int(input())

print("b=")
b:int=int(input())

print("c=")
c:int=int(input())

print("d=")
d:int=int(input())

osszeg:int= a + b
szorzat:int= osszeg * c
kulonbseg:int= szorzat - d
maradek:float=kulonbseg % 7

print(f"[({a} + {b})*{c}-{d}] % 7 = {maradek} ")