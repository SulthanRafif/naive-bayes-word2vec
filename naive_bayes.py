import pandas as pd
import csv

# ------------------------ Hitung NB Training ---------------------- #

with open(f'hasil_naive_bayes_data_dosen/nilai_nb_training_5.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)

    df1 = pd.read_csv(f'hasil_weighting_data_model/tf_idf_5.csv', encoding='ISO-8859-1')

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

    kata = list(df2['Kata Judul Jurnal Hasil Filter'])

    kata_dokumen = []

    array_header = ['Grup Riset', 'Bidang']

    for i in kata:
        if i not in kata_dokumen:
            kata_dokumen.append(i)
            array_header.append(i)

    writer.writerow(array_header)

    no_kata = 0

    hitung_kata_muncul = 0

    jumlah_kata_muncul = 0

    jumlah_kata_unik = len(kata_dokumen)

    hitung_kata = 0

    hitung_naive = 0

    while no_grup < len(grup_dokumen):
        while no_bidang < len(grup_dokumen[no_grup]):
            print(grup_dokumen[no_grup][no_bidang])
            print('')
            array_row = []
            array_row.append(nama_grup_dokumen[no_grup])
            array_row.append(grup_dokumen[no_grup][no_bidang])
            for data_kata in kata_dokumen:
                daftar_kata = list(df1[data_kata].loc[(df1['Bidang'] == grup_dokumen[no_grup][no_bidang])])
                for tf_kata in daftar_kata:
                    jumlah_kata_muncul = jumlah_kata_muncul + tf_kata
            for data_kata in kata_dokumen:
                print(data_kata)
                daftar_kata = list(df1[data_kata].loc[(df1['Bidang'] == grup_dokumen[no_grup][no_bidang])])
                print(daftar_kata)
                for tf_kata in daftar_kata:
                    hitung_kata_muncul = hitung_kata_muncul + tf_kata
                print(hitung_kata_muncul)
                print(jumlah_kata_muncul)
                print(jumlah_kata_unik)
                hitung_naive = (hitung_kata_muncul + 1) / (jumlah_kata_muncul + jumlah_kata_unik)
                print(hitung_naive)
                array_row.append(hitung_naive)
                hitung_kata_muncul = 0
                print('')
            writer.writerow(array_row)
            jumlah_kata_muncul = 0
            no_bidang += 1
        no_bidang = 0
        no_grup += 1

# ------------------------ Hitung Hasil Prediksi ----------------------

with open(f'hasil_naive_bayes_data_dosen/hasil_prediksi_5.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)

    df1 = pd.read_csv(f'data/data_judul_dosen/data_judul_dosen.csv', encoding='ISO-8859-1')
    df2 = pd.read_csv(f'hasil_naive_bayes_data_dosen/nilai_nb_training_5.csv', encoding='ISO-8859-1')
    df3 = pd.read_csv(f'hasil_weighting_data_model/tf_idf_5.csv', encoding='ISO-8859-1')

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

    nama_dosen = list(df1['Nama Dosen'])

    nama_dosen_dokumen = []

    for data_nama_dosen in nama_dosen:
        if data_nama_dosen not in nama_dosen_dokumen:
            nama_dosen_dokumen.append(data_nama_dosen)

    no_judul = 0

    no_grup = 0

    array_header = ['No Dosen', 'Nama Dosen', 'No Judul', 'Judul']

    while no_grup < len(grup_dokumen):
        while no_bidang < len(grup_dokumen[no_grup]):
            array_header.append(grup_dokumen[no_grup][no_bidang])
            no_bidang += 1
        no_bidang = 0
        no_grup += 1

    writer.writerow(array_header)

    hitung_total_judul = 0

    judul_hitung = list(df3['Judul'])

    judul_hitung_dokumen = []

    for z in judul_hitung:
        judul_hitung_dokumen.append(z)
    for z in range(0, len(judul_hitung_dokumen)):
        hitung_total_judul = hitung_total_judul + 1

    # print(hitung_total_judul)

    nilai_prob_bidang = []

    hitung_judul_bidang = 0

    no_grup = 0

    while no_grup < len(grup_dokumen):
        while no_bidang < len(grup_dokumen[no_grup]):
            judul_training = list(df3['Judul'].loc[(df3['Bidang']) == grup_dokumen[no_grup][no_bidang]])
            judul_training_dokumen = []
            for data_judul_training in judul_training:
                if data_judul_training not in judul_training_dokumen:
                    judul_training_dokumen.append(data_judul_training)
            for data_judul_training in range(0, len(judul_training_dokumen)):
                hitung_judul_bidang = hitung_judul_bidang + 1
            nilai_prob = hitung_judul_bidang / hitung_total_judul
            nilai_prob_bidang.append(nilai_prob)
            hitung_judul_bidang = 0
            no_bidang += 1
        no_bidang = 0
        no_grup += 1

    no_grup = 0

    hitung_prediksi = 0

    hitung_prob_kata = 1

    # print(nilai_prob_bidang)

    no_bidang = 0

    nomor_judul = 0

    for datanya_nama_dosen in nama_dosen_dokumen:
        # print(datanya_nama_dosen)
        judul_dokumen = []
        no_dosen = list(df1['No Dosen'].loc[(df1['Nama Dosen'] == datanya_nama_dosen)])
        no = list(df1['No Judul'].loc[(df1['Nama Dosen'] == datanya_nama_dosen)])
        no_awal = no[0]
        no_akhir = no[len(no) - 1]
        no_hitung = no_awal
        while no_hitung <= no_akhir:
            judul = list(df1['Judul Jurnal'].loc[(df1['No Judul'] == no_hitung)])
            judul_dokumen.append(judul[0])
            # print(judul[0].encode("utf-8"))
            no_hitung += 1
        for data_judul in judul_dokumen:
            nomor_judul += 1
            array_row = []
            array_row.append(no_dosen[0])
            array_row.append(datanya_nama_dosen)
            array_row.append(nomor_judul)
            array_row.append(data_judul)
            kata_dokumen = list(df1['Kata Judul Jurnal Hasil Filter'].loc[(df1['Judul Jurnal'] == data_judul)])
            while no_grup < len(grup_dokumen):
                while no_bidang < len(grup_dokumen[no_grup]):
                    # print(f'Judul Dokumen: {data_judul.encode("utf-8")}')
                    # print(f'Bidang Dokumen: {grup_dokumen[no_grup][no_bidang]}')
                    for data_kata_dokumen in kata_dokumen:
                        # print(f'Kata Dokumen: {data_kata_dokumen}')
                        try:
                            nilai_nb = list(df2[data_kata_dokumen].loc[df2['Bidang'] == grup_dokumen[no_grup][no_bidang]])
                            # print(f'Nilai Nb Kata : {nilai_nb[0]}')
                            hitung_prob_kata = hitung_prob_kata * nilai_nb[0]
                        except:
                            pass
                            # print('data kosong')
                    if hitung_prob_kata == 1:
                        hitung_prob_kata = 0
                    hitung_prediksi = nilai_prob_bidang[no_bidang] * hitung_prob_kata
                    # print(f'nilai prob bidang: {nilai_prob_bidang[no_bidang]}')
                    # print(f'Prob Kata: {hitung_prob_kata}')
                    # print(f'Hasil Prediksi: {hitung_prediksi}')
                    array_row.append(hitung_prediksi)
                    hitung_prob_kata = 1
                    no_bidang += 1
                    # print('')
                no_bidang = 0
                no_grup += 1
            writer.writerow(array_row)
            no_grup = 0

# ------------------------ Tampilkan Bidang Hasil Prediksi --------------------

with open(f'hasil_naive_bayes_data_dosen/prediksi_5.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Dosen', 'Nama Dosen', 'No Judul', 'Judul', 'No Grup Riset', 'Grup Riset', 'No Bidang', 'Nama Bidang', 'Nilai Prediksi', 'Deleted'])

    df1 = pd.read_csv(f'hasil_naive_bayes_data_dosen/hasil_prediksi_5.csv', encoding='ISO-8859-1')
    df2 = pd.read_csv(f'database/bidang_penelitian.csv', encoding='ISO-8859-1')

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

    nilai_terbesar = 0

    bidang = 'bidang'

    nama_dosen = list(df1['Nama Dosen'])

    nama_dosen_dokumen = []

    for data_nama_dosen in nama_dosen:
        if data_nama_dosen not in nama_dosen_dokumen:
            nama_dosen_dokumen.append(data_nama_dosen)

    nomor_dosen = 0
    nomor_judul = 0

    for datanya_nama_dosen in nama_dosen_dokumen:
        nomor_dosen += 1
        # print(datanya_nama_dosen)
        judul_dokumen = []
        no_dosen = list(df1['No Dosen'].loc[(df1['Nama Dosen'] == datanya_nama_dosen)])
        no = list(df1['No Judul'].loc[(df1['Nama Dosen'] == datanya_nama_dosen)])
        no_awal = no[0]
        no_akhir = no[len(no) - 1]
        no_hitung = no_awal
        while no_hitung <= no_akhir:
            judul = list(df1['Judul'].loc[(df1['No Judul'] == no_hitung)])
            judul_dokumen.append(judul[0])
            # print(judul[0].encode("utf-8"))
            no_hitung += 1
        for data_judul in judul_dokumen:
            nomor_judul += 1
            # print(data_judul.encode("utf-8"))
            while no_grup < len(grup_dokumen):
                for data_bidang in grup_dokumen[no_grup]:
                    # print(data_bidang)
                    try:
                        nilai_prediksi_dokumen = list(df1[data_bidang].loc[(df1['Judul'] == data_judul)])
                        # print(nilai_prediksi_dokumen[0])
                        if nilai_prediksi_dokumen[0] > nilai_terbesar:
                            nilai_terbesar = nilai_prediksi_dokumen[0]
                            no_bidang_penelitian = list(df2['No Bidang'].loc[(df2['Bidang Penelitian'] == data_bidang)])
                            no_grup_riset = list(df2['No Grup Riset'].loc[(df2['Bidang Penelitian'] == data_bidang)])
                            bidang = data_bidang
                            grup = nama_grup_dokumen[no_grup]
                    except:
                        pass
                        # print('data kosong')
                no_grup += 1
            # print('')
            # print(no_dosen[0])
            # print(nilai_terbesar)
            # print(bidang)
            # print(no_bidang_penelitian[0])
            # print(no_grup_riset[0])
            # print('')
            writer.writerow([no_dosen[0], datanya_nama_dosen, nomor_judul, data_judul, no_grup_riset[0], grup, no_bidang_penelitian[0], bidang, nilai_terbesar, 0])
            nilai_terbesar = 0
            no_grup = 0

print('Proses Naive Bayes berhasil dijalankan.')