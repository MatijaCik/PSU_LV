'''Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
ispiše odgovarajuću poruku.'''

lst = []
counter = 0
while True:
 try:
  unos = input("unesi broj \n")
  if( unos == "Done"):
    break
  else:
   broj = int(unos)
   lst.append(broj)
   counter += 1

 except:
  print("Unositi samo brojeve !!")



print("Korisnik je unjeo :", counter, "brojeva")
avg = float(sum(lst)/len(lst))
print("Srednja vrijednost: ",avg)
print('minimalna vrijednost: ', min(lst))
print('maksimalna vrijednost: ', max(lst))
lst.sort()
print(lst)