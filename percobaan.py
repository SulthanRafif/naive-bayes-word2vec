import pandas as pd

# ------------------------------------- Mengecek nama dosen yang bukan nama dosen --------------------------------- #

print('percobaan.py')

dfd = pd.read_csv(f'../../Program_Klasifikasi/data_dosen_sistem/id_dosen/id_dosen.csv')
df1 = pd.read_csv(f'../../Program_Klasifikasi/data_dosen_sistem/data/data_judul_dosen/data_judul_dosen.csv', encoding='ISO-8859-1')

list_nama_dosen = list(dfd['Nama Dosen'])

no = list(df1['No'])
dosen = list(df1['Nama Dosen'])
list_dosen = []

for data in dosen:
    if data not in list_dosen:
        list_dosen.append(data)

panjang_list_dosen = len(list_dosen)
panjang_list_nama_dosen = len(list_nama_dosen)
s = dict()

bukan_nama_dosen = 'nama dosen'

for i in range(panjang_list_nama_dosen):
    s[list_nama_dosen[i]] = 1
for i in range(panjang_list_dosen):
    if list_dosen[i] not in s.keys():
        bukan_nama_dosen = list_dosen[i]

print(bukan_nama_dosen)

# ------------------------------------- Menghilangkan BUG pada Proses Crawling ketika dijalankan di web ---------- #

if bukan_nama_dosen is not 'nama dosen':
    df2 = pd.read_csv(f'../../Program_Klasifikasi/data_dosen_sistem/data/data_judul_dosen/data_judul_dosen.csv', encoding='ISO-8859-1')
    df2.to_csv(f'../../Program_Klasifikasi/data_dosen_sistem/temporary_2/data_judul_dosen_3_number.csv', encoding='ISO-8859-1')

    with open(f'../../Program_Klasifikasi/data_dosen_sistem/temporary_2/data_judul_dosen_3_number.csv','r') as f:
        with open(f'../../Program_Klasifikasi/data_dosen_sistem/temporary_2/data_judul_dosen_3_number_updated.csv','w') as f1:
            next(f) # skip header line
            for line in f:
                f1.write(line)

    df3 = pd.read_csv(f'../../Program_Klasifikasi/data_dosen_sistem/temporary_2/data_judul_dosen_3_number_updated.csv', encoding='ISO-8859-1')
    header_new = ['Indeks','No','Nama Dosen','Judul Jurnal','Kata Judul Jurnal Hasil Filter']
    df3.to_csv(f'../../Program_Klasifikasi/data_dosen_sistem/temporary_2/data_judul_dosen_new.csv', encoding='ISO-8859-1', header=header_new)

    df = pd.read_csv(f'../../Program_Klasifikasi/data_dosen_sistem/temporary_2/data_judul_dosen_new.csv', encoding='ISO-8859-1')
    nomor_cek = list(df['Indeks'].loc[(df['Nama Dosen']) == bukan_nama_dosen])
    no_awal = nomor_cek[0]
    print(no_awal)
    last = list(df['Indeks'].iloc[[-1]])
    no_akhir = last[0]
    print(no_akhir)

    while no_awal <= no_akhir:
        index_names = df['Indeks'].loc[(df['Indeks']) == no_awal].index
        df.drop(index_names, inplace=True)
        print('Terhapus')
        no_awal += 1

    header_baru = ["indeks_1","indeks_2",'No','Nama Dosen','Judul Jurnal','Kata Judul Jurnal Hasil Filter']
    df.to_csv(f'../../Program_Klasifikasi/data_dosen_sistem/data/data_judul_dosen/data_judul_dosen_2.csv', encoding='ISO-8859-1', header=header_baru)

    print('Proses crawling berhasil dijalankan')












