import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''Napišite programski kod koji će iscrtati sljedeće slike za mtcars skup podataka:
1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara.
2. Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila s 4, 6 i 8 cilindara.
3. Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s ručnim mjenjačem veću
potrošnju od automobila s automatskim mjenjačem?
4. Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatskim
mjenjačem.'''
mtcars = pd.read_csv('C:\\Users\\student\\Desktop\\LV3\\mtcars.csv.csv')


sorted = mtcars.sort_values(by='cyl')
cyl = sorted.iloc[:,2:3]
mpg = sorted.iloc[:,1:2]
vector = np.vectorize(np.int_)
cyl = np.array([cyl])
x = vector(cyl)

vector = np.vectorize(np.int_)
mpg = np.array([mpg])
y = vector(mpg)
#cyl = [sorted.cyl.to_numpy()]
mpg = [sorted.mpg.to_numpy()]


plt.bar(x, y)
plt.title('Fruit Sales')
plt.xlabel('Cylinders')
plt.ylabel('mpg')
plt.show()