sum: int=0
szorzat: int=1

print("Kezdő érték")
kezdo:int=int(input())

print("Végső érték")
vegso:int=int(input())


for i in range(kezdo, vegso +1, 1):
    sum += i
    szorzat *= i

print(f"Az összeg = {sum}")
print(f"A szorzat ={szorzat} ")