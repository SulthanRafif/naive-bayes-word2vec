import pandas as pd
import csv
import math

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

with open(f'../../Program_Klasifikasi/data_dosen_sistem/hitung_jumlah/sistem_cerdas.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    df1 = pd.read_csv(f'../../Program_Klasifikasi/data_dosen_sistem/kecenderungan_bidang_dosen/daftar_kecenderungan_dosen_2.csv', encoding='ISO-8859-1')
    writer.writerow(['No Bidang', 'Grup Riset', 'Bidang Penelitian', 'Jumlah Dosen', 'Presentase', 'Presentase2'])

    no_bidang = 0

    def round_decimals_up(number: float, decimals: int = 1):
        if not isinstance(decimals, int):
            raise TypeError("decimal places must be an integer")
        elif decimals < 0:
            raise ValueError("decimal places needs to be 0 or more")
        elif decimals == 0:
            return math.ceil(number)

        factor = 10 ** decimals
        return math.ceil(number * factor) / factor


    def round_decimals_up_up(number: float, decimals: int = 1):
        if not isinstance(decimals, int):
            raise TypeError("decimal places must be an integer")
        elif decimals < 0:
            raise ValueError("decimal places needs to be 0 or more")
        elif decimals == 0:
            return math.ceil(number)

        factor = 1 ** decimals
        return math.ceil(number * factor) / factor

    while no_grup < len(grup_dokumen):
        for data_bidang in grup_dokumen[no_grup]:
            no_bidang += 1
            bidang_nama_dosen = list(df1['Nama Dosen'].loc[(df1['Kecenderungan Bidang'] == data_bidang)])
            nama_dosen = list(df1['Nama Dosen'])
            presentase = len(bidang_nama_dosen)/len(nama_dosen)*100
            hasil = round_decimals_up(presentase)
            hasil2 = round_decimals_up_up(presentase)
            writer.writerow([no_bidang, nama_grup_dokumen[no_grup], data_bidang, len(bidang_nama_dosen), hasil, int(hasil2)])
        no_grup += 1

    print('Sistem Cerdas Selesai')

with open(f'../../Program_Klasifikasi/data_dosen_sistem/hitung_jumlah/presentase_kecenderungan_grup_riset.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    df1 = pd.read_csv(f'../../Program_Klasifikasi/data_dosen_sistem/kecenderungan_bidang_dosen/daftar_kecenderungan_dosen_2.csv', encoding='ISO-8859-1')
    writer.writerow(['No', 'Kecenderungan Grup Riset 1', 'Jumlah Dosen', 'Presentase', 'Presentase2' , 'Kecenderungan Grup Riset 2', 'Jumlah Dosen', 'Presentase', 'Presentase2'])

    no = 0

    def round_decimals_up(number: float, decimals: int = 1):
        if not isinstance(decimals, int):
            raise TypeError("decimal places must be an integer")
        elif decimals < 0:
            raise ValueError("decimal places needs to be 0 or more")
        elif decimals == 0:
            return math.ceil(number)

        factor = 10 ** decimals
        return math.ceil(number * factor) / factor


    def round_decimals_up_up(number: float, decimals: int = 1):
        if not isinstance(decimals, int):
            raise TypeError("decimal places must be an integer")
        elif decimals < 0:
            raise ValueError("decimal places needs to be 0 or more")
        elif decimals == 0:
            return math.ceil(number)

        factor = 1 ** decimals
        return math.ceil(number * factor) / factor

    for data_grup in nama_grup_dokumen:
        no += 1
        nama_dosen = list(df1['Nama Dosen'])

        grup_riset_1 = list(df1['Nama Dosen'].loc[(df1['Kecenderungan Grup Riset 1'] == data_grup)])
        presentase_grup_riset_1 = len(grup_riset_1)/len(nama_dosen)*100
        hasil_grup_riset_1 = round_decimals_up(presentase_grup_riset_1)
        hasil2_grup_riset_1 = round_decimals_up_up(presentase_grup_riset_1)

        grup_riset_2 = list(df1['Nama Dosen'].loc[(df1['Kecenderungan Grup Riset 2'] == data_grup)])
        presentase_grup_riset_2 = len(grup_riset_2)/len(nama_dosen)*100
        hasil_grup_riset_2 = round_decimals_up(presentase_grup_riset_2)
        hasil2_grup_riset_2 = round_decimals_up_up(presentase_grup_riset_2)

        writer.writerow([no, data_grup, len(grup_riset_1), hasil_grup_riset_1, int(hasil2_grup_riset_1), data_grup, len(grup_riset_2), hasil_grup_riset_2, int(hasil2_grup_riset_2)])

        print('Untuk Grafik Selesai')

print('proses hitung jumlah dosen berhasil dijalankan')