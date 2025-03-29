'''
2.
Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). Također, ako je
broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku
'''

try:
 ocijena = float(input("Unesite float ocijenu od 0.0 do 1.0 \n"))
 if not (0.0 <= ocijena <= 1.0):
    print("Error broj je izvan podrucja")
 ocijena = float(ocijena)
except:
    print("Unesite samo brojeve float")

if(ocijena >= 0.9):
   print('A')
elif(ocijena  >= 0.8):
   print('B')
elif(ocijena >= 0.7):
   print('C')
elif(ocijena >= 0.6):
   print('D')
elif(ocijena < 0.6):
   print('F')