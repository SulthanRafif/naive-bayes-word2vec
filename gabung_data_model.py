import pandas as pd
import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

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

df1 = pd.read_csv(f'filter_2/filter.csv', encoding='ISO-8859-1')
df2 = pd.read_csv(f'database/bidang_penelitian.csv')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

with open(f'data/data_model/data_model.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No', 'No Grup Riset', 'Grup Riset', 'No Bidang', 'Bidang', 'Judul Jurnal', 'Kata Judul Jurnal Hasil Filter'])

    no_dokumen = 0

    no_judul = 0

    while no_grup < len(grup_dokumen):
        print(f'Nama Grup Riset: {nama_grup_dokumen[no_grup]}')
        for data_bidang in grup_dokumen[no_grup]:
            print(f'Nama Bidang: {data_bidang}')
            no_bidang_penelitian = list(df2['No Bidang'].loc[(df2['Bidang Penelitian'] == data_bidang)])
            no_grup_riset = list(df2['No Grup Riset'].loc[(df2['Bidang Penelitian'] == data_bidang)])
            while no_dokumen < 5:
                no = no_dokumen + 1
                print(f'Nomor Dokumen: {no}')
                df = pd.read_csv(f'hasil_naive_bayes/data_{no}/prediksi_{no}.csv', encoding='ISO-8859-1')
                judul_model = list(df['Judul'].loc[(df['Nama Bidang'] == data_bidang)])
                for data_judul_model in judul_model:
                    print(f'Judul Dokumen: {data_judul_model}')
                    kata_dasar =  stemmer.stem(data_judul_model)
                    judul_jurnal_split = kata_dasar.split()
                    no_judul += 1
                    no_split = 0
                    while no_split < len(judul_jurnal_split):
                        kata = judul_jurnal_split[no_split]
                        array_kata = list(df1['Kata'])

                        panjang_data_kata = 1
                        panjang_array_kata = len(array_kata)

                        s = dict()

                        for i in range(panjang_array_kata):
                            s[array_kata[i]] = 1
                        for i in range(panjang_data_kata):
                            if kata not in s.keys():
                                print(f'Kata: {kata}')
                                writer.writerow([no_judul, no_grup_riset[0], nama_grup_dokumen[no_grup], no_bidang_penelitian[0], data_bidang, data_judul_model, kata])
                        no_split += 1
                no_dokumen += 1
            no_dokumen = 0
        no_grup += 1
