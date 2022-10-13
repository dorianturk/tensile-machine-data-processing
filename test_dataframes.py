# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:53:23 2022

@author: zsk
"""
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style
import numpy as np
import xlsxwriter
from IPython import get_ipython

get_ipython().magic('reset -sf')

A=7*11
l=95

#Velicina grafa
x = 6.5
y = (10/15)*x

df = pd.read_csv('rezultati_kidalica/mjerenje19.5.Dorian.csv', header=1)

df = df.drop(df.columns[range(0,len(df.columns),4)], axis=1)
df = df.drop(df.columns[range(2,len(df.columns),3)], axis=1)
df = df.drop(index=0)
df = df.stack().str.replace(',','.').unstack().astype(float)


print(df)
st_pr=len(df.columns)
uzoraka=int(st_pr/2)
print("Uzoraka: ", uzoraka)
print("stupaca prije: ", st_pr)

df['Naprezanje'] = (df["Force"] / A).round(2)
df['Deformacija'] = (df["Stroke"] / l).round(6)

i = 0
for j in range(0,int((len(df.columns)/2)-2)):
    i += 1
    df['Naprezanje.' + str(i)] = (df["Force."+str(i)] / A).round(2)
    df['Deformacija.' + str(i)] = (df["Stroke."+str(i)] / l).round(6)
print(df)
#print(len(df.columns))#za kreiranje vise sheetova
st_nk=len(df.columns)
print("stupaca nakon:", st_nk)

#dijagrami svi
matplotlib.style.use('default')
fig, ax = plt.subplots(figsize=(x, y), layout='constrained')
i = 0
for j in range(1,uzoraka):
    i += 1
    #print(i)
    ax.plot('Deformacija.' + str(i), 'Naprezanje.' + str(i), label='uzorak '+str(i), data=df)
ax.set_xlabel('Deformacija')
ax.set_ylabel('Naprezanje, MPa')
ax.set_title('Naprezanje vs deformacija')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.savefig('dijagrami/svi.png')   
#ax.plot("Stroke", "Force", label='uzorak 1', data=df)
i = 0
for j in range(1, uzoraka):
    i += 1
    #print(i)
    fig, ax = plt.subplots(figsize=(x, y), layout='constrained')
    ax.plot('Deformacija.' + str(i), 'Naprezanje.' + str(i), label='uzorak '+str(i), data=df)
    ax.set_xlabel('Deformacija')
    ax.set_ylabel('Naprezanje, MPa')
    ax.set_title('Naprezanje vs deformacija')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.savefig(f'dijagrami/plot{str(i)} .png')   
#mjerenje.to_excel('test.xlsx', sheet_name='uzorak')
"""
"""
mjerenje = df [['Force', 'Stroke', 'Naprezanje', 'Deformacija']]

i = 0
for j in range(1, uzoraka):
    i += 1
    #print(i)
    globals()["mjerenje_" + str(i)] = df[["Force."+str(i) ,"Stroke."+str(i), "Naprezanje." + str(i), "Deformacija." + str(i)]].astype(float)
    #vars()['mjerenje_' + str(i)]['Naprezanje' + str(i)+', MPa'] = (vars()['mjerenje_' + str(i)]["Force."+str(i)] / A).round(2)
    #vars()['mjerenje_' + str(i)]['Deformacija' + str(i)] = (vars()['mjerenje_' + str(i)]["Stroke."+str(i)] / l).round(6)
   
#Spremanje dijagrama
 
   
with pd.ExcelWriter('obradeni_podaci.xlsx') as writer:
    i=0
    for i in range(int((len(df.columns)/2)-1)):
        i += 1
        vars()['mjerenje_' + str(i)].to_excel(writer, sheet_name='uzorak '+str(i))
for         
writer.sheets['mjerenje_' + str(i)]
worksheet.insert_image('E2',f'dijagrami/plot{str(i)} .png')
#print(mjerenje_1)

"""
fali nulto mjerenje, popravi kasnije
"""



