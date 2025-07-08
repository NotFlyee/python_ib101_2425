import numpy as np

data = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding='utf8')#.reshape(8790, 53)
print(data[np.where(data['Energ_Kcal'] == np.max(data['Energ_Kcal']))[0][-1]]['Shrt_Desc'])
print(data[np.where(data['Sugar_Tot_g'] == np.min(data['Sugar_Tot_g']))[0][0]]['Shrt_Desc'])
print(data[np.where(data['Protein_g'] == np.max(data['Protein_g']))[0][0]]['Shrt_Desc'])
print(data[np.argmax(data['Vit_C_mg'])]['Shrt_Desc'])
