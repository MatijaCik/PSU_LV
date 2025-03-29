'''Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije
oblika:

X-DSPAM-Confidence: <neki_broj>
koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. Koristite
datoteke mbox.txt i mbox-short.txt
Primjer
Ime datoteke: mbox.txt
Average X-DSPAM-Confidence: 0.894128046745
Ime datoteke: mbox-short.txt
Average X-DSPAM-Confidence: 0.750718518519
'''
spam_counter = 0
sum = 0.0

unos = input("unesite ime tekstualne datoteke \n")
datoteka = 'C:\\Users\\student\\Desktop\\'+unos+'.txt'
try:
  dat = open(datoteka, 'r')
except:
    print("Datoteka ne postoji")

for line in dat:
   line = line.split()
   if("X-DSPAM-Confidence:" in line):
      spam_counter += 1
      sum += float(line[1])


print("Srednja vrijednost pouzdanosti je : ", sum/spam_counter)