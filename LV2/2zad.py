'''U direktoriju PSU_LV/LV2/ nalazi se datoteka mtcars.csv koja sadrži različita mjerenja provedena na 32
automobila (modeli 1973-74). Opis pojedinih varijabli nalazi se u datoteci mtcars_info.txt.
a) Učitajte datoteku mtcars.csv pomoću:
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)
b) Prikažite ovisnost potrošnje automobila (mpg) o konjskim snagama (hp) pomoću naredbe
matplotlib.pyplot.scatter.
c) Na istom grafu prikažite i informaciju o težini pojedinog vozila (npr. veličina točkice neka bude u skladu sa
težinom wt).
d) Izračunajte minimalne, maksimalne i srednje vrijednosti potrošnje (mpg) automobila.
e) Ponovite zadatak pod d), ali samo za automobile sa 6 cilindara (cyl).
'''
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)

#print(data)
mpg = data[:,0:1]
hp = data[:,3:4]
wt = data[:,5:6]
cyl = data[:,1:2]
#print(mpg)
#print(hp)

#plt.scatter(mpg, hp,linewidths=wt)
plt.scatter(mpg, hp, c='purple', s=wt*12, cmap='plasma')
plt.show()

print(np.min(mpg))
print(np.max(mpg))
print(np.mean(mpg))



'''for a in data[:,0:1]:
    if a == 6:
        mpg1= a[:,0:1]
'''
i = -1
mpg2 = []
for a in cyl:
    i += 1
    if a == 6:
        mpg2.append(mpg[i])      


print(np.min(mpg2))
print(np.max(mpg2))
print(np.mean(mpg2))        