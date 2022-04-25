from szuperhos import Szuperhos

marvelSzuperhos:Szuperhos=Szuperhos("Vasember")
dcSzuperhos:Szuperhos=Szuperhos("Batman")

print(marvelSzuperhos)
print(dcSzuperhos)

if(marvelSzuperhos.tamad(dcSzuperhos)):
    print("Legyőzi")
else:
    print("Nem győzi le")