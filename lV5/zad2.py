'''Izgradite i evaluirajte algoritam K najbližih susjeda. Slijedite ovaj redoslijed:
a) Podijelite podatke na skup za učenje i skup za testiranje (omjer 80%-20%) pomoću funkcije
train_test_split. Koristite opciju stratify=y.
b) Pomoću StandardScaler skalirajte ulazne veličine.
c) Pomoću klase KNeighborsClassifier izgradite algoritam K najbližih susjeda.
d) Evaluirajte izgrađeni klasifikator na testnom skupu podataka:
a. prikažite matricu zabune
b. izračunajte točnost klasifikacije
c. izračunajte preciznost i odziv po klasama
e) Što se događa s rezultatima ako se koristi veći odnosno manji broj susjeda?
f) Što se događa s rezultatima ako ne koristite skaliranje ulaznih veličina?'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# ucitaj podatke za ucenje
df = pd.read_csv('C:\\Users\\student\\Desktop\\lV5\\occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[class_value])
    
x_train, x_test, y_train, y_test =train_test_split(df, test_size=0.2, train_size=0.8, random_state=None, shuffle=True, stratify=y)


print(x_train)
