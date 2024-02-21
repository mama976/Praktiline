#7
numbers = [5, -3, 2, 8, 10, -1]


n = len(numbers)

for i in range(n):

for j in range(0, n-i-1):

if abs(numbers[j]) < abs (numbers[j+1]):

numbers[j], numbers[j+1] = numbers[j+1], numbers[j]



#11

n = int(input("Sisestage tähtede arv: "))


tähestik = 'abcdefghijklmnopqrstuvwxyz'


for i in range(n):

 print(tähestik[i], lõpp='')

 for j in range(i):

 print(tähestik[i], lõpp='')

 print()

#16

import random
vastused = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"]
print("Tere tulemast Jah/Ei küsimuste programmisse!")
küsimus = input("Kas sul on küsimus, millele soovid vastust (jah/ei)? ")
juhuslik_indeks = random.randint(0, len(vastused) - 1)
juhuslik_vastus = vastused[juhuslik_indeks]
print("Mõtlen... " + juhuslik_vastus)

#18 Ülesanne on käskida kasutajal sisestada nimi ja vanus.
#kirjutage sõnum, mis tervitab teda nimepidi ja ütleb talle, kui vana ta on.

nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))


print("Tere, {nimi}! Sa oled {vanus} aastat vana.")

#17 (loo nimekiri "maailm")

maailm = ["õun", "pirn", "maasikas", "oranþ", "ploom"]

otsingupäring= input("Sisestage oma otsingutermin: ")

for maailm in maailm:

if otsingupäring in maailm: print(maailm)


#klassitöö

#
for i in range(100):
    print("#",end="")
    sleep(random())
print()

#
for i in range(100):
    print(f"{i}",1*"#")
    sleep(random())
print()

#
for i in range(100,0,-1):
    sym=i*"#"
    print(replace(sym,)
    sleep(random())
print()


#
nimekirjal=[]
nimekirja=[]
n=int(input("Nimikirja suurus:"))
for i in ange(n):
    arv=randint(10,100)
    nimekirjal.append(arv)
    nimekirja.append(arv)
maksimum=nimekirja[0]
for arv in nimekirja:
    if arv>maksimum:
        maksimum=arv
        vajavarv=maksimum/len(nimekirja)
for i in range(len(nimekirja)):
    if nimekirja[i]==maksimum:
        nimekirja[i]=vajavarv
    print("nimekirjal")
    print("nimekirja")