from matematikaFuggvenyek import *
from inputLib import *

osszeg:float=None
kulonbseg:float=None
szorzat:float=None
hanyados:float=None
x:float=None
y:float=None

while (x==None):
    x=tizedesSzamBeolvasas()

while (y==None):
    y=tizedesSzamBeolvasas()

osszeg=osszeadas(x,y)
kulonbseg=kivonas(x,y)
szorzat=szorzas(x,y)
hanyados=osztas(x,y)

print(f"A két szám {x} és {y} összege:{osszeg} \nkülönbsége:{kulonbseg} \nszorzata:{szorzat} \nhányadosa:{hanyados}")