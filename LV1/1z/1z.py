'''  Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.
Primjer:
Radni sati: 35 h
eura/h: 8.5
Ukupno: 297.5 eura'''

Radni_sati = int(input("Unesite broj radnih sati \n"))
Satnica = float(input("Unesite satnicu \n"))

print('Radni sati :', Radni_sati)
print('Satnica: ', Satnica)
Ukupno = Radni_sati * Satnica
print('Ukupno: ', Ukupno)