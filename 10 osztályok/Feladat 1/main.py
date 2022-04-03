import imp
from Teglalap import Teglalap
from kor import Kor
from Derekszog import Derekszog
from Egyenlooldal import Egyenlooldal
from Egyenloszar import Egyenloszar

#példányosítás
teglalap: Teglalap = Teglalap(10,20)
print("Téglalap: ")
print(teglalap)

negyzet: Teglalap = Teglalap(10,10)
print("\nNégyzet: ")
print(negyzet)

kor: Kor = Kor(10)
print("\nA kör kerülete és területe: ")
print(kor)

Derekszog: Derekszog=Derekszog(10,20,22.35)
print("\nDerékszögű háromszög")
print(Derekszog)

Egyenlooldal:Egyenlooldal=Egyenlooldal(10)
print("\n Egyelnő oldalú")
print(Egyenlooldal)

Egyenloszar:Egyenloszar=Egyenloszar(10,20)
print("\n Egyelnőszárú")
print(Egyenloszar)
