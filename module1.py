#7
numbers = [5, -3, 2, 8, 10, -1]


n = len(numbers)

for i in range(n):

for j in range(0, n-i-1):

if abs(numbers[j]) < abs (numbers[j+1]):

numbers[j], numbers[j+1] = numbers[j+1], numbers[j]



#11

n = int(input("Sisestage t�htede arv: "))


t�hestik = 'abcdefghijklmnopqrstuvwxyz'


for i in range(n):

 print(t�hestik[i], l�pp='')

 for j in range(i):

 print(t�hestik[i], l�pp='')

 print()

#16

import random
vastused = ["Jah, kindlasti!", "Jah!", "V�ib-olla!", "Ei!"]
print("Tere tulemast Jah/Ei k�simuste programmisse!")
k�simus = input("Kas sul on k�simus, millele soovid vastust (jah/ei)? ")
juhuslik_indeks = random.randint(0, len(vastused) - 1)
juhuslik_vastus = vastused[juhuslik_indeks]
print("M�tlen... " + juhuslik_vastus)

#18 �lesanne on k�skida kasutajal sisestada nimi ja vanus.
#kirjutage s�num, mis tervitab teda nimepidi ja �tleb talle, kui vana ta on.

nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))


print("Tere, {nimi}! Sa oled {vanus} aastat vana.")

#17 (loo nimekiri "maailm")

maailm = ["�un", "pirn", "maasikas", "oran�", "ploom"]

otsingup�ring= input("Sisestage oma otsingutermin: ")

for maailm in maailm:

if otsingup�ring in maailm: print(maailm)


#klassit��

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