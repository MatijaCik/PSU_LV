
'''Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao
ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka
riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.'''

rijecnik = {}
brojac = 0
try:
 dat = open("C:\\Users\\student\\Desktop\\song.txt", 'r')


except:
    print("datoteka ne postoji")

for line in dat:
   line = line.split()
   for rijec in line:
      if rijec in rijecnik:
         rijecnik[rijec] += 1
      else:
         rijecnik[rijec] = 1

unikatne_rijeci = []

for rijeci in rijecnik:
   if rijecnik[rijeci] == 1:
      unikatne_rijeci.append(rijeci)
      brojac += 1


print(rijecnik)
print("Broj unikatnih rijeci: ", brojac)
print(unikatne_rijeci)
