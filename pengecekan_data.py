import pandas as pd
import csv

df1 = pd.read_csv(f'temporary/prediksi_5.csv', encoding='ISO-8859-1')
df2 = pd.read_csv(f'hasil_naive_bayes_data_dosen/prediksi_5.csv', encoding='ISO-8859-1')

judul_dokumen_temporary = list(df1['Judul'])
judul_dokumen_asli = list(df2['Judul'])

panjang_dokumen_temporary = len(judul_dokumen_temporary)
panjang_dokumen_asli = len(judul_dokumen_asli)

s = dict()

for i in range(panjang_dokumen_asli):
    s[judul_dokumen_asli[i]]= 1
for i in range(panjang_dokumen_temporary):
    if judul_dokumen_temporary[i] not in s.keys():
        print(judul_dokumen_temporary[i])
