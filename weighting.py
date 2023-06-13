import pandas as pd
import csv
import math

# ------------------------ Fungsi Weighting ----------------------

# def weighting(no_dokumen):

# ------------------------ Perhitungan TF ------------------------
with open(f'hasil_weighting_data_model/tf_5.csv', 'w', newline='',
          encoding='ISO-8859-1') as file:
    writer = csv.writer(file)

    df1 = pd.read_csv(f'data/data_model/data_model.csv', encoding='ISO-8859-1')

    SistemCerdas = ["Skalabilitas dan Analitik Data",
                    "Penerapan Kecerdasan Buatan",
                    "Penerapan Data Besar",
                    "Penerapan Information Retrieval",
                    "Penerapan Sistem Pakar",
                    "Penerapan Penambangan Data",
                    "Penerapan Penambangan Teks",
                    "Penerapan Intelijen Bisnis",
                    "Penerapan Smart Living"]

    ComputerNetwork = ["Penerapan Komputasi Awan",
                       "Penerapan IoT",
                       "Penerapan Keamanan Data",
                       "Penerapan Keamanan Cyber",
                       "Penerapan Virtualisasi Jaringan",
                       "Penerapan Teknologi Jaringan",
                       "Penerapan Teknologi Nirkabel",
                       "Penerapan IT Forensik pada Jaringan",
                       "Penerapan Enkripsi"]

    ComputerVision = ["Penerapan Pengenalan Pola",
                      "Penerapan Watermarking pada Citra",
                      "Penerapan Kompresi Citra",
                      "Penerapan Pengolahan Citra",
                      "Penerapan Transformasi Citra",
                      "Penerapan Filtering Citra",
                      "Penerapan Morfologi Citra Digital"]

    InformationSystem = ["Integrasi Sistem dan Arsitektur",
                         "Penerapan Manajemen Informasi",
                         "Penerapan Sistem Informasi Geografis",
                         "Penerapan Global Professional Practice",
                         "Penerapan Sistem Peramalan",
                         "Penerapan Sistem Pendukung Keputusan",
                         "Penerapan Bisnis Elektronik Sistem Informasi",
                         "Penerapan Customer Relationship Management",
                         "Penerapan Pembelajaran Elektronik pada Sistem Informasi",
                         "Computational Thinking"]

    MultimediaDanGame = ["Pengembangan Game",
                         "Multimedia",
                         "Penerapan Augmented Reality"]

    no_bidang = 0

    grup_dokumen = [SistemCerdas, ComputerNetwork, ComputerVision, InformationSystem, MultimediaDanGame]

    nama_grup_dokumen = ['Sistem Cerdas', 'Computer Network', 'Computer Vision', 'Information System', 'Multimedia dan Game']

    no_grup = 0

    kata = list(df1['Kata Judul Jurnal Hasil Filter'])

    kata_dokumen = []

    array_header = ['Grup Riset', 'Bidang', 'Judul']

    for i in kata:
        if i not in kata_dokumen:
            kata_dokumen.append(i)
            array_header.append(i)

    writer.writerow(array_header)

    no_kata = 0

    hitung_tf = 0

    while no_grup < len(grup_dokumen):
        for data_bidang in grup_dokumen[no_grup]:
            print(data_bidang)
            buat_judul_dokumen = []
            no = list(df1['No'].loc[(df1['Bidang'] == data_bidang)])
            no_awal = no[0]
            no_akhir = no[len(no) - 1]
            no_hitung = no_awal
            while no_hitung <= no_akhir:
                judul = list(df1['Judul Jurnal'].loc[(df1['No'] == no_hitung)])
                buat_judul_dokumen.append(judul[0])
                array_row = []
                array_row.append(nama_grup_dokumen[no_grup])
                array_row.append(data_bidang)
                array_row.append(judul[0])
                kata = list(df1['Kata Judul Jurnal Hasil Filter'].loc[(df1['No'] == no_hitung)])
                for i in range(len(kata_dokumen)):
                    TF = kata.count(kata_dokumen[i])
                    array_row.append(TF)
                writer.writerow(array_row)
                no_hitung += 1
            print('')
            print(len(buat_judul_dokumen))
            print('')
        no_grup += 1

# ------------------------ Perhitungan DF ------------------------

with open(f'hasil_weighting_data_model/df_5.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['kata', 'df'])

    df2 = pd.read_csv(f'data/data_model/data_model.csv', encoding='ISO-8859-1')

    SistemCerdas = ["Skalabilitas dan Analitik Data",
                    "Penerapan Kecerdasan Buatan",
                    "Penerapan Data Besar",
                    "Penerapan Information Retrieval",
                    "Penerapan Sistem Pakar",
                    "Penerapan Penambangan Data",
                    "Penerapan Penambangan Teks",
                    "Penerapan Intelijen Bisnis",
                    "Penerapan Smart Living"]

    ComputerNetwork = ["Penerapan Komputasi Awan",
                       "Penerapan IoT",
                       "Penerapan Keamanan Data",
                       "Penerapan Keamanan Cyber",
                       "Penerapan Virtualisasi Jaringan",
                       "Penerapan Teknologi Jaringan",
                       "Penerapan Teknologi Nirkabel",
                       "Penerapan IT Forensik pada Jaringan",
                       "Penerapan Enkripsi"]

    ComputerVision = ["Penerapan Pengenalan Pola",
                      "Penerapan Watermarking pada Citra",
                      "Penerapan Kompresi Citra",
                      "Penerapan Pengolahan Citra",
                      "Penerapan Transformasi Citra",
                      "Penerapan Filtering Citra",
                      "Penerapan Morfologi Citra Digital"]

    InformationSystem = ["Integrasi Sistem dan Arsitektur",
                         "Penerapan Manajemen Informasi",
                         "Penerapan Sistem Informasi Geografis",
                         "Penerapan Global Professional Practice",
                         "Penerapan Sistem Peramalan",
                         "Penerapan Sistem Pendukung Keputusan",
                         "Penerapan Bisnis Elektronik Sistem Informasi",
                         "Penerapan Customer Relationship Management",
                         "Penerapan Pembelajaran Elektronik pada Sistem Informasi",
                         "Computational Thinking"]

    MultimediaDanGame = ["Pengembangan Game",
                         "Multimedia",
                         "Penerapan Augmented Reality"]

    no_bidang = 0

    grup_dokumen = [SistemCerdas, ComputerNetwork, ComputerVision, InformationSystem, MultimediaDanGame]

    nama_grup_dokumen = ['Sistem Cerdas', 'Computer Network', 'Computer Vision', 'Information System',
                         'Multimedia dan Game']

    no_grup = 0

    print('')

    katanya = []

    while no_grup < len(grup_dokumen):
        for data_bidang in grup_dokumen[no_grup]:
            print(data_bidang)
            no = list(df1['No'].loc[(df1['Bidang'] == data_bidang)])
            no_awal = no[0]
            no_akhir = no[len(no) - 1]
            no_hitung = no_awal
            while no_hitung <= no_akhir:
                kata = list(df1['Kata Judul Jurnal Hasil Filter'].loc[(df1['No'] == no_hitung)])
                kata_pisah = []
                for data_kata in kata:
                    if data_kata not in kata_pisah:
                        kata_pisah.append(data_kata)
                print(kata_pisah)
                for a in kata_pisah:
                    katanya.append(a)
                no_hitung += 1
        no_grup += 1

    print('')

    print(katanya)

    print('')

    str3 = []

    for i in katanya:
        if i not in str3:
            str3.append(i)
    for i in range(0, len(str3)):
        print(str3[i])
        print(katanya.count(str3[i]))
        writer.writerow([str3[i], katanya.count(str3[i])])

# ------------------------ Perhitungan IDF ------------------------

with open(f'hasil_weighting_data_model/idf_5.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['kata', 'df', 'idf'])

    df2 = pd.read_csv(f'data/data_model/data_model.csv', encoding='ISO-8859-1')

    SistemCerdas = ["Skalabilitas dan Analitik Data",
                    "Penerapan Kecerdasan Buatan",
                    "Penerapan Data Besar",
                    "Penerapan Information Retrieval",
                    "Penerapan Sistem Pakar",
                    "Penerapan Penambangan Data",
                    "Penerapan Penambangan Teks",
                    "Penerapan Intelijen Bisnis",
                    "Penerapan Smart Living"]

    ComputerNetwork = ["Penerapan Komputasi Awan",
                       "Penerapan IoT",
                       "Penerapan Keamanan Data",
                       "Penerapan Keamanan Cyber",
                       "Penerapan Virtualisasi Jaringan",
                       "Penerapan Teknologi Jaringan",
                       "Penerapan Teknologi Nirkabel",
                       "Penerapan IT Forensik pada Jaringan",
                       "Penerapan Enkripsi"]

    ComputerVision = ["Penerapan Pengenalan Pola",
                      "Penerapan Watermarking pada Citra",
                      "Penerapan Kompresi Citra",
                      "Penerapan Pengolahan Citra",
                      "Penerapan Transformasi Citra",
                      "Penerapan Filtering Citra",
                      "Penerapan Morfologi Citra Digital"]

    InformationSystem = ["Integrasi Sistem dan Arsitektur",
                         "Penerapan Manajemen Informasi",
                         "Penerapan Sistem Informasi Geografis",
                         "Penerapan Global Professional Practice",
                         "Penerapan Sistem Peramalan",
                         "Penerapan Sistem Pendukung Keputusan",
                         "Penerapan Bisnis Elektronik Sistem Informasi",
                         "Penerapan Customer Relationship Management",
                         "Penerapan Pembelajaran Elektronik pada Sistem Informasi",
                         "Computational Thinking"]

    MultimediaDanGame = ["Pengembangan Game",
                         "Multimedia",
                         "Penerapan Augmented Reality"]

    no_bidang = 0

    grup_dokumen = [SistemCerdas, ComputerNetwork, ComputerVision, InformationSystem, MultimediaDanGame]

    nama_grup_dokumen = ['Sistem Cerdas', 'Computer Network', 'Computer Vision', 'Information System',
                         'Multimedia dan Game']

    no_grup = 0

    judul = list(df2['Judul Jurnal'])

    judul_dokumen = []

    for i in judul:
        if i not in judul_dokumen:
            judul_dokumen.append(i)

    jumlah_dokumen = len(judul_dokumen)

    print('')

    katanya = []

    while no_grup < len(grup_dokumen):
        for data_bidang in grup_dokumen[no_grup]:
            print(data_bidang)
            no = list(df2['No'].loc[(df2['Bidang'] == data_bidang)])
            no_awal = no[0]
            no_akhir = no[len(no) - 1]
            no_hitung = no_awal
            while no_hitung <= no_akhir:
                kata = list(df2['Kata Judul Jurnal Hasil Filter'].loc[(df2['No'] == no_hitung)])
                kata_pisah = []
                for data_kata in kata:
                    if data_kata not in kata_pisah:
                        kata_pisah.append(data_kata)
                print(kata_pisah)
                for a in kata_pisah:
                    katanya.append(a)
                no_hitung += 1
        no_grup += 1

    print('')

    print(katanya)

    print('')

    str3 = []

    for i in katanya:
        if i not in str3:
            str3.append(i)
    for i in range(0, len(str3)):
        print(str3[i])
        print(katanya.count(str3[i]))
        hitung_idf = math.log10(jumlah_dokumen / katanya.count(str3[i]))
        writer.writerow([str3[i], katanya.count(str3[i]), hitung_idf])

# ------------------------ Perhitungan TF-IDF ------------------------

with open(f'hasil_weighting_data_model/tf_idf_5.csv', 'w', newline='',
          encoding='ISO-8859-1') as file:
    writer = csv.writer(file)

    df1 = pd.read_csv(f'data/data_model/data_model.csv', encoding='ISO-8859-1')

    df2 = pd.read_csv(f'hasil_weighting_data_model/idf_5.csv')

    SistemCerdas = ["Skalabilitas dan Analitik Data",
                    "Penerapan Kecerdasan Buatan",
                    "Penerapan Data Besar",
                    "Penerapan Information Retrieval",
                    "Penerapan Sistem Pakar",
                    "Penerapan Penambangan Data",
                    "Penerapan Penambangan Teks",
                    "Penerapan Intelijen Bisnis",
                    "Penerapan Smart Living"]

    ComputerNetwork = ["Penerapan Komputasi Awan",
                       "Penerapan IoT",
                       "Penerapan Keamanan Data",
                       "Penerapan Keamanan Cyber",
                       "Penerapan Virtualisasi Jaringan",
                       "Penerapan Teknologi Jaringan",
                       "Penerapan Teknologi Nirkabel",
                       "Penerapan IT Forensik pada Jaringan",
                       "Penerapan Enkripsi"]

    ComputerVision = ["Penerapan Pengenalan Pola",
                      "Penerapan Watermarking pada Citra",
                      "Penerapan Kompresi Citra",
                      "Penerapan Pengolahan Citra",
                      "Penerapan Transformasi Citra",
                      "Penerapan Filtering Citra",
                      "Penerapan Morfologi Citra Digital"]

    InformationSystem = ["Integrasi Sistem dan Arsitektur",
                         "Penerapan Manajemen Informasi",
                         "Penerapan Sistem Informasi Geografis",
                         "Penerapan Global Professional Practice",
                         "Penerapan Sistem Peramalan",
                         "Penerapan Sistem Pendukung Keputusan",
                         "Penerapan Bisnis Elektronik Sistem Informasi",
                         "Penerapan Customer Relationship Management",
                         "Penerapan Pembelajaran Elektronik pada Sistem Informasi",
                         "Computational Thinking"]

    MultimediaDanGame = ["Pengembangan Game",
                         "Multimedia",
                         "Penerapan Augmented Reality"]

    no_bidang = 0

    grup_dokumen = [SistemCerdas, ComputerNetwork, ComputerVision, InformationSystem, MultimediaDanGame]

    nama_grup_dokumen = ['Sistem Cerdas', 'Computer Network', 'Computer Vision', 'Information System',
                         'Multimedia dan Game']

    no_grup = 0

    kata = list(df1['Kata Judul Jurnal Hasil Filter'])

    kata_dokumen = []

    array_header = ['Grup Riset', 'Bidang', 'Judul']

    for i in kata:
        if i not in kata_dokumen:
            kata_dokumen.append(i)
            array_header.append(i)

    writer.writerow(array_header)

    no_kata = 0

    hitung_tf = 0

    idf_1 = list(df2['kata'])
    idf_2 = list(df2['df'])
    idf_3 = list(df2['idf'])

    while no_grup < len(grup_dokumen):
        for data_bidang in grup_dokumen[no_grup]:
            print(data_bidang)
            buat_judul_dokumen = []
            no = list(df1['No'].loc[(df1['Bidang'] == data_bidang)])
            no_awal = no[0]
            no_akhir = no[len(no) - 1]
            no_hitung = no_awal
            while no_hitung <= no_akhir:
                judul = list(df1['Judul Jurnal'].loc[(df1['No'] == no_hitung)])
                buat_judul_dokumen.append(judul[0])
                array_row = []
                array_row.append(nama_grup_dokumen[no_grup])
                array_row.append(data_bidang)
                array_row.append(judul[0])
                kata = list(df1['Kata Judul Jurnal Hasil Filter'].loc[(df1['No'] == no_hitung)])
                for i in range(len(kata_dokumen)):
                    index_kata = idf_1.index(kata_dokumen[i])
                    idf = idf_3[index_kata]
                    perhitungan = idf * kata.count(kata_dokumen[i])
                    array_row.append(perhitungan)
                writer.writerow(array_row)
                no_hitung += 1
        no_grup += 1

# ------------------------ Panggil Fungsi Weighting ------------------------

# no_dokumen = 0
# total_dokumen = 3

# while no_dokumen < total_dokumen:
#     nomor = no_dokumen + 1
#     weighting(nomor)
#     no_dokumen += 1