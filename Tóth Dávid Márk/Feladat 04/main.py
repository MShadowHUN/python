print("x=")
x:int=int(input())

if((x%3==0) and (x%4==0)):
    print("TEJ-be-RIZS")
elif(x%3==0):
    print("TEJ")
elif(x%4==0):
    print("RIZS")
else:
    print("Nem oszható sem 3-mal sem 4-gyel")