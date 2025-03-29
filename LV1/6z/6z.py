''' Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1]. Ova datoteka
sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham. Primjer dijela datoteke:
ham Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
ham Ok lar... Joking wif u oni...
spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken's stuff!
ham Yup next stop.
a) Izračunajte koliki je prosječan broj riječi u SMS porukama koje su tipa ham, a koliko je prosječan broj riječi u
porukama koje su tipa spam.
b) Koliko SMS poruka koje su tipa spam završava uskličnikom ?'''


spam_sum = 0
ham_sum = 0
spam_counter = 0
ham_counter = 0
usklicnici_counter = 0
try:
 dat = open("C:\\Users\\student\\Desktop\\SMSSpamCollection.txt", 'r')

except:
    print("Datoteka ne postoji")

for line in dat:
   line = line.split()
   if(line[0] == "ham"):
      ham_counter += 1
      ham_sum += len(line)
   elif(line[0] == "spam"):
      spam_counter += 1
      spam_sum += len(line)
      if("!" in line[-1]):
         usklicnici_counter += 1

print("prosjecan broj rijeci u sms porukama tipa ham: ", ham_sum/ham_counter)
print("prosjecan broj rijeci u sms porukama tipa spam: ", spam_sum/spam_counter)
print("broj sms poruka spam koje završavaju sa !", usklicnici_counter)