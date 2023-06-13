import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
import csv

# ---------------- Membuat Tabel --------------------------------------------------------------------------

# Tabel Publikasi Dosen

with open('database/publikasi_dosen.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Judul', 'No Dosen', 'No Bidang', 'Judul', 'Nilai Prediksi'])

    df1 = pd.read_csv(f'hasil_naive_bayes_data_dosen/prediksi_5.csv', encoding='ISO-8859-1')

    list_no_judul = list(df1['No Judul'])
    list_no_judul_dokumen = []

    for data in list_no_judul:
        if data not in list_no_judul_dokumen:
            list_no_judul_dokumen.append(data)

    for no_judul_dokumen in list_no_judul_dokumen:
        no_dosen = list(df1['No Dosen'].loc[(df1['No Judul'] == no_judul_dokumen)])
        no_bidang = list(df1['No Bidang'].loc[(df1['No Judul'] == no_judul_dokumen)])
        judul = list(df1['Judul'].loc[(df1['No Judul'] == no_judul_dokumen)])
        nilai_prediksi = list(df1['Nilai Prediksi'].loc[(df1['No Judul'] == no_judul_dokumen)])

        writer.writerow([no_judul_dokumen, no_dosen[0], no_bidang[0], judul[0], nilai_prediksi[0]])

# Tabel Model Publikasi Dosen

with open('database/model_publikasi_dosen.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Judul Model', 'No Bidang Penelitian', 'Judul Model'])

    df1 = pd.read_csv(f'data/data_model/data_model.csv', encoding='ISO-8859-1')

    list_no_judul_model = list(df1['No'])
    list_no_judul_model_dokumen = []

    for data in list_no_judul_model:
        if data not in list_no_judul_model_dokumen:
            list_no_judul_model_dokumen.append(data)

    for no_judul_dokumen in list_no_judul_model_dokumen:
        no_bidang = list(df1['No Bidang'].loc[(df1['No'] == no_judul_dokumen)])
        judul = list(df1['Judul Jurnal'].loc[(df1['No'] == no_judul_dokumen)])

        writer.writerow([no_judul_dokumen, no_bidang[0], judul[0]])

# Tabel Minat Bidang Penelitian

with open('database/minat_bidang_penelitian.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Bidang Penelitian', 'No Dosen', 'No Bidang', 'Persentase'])

    df1 = pd.read_csv(f'kecenderungan_bidang_dosen/kecenderungan_bidang_dosen.csv', encoding='ISO-8859-1')

    list_no_kecenderungan_bidang = list(df1['No Dosen'])
    list_no_kecenderungan_bidang_dokumen = []

    for data in list_no_kecenderungan_bidang:
        if data not in list_no_kecenderungan_bidang_dokumen:
            list_no_kecenderungan_bidang_dokumen.append(data)

    no_minat_bidang_penelitian = 0

    for no_judul_dokumen in list_no_kecenderungan_bidang_dokumen:
        no_bidang_penelitian = list(df1['No Bidang'].loc[(df1['No Dosen'] == no_judul_dokumen)])
        no_minat_bidang_penelitian  = no_minat_bidang_penelitian + 1
        persentase = list(df1['Persentase'].loc[(df1['No Dosen'] == no_judul_dokumen)])

        writer.writerow([no_minat_bidang_penelitian, no_judul_dokumen, no_bidang_penelitian[0], persentase[0]])

# Tabel Minat Grup Riset

with open('database/minat_grup_riset.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Minat Grup Riset', 'No Dosen', 'No Grup Riset 1', 'Persentase Grup Riset 1', 'No Grup Riset 2', 'Persentase Grup Riset 2'])

    df1 = pd.read_csv(f'kecenderungan_bidang_dosen/daftar_kecenderungan_grup_riset_dosen.csv', encoding='ISO-8859-1')

    list_no_kecenderungan_bidang = list(df1['No Dosen'])
    list_no_kecenderungan_bidang_dokumen = []

    for data in list_no_kecenderungan_bidang:
        if data not in list_no_kecenderungan_bidang_dokumen:
            list_no_kecenderungan_bidang_dokumen.append(data)

    no_minat_grup_riset = 0

    for no_judul_dokumen in list_no_kecenderungan_bidang_dokumen:
        no_minat_grup_riset = no_minat_grup_riset + 1
        no_grup_riset_1 = list(df1['No Grup Riset 1'].loc[(df1['No Dosen'] == no_judul_dokumen)])
        no_grup_riset_2  = list(df1['No Grup Riset 2'].loc[(df1['No Dosen'] == no_judul_dokumen)])
        persentase_1 = list(df1['Persentase Grup Riset 1'].loc[(df1['No Dosen'] == no_judul_dokumen)])
        persentase_2 = list(df1['Persentase Grup Riset 2'].loc[(df1['No Dosen'] == no_judul_dokumen)])

        writer.writerow([no_minat_grup_riset, no_judul_dokumen, no_grup_riset_1[0], persentase_1[0], no_grup_riset_2[0], persentase_2[0]])

# ----------------------------------- Memasukkan File ke Database ------------------------------------------------------

# Memasukkan Isi Tabel Dosen ------------------------------------------------------------------------------

# data_dosen = pd.read_csv('database/dosen.csv', encoding='ISO-8859-1')
# data_dosen.head()
#
# a = 0
#
# try:
#     conn = msql.connect(host='localhost',
#                            database='database_skripsi_backup', user='root',
#                            password='')
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
#         cursor.execute("DELETE FROM dosen")
#         print("tabel dosen berhasil dikosongkan")
#         for i, row in data_dosen.iterrows():
#             sql = "INSERT INTO dosen (ID_DOSEN, NAMA_DOSEN, LINK_SCHOLAR) VALUES (%s,%s,%s)"
#             cursor.execute(sql, tuple(row))
#             print("dosen Inserted")
#             a = a + 1
#             print(a)
#             conn.commit()
# except Error as e:
#     print("Error while connecting to MySQL", e)

# Memasukkan Isi Tabel Grup Riset ----------------------------------------------------------------------------

# data_grup_riset = pd.read_csv('database/grup_riset.csv', encoding='ISO-8859-1')
# data_grup_riset.head()
#
# a = 0
#
# try:
#     conn = msql.connect(host='localhost',
#                            database='database_skripsi_backup', user='root',
#                            password='')
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
#         cursor.execute("DELETE FROM group_riset")
#         print("tabel group_riset berhasil dikosongkan")
#         for i, row in data_grup_riset.iterrows():
#             sql = "INSERT INTO group_riset (ID_GROUP_RISET, GROUP_RISET) VALUES (%s,%s)"
#             cursor.execute(sql, tuple(row))
#             print("group_riset Inserted")
#             a = a + 1
#             print(a)
#             conn.commit()
# except Error as e:
#     print("Error while connecting to MySQL", e)

# Memasukkan Isi Tabel Bidang Penelitian ----------------------------------------------------------------------------

# data_grup_riset = pd.read_csv('database/bidang_penelitian.csv', encoding='ISO-8859-1')
# data_grup_riset.head()
#
# a = 0
#
# try:
#     conn = msql.connect(host='localhost',
#                            database='database_skripsi_backup', user='root',
#                            password='')
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
#         cursor.execute("DELETE FROM bidang_penelitian")
#         print("tabel bidang_penelitian berhasil dikosongkan")
#         for i, row in data_grup_riset.iterrows():
#             sql = "INSERT INTO bidang_penelitian (ID_BIDANG_PENELITIAN, ID_GROUP_RISET, BIDANG_PENELITIAN) VALUES (%s,%s,%s)"
#             cursor.execute(sql, tuple(row))
#             print("bidang_penelitian Inserted")
#             a = a + 1
#             print(a)
#             conn.commit()
# except Error as e:
#     print("Error while connecting to MySQL", e)

# Memasukkan Isi Tabel Grup Riset Dosen ----------------------------------------------------------------------------

data_grup_riset = pd.read_csv('database/grup_riset_dosen.csv', encoding='ISO-8859-1')
data_grup_riset.head()

a = 0

try:
    conn = msql.connect(host='localhost',
                           database='database_skripsi_backup', user='root',
                           password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        # print("You're connected to database: ", record)
        cursor.execute("DELETE FROM group_riset_dosen")
        # print("tabel group_riset_dosen berhasil dikosongkan")
        for i, row in data_grup_riset.iterrows():
            sql = "INSERT INTO group_riset_dosen (ID_GROUP_RISET_DOSEN, ID_DOSEN, ID_GROUP_RISET_1, ID_GROUP_RISET_2) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # print("group_riset_dosen Inserted")
            a = a + 1
            # print(a)
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

# Memasukkan Isi Tabel Publikasi Dosen ----------------------------------------------------------------------------

data_grup_riset = pd.read_csv('database/publikasi_dosen.csv', encoding='ISO-8859-1')
data_grup_riset.head()

a = 0

try:
    conn = msql.connect(host='localhost',
                           database='database_skripsi_backup', user='root',
                           password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        # print("You're connected to database: ", record)
        cursor.execute("DELETE FROM publikasi_dosen")
        # print("tabel publikasi_dosen berhasil dikosongkan")
        for i, row in data_grup_riset.iterrows():
            sql = "INSERT INTO publikasi_dosen (ID_PUBLIKASI, ID_DOSEN, ID_BIDANG_PENELITIAN, JUDUL, NILAI_PREDIKSI) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # print("publikasi_dosen Inserted")
            a = a + 1
            # print(a)
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

# Memasukkan Isi Tabel Model Publikasi Dosen ----------------------------------------------------------------------------

# data_grup_riset = pd.read_csv('database/model_publikasi_dosen.csv', encoding='ISO-8859-1')
# data_grup_riset.head()
#
# a = 0
#
# try:
#     conn = msql.connect(host='localhost',
#                            database='database_skripsi_backup', user='root',
#                            password='')
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
#         cursor.execute("DELETE FROM model_publikasi_dosen")
#         print("tabel model_publikasi_dosen berhasil dikosongkan")
#         for i, row in data_grup_riset.iterrows():
#             sql = "INSERT INTO model_publikasi_dosen (ID_MODEL, ID_BIDANG_PENELITIAN, JUDUL) VALUES (%s,%s,%s)"
#             cursor.execute(sql, tuple(row))
#             print("model_publikasi_dosen Inserted")
#             a = a + 1
#             print(a)
#             conn.commit()
# except Error as e:
#     print("Error while connecting to MySQL", e)

# Memasukkan Isi Tabel Minat Bidang Penelitian Dosen ----------------------------------------------------------------------------

data_grup_riset = pd.read_csv('database/minat_bidang_penelitian.csv', encoding='ISO-8859-1')
data_grup_riset.head()

a = 0

try:
    conn = msql.connect(host='localhost',
                           database='database_skripsi_backup', user='root',
                           password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        # print("You're connected to database: ", record)
        cursor.execute("DELETE FROM minat_bidang_penelitian")
        # print("tabel minat_bidang_penelitian berhasil dikosongkan")
        for i, row in data_grup_riset.iterrows():
            sql = "INSERT INTO minat_bidang_penelitian (ID_MINAT_BIDANG_PENELITIAN, ID_DOSEN, ID_BIDANG_PENELITIAN, PERSENTASE) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # print("minat_bidang_penelitian Inserted")
            a = a + 1
            # print(a)
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

# Memasukkan Isi Tabel Minat Grup Riset Dosen

data_grup_riset = pd.read_csv('database/minat_grup_riset.csv', encoding='ISO-8859-1')
data_grup_riset.head()

a = 0

try:
    conn = msql.connect(host='localhost',
                           database='database_skripsi_backup', user='root',
                           password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        # print("You're connected to database: ", record)
        cursor.execute("DELETE FROM minat_group_riset")
        # print("tabel minat_group_riset berhasil dikosongkan")
        for i, row in data_grup_riset.iterrows():
            sql = "INSERT INTO minat_group_riset (ID_MINAT_GROUP_RISET, ID_DOSEN, ID_GROUP_RISET_1, PERSENTASE_GRUP_RISET_1, ID_GROUP_RISET_2, PERSENTASE_GRUP_RISET_2) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # print("minat_group_riset Inserted")
            a = a + 1
            # print(a)
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

print("Proses Memasukkan Data Hasil Klasifikasi Berhasil Dijalankan.")