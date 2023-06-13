import pandas as pd
import csv

# Jumlah Bidang Muncul Dosen

with open(f'kecenderungan_bidang_dosen/jumlah_bidang_muncul_dosen.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Dosen', 'Nama Dosen', 'Nama Bidang', 'Jumlah Bidang Muncul'])

    df1 = pd.read_csv(f'hasil_naive_bayes_data_dosen/prediksi_5.csv', encoding='ISO-8859-1')

    nama_dosen = list(df1['Nama Dosen'])

    nama_dosen_dokumen = []

    for data_nama_dosen in nama_dosen:
        if data_nama_dosen not in nama_dosen_dokumen:
            nama_dosen_dokumen.append(data_nama_dosen)

    nomor_dosen = 0
    hitung_bidang = 0

    total_perbidang = 0

    grup_riset_hitung = []
    bidang_hitung = []

    for datanya_nama_dosen in nama_dosen_dokumen:
        nomor_dosen = list(df1['No Dosen'].loc[(df1['Nama Dosen'] == datanya_nama_dosen)])
        # print(datanya_nama_dosen)
        # print('')
        no = list(df1['No Judul'].loc[(df1['Nama Dosen'] == datanya_nama_dosen)])
        no_awal = no[0]
        no_akhir = no[len(no) - 1]
        no_hitung = no_awal
        while no_hitung <= no_akhir:
            grup_riset = list(df1['Grup Riset'].loc[(df1['No Judul'] == no_hitung)])
            bidang = list(df1['Nama Bidang'].loc[(df1['No Judul'] == no_hitung)])
            # print(grup_riset[0])
            # print(bidang[0])
            grup_riset_hitung.append(grup_riset[0])
            bidang_hitung.append(bidang[0])
            # print('------------------------')
            no_hitung += 1
        hitung_bidang = []
        for i in bidang_hitung:
            if i not in hitung_bidang:
                hitung_bidang.append(i)
        # print('')
        # print('total bidang penelitian yang muncul setiap dosen')
        for i in range(0, len(hitung_bidang)):
            # print(hitung_bidang[i])
            # print(bidang_hitung.count(hitung_bidang[i]))
            writer.writerow([nomor_dosen[0], datanya_nama_dosen, hitung_bidang[i], bidang_hitung.count(hitung_bidang[i])])
        bidang_hitung = []
        # print('')
        # print('')

# Jumlah Grup Riset Muncul

with open(f'kecenderungan_bidang_dosen/jumlah_grup_riset_muncul_dosen.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Dosen', 'Nama Dosen', 'Grup Riset', 'Jumlah Grup Riset Muncul'])

    df1 = pd.read_csv(f'hasil_naive_bayes_data_dosen/prediksi_5.csv', encoding='ISO-8859-1')

    nama_dosen = list(df1['Nama Dosen'])

    nama_dosen_dokumen = []

    for data_nama_dosen in nama_dosen:
        if data_nama_dosen not in nama_dosen_dokumen:
            nama_dosen_dokumen.append(data_nama_dosen)

    nomor_dosen = 0
    hitung_bidang = 0

    total_perbidang = 0

    grup_riset_hitung = []
    bidang_hitung = []

    for datanya_nama_dosen in nama_dosen_dokumen:
        nomor_dosen = list(df1['No Dosen'].loc[(df1['Nama Dosen'] == datanya_nama_dosen)])
        # print(datanya_nama_dosen)
        # print('')
        no = list(df1['No Judul'].loc[(df1['Nama Dosen'] == datanya_nama_dosen)])
        no_awal = no[0]
        no_akhir = no[len(no) - 1]
        no_hitung = no_awal
        while no_hitung <= no_akhir:
            grup_riset = list(df1['Grup Riset'].loc[(df1['No Judul'] == no_hitung)])
            bidang = list(df1['Nama Bidang'].loc[(df1['No Judul'] == no_hitung)])
            # print(grup_riset[0])
            # print(bidang[0])
            grup_riset_hitung.append(grup_riset[0])
            bidang_hitung.append(bidang[0])
            # print('------------------------')
            no_hitung += 1
        hitung_grup = []
        for i in grup_riset_hitung:
            if i not in hitung_grup:
                hitung_grup.append(i)
        # print('')
        # print('total grup riset yang muncul setiap dosen')
        for i in range(0, len(hitung_grup)):
            # print(hitung_grup[i])
            # print(grup_riset_hitung.count(hitung_grup[i]))
            writer.writerow([nomor_dosen[0], datanya_nama_dosen, hitung_grup[i], grup_riset_hitung.count(hitung_grup[i])])
        grup_riset_hitung = []
        # print('')
        # print('')

# Kecenderungan Bidang ## Butuh

with open(f'kecenderungan_bidang_dosen/kecenderungan_bidang_dosen.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Dosen', 'Nama Dosen', 'No Bidang', 'Kecenderungan Bidang', 'Jumlah Bidang Muncul', 'Persentase'])

    df1 = pd.read_csv(f'kecenderungan_bidang_dosen/jumlah_bidang_muncul_dosen.csv', encoding='ISO-8859-1')
    df2 = pd.read_csv(f'database/bidang_penelitian.csv', encoding='ISO-8859-1')
    df3 = pd.read_csv(f'hasil_naive_bayes_data_dosen/prediksi_5.csv', encoding='ISO-8859-1')

    nama_dosen = list(df1['Nama Dosen'])

    nama_dosen_dokumen = []

    for data in nama_dosen:
        if data not in nama_dosen_dokumen:
            nama_dosen_dokumen.append(data)

    nomor_dosen = 0

    no_bidang_tertinggi = 0

    bidang = []
    jumlah_bidang_muncul = []

    for data_dosen in nama_dosen_dokumen:
        # print(data_dosen)
        # print('')
        jumlah_publikasi = list(df3['No Judul'].loc[(df3['Nama Dosen'] == data_dosen)])
        nomor_dosen = list(df1['No Dosen'].loc[(df1['Nama Dosen'] == data_dosen)])
        no_awal = nomor_dosen[0]
        no_akhir = nomor_dosen[len(nomor_dosen) - 1]
        no_hitung = no_awal
        while no_hitung <= no_akhir:
            bidang = list(df1['Nama Bidang'].loc[(df1['No Dosen'] == no_hitung)])
            jumlah_bidang_muncul = list(df1['Jumlah Bidang Muncul'].loc[(df1['No Dosen'] == no_hitung)])
            no_hitung += 1
        for data_jumlah_bidang in jumlah_bidang_muncul:
            if no_bidang_tertinggi < data_jumlah_bidang:
                no_bidang_tertinggi = data_jumlah_bidang
        # print(f'No Bidang Tertinggi: {no_bidang_tertinggi}')
        index_kecenderungan_bidang = jumlah_bidang_muncul.index(no_bidang_tertinggi)
        kecenderungan_bidang = bidang[index_kecenderungan_bidang]
        no_kecenderungan_bidang = list(df2['No Bidang'].loc[(df2['Bidang Penelitian'] == kecenderungan_bidang)])
        # print(f'Kecenderungan Bidang: {kecenderungan_bidang}')
        persentase = (no_bidang_tertinggi / len(jumlah_publikasi)) * 100
        writer.writerow([nomor_dosen[0], data_dosen, no_kecenderungan_bidang[0], kecenderungan_bidang, no_bidang_tertinggi, int(persentase)])
        no_bidang_tertinggi = 0
        # print('')

# Kecenderungan Grup Riset ## Butuh

with open(f'kecenderungan_bidang_dosen/daftar_kecenderungan_grup_riset_dosen.csv', 'w', newline='', encoding='ISO-8859-1') as file:
    writer = csv.writer(file)
    writer.writerow(['No Dosen', 'Nama Dosen', "No Grup Riset 1", 'Kecenderungan Grup Riset 1', "Jumlah Grup Riset 1", "Persentase Grup Riset 1", "No Grup Riset 2", 'Kecenderungan Grup Riset 2', "Jumlah Grup Riset 2", "Persentase Grup Riset 2", 'Deleted'])

    df1 = pd.read_csv(f'kecenderungan_bidang_dosen/jumlah_grup_riset_muncul_dosen.csv', encoding='ISO-8859-1')
    df2 = pd.read_csv(f'database/grup_riset.csv', encoding='ISO-8859-1')
    df3 = pd.read_csv(f'hasil_naive_bayes_data_dosen/prediksi_5.csv', encoding='ISO-8859-1')

    nama_dosen = list(df1['Nama Dosen'])

    nama_dosen_dokumen = []

    for data in nama_dosen:
        if data not in nama_dosen_dokumen:
            nama_dosen_dokumen.append(data)

    nomor_dosen = 0

    no_grup_tertinggi_1 = 0
    no_grup_tertinggi_2 = 0

    grup = []
    jumlah_grup_muncul = []

    deleted = 0

    perulangan = 2
    no_perulangan = 1

    for data_dosen in nama_dosen_dokumen:
        jumlah_publikasi = list(df3['No Judul'].loc[(df3['Nama Dosen'] == data_dosen)])
        nomor_dosen = list(df1['No Dosen'].loc[(df1['Nama Dosen'] == data_dosen)])
        # print(data_dosen)
        # print('')
        no = list(df1['No Dosen'].loc[(df1['Nama Dosen'] == data_dosen)])
        no_awal = no[0]
        no_akhir = no[len(no) - 1]
        no_hitung = no_awal
        while no_hitung <= no_akhir:
            grup = list(df1['Grup Riset'].loc[(df1['No Dosen'] == no_hitung)])
            jumlah_grup_muncul = list(df1['Jumlah Grup Riset Muncul'].loc[(df1['No Dosen'] == no_hitung)])
            no_hitung += 1
            for data_jumlah_grup in jumlah_grup_muncul:
                if no_grup_tertinggi_1 < data_jumlah_grup:
                    no_grup_tertinggi_1 = data_jumlah_grup
            # print(f'No Grup Tertinggi: {no_grup_tertinggi_1}')
            index_kecenderungan_grup_1 = jumlah_grup_muncul.index(no_grup_tertinggi_1)
            kecenderungan_grup_1 = grup[index_kecenderungan_grup_1]
            no_kecenderungan_grup_1 = list(df2['No Grup Riset'].loc[(df2['Nama Grup Riset'] == kecenderungan_grup_1)])
            # print(f'Kecenderungan Grup: {kecenderungan_grup_1}')
            persentase_grup_1 = (no_grup_tertinggi_1 / len(jumlah_publikasi)) * 100

            if len(jumlah_grup_muncul) > 1:
                mx = max(jumlah_grup_muncul[0], jumlah_grup_muncul[1])
                secondmax = min(jumlah_grup_muncul[0], jumlah_grup_muncul[1])
                n = len(jumlah_grup_muncul)
                for i in range(2, n):
                    if jumlah_grup_muncul[i] > mx:
                        secondmax = mx
                        mx = jumlah_grup_muncul[i]
                    elif jumlah_grup_muncul[i] > secondmax and \
                            mx != jumlah_grup_muncul[i]:
                        secondmax = jumlah_grup_muncul[i]
            else:
                secondmax = jumlah_grup_muncul[0]
            index_kecenderungan_grup_2 = jumlah_grup_muncul.index(secondmax)
            kecenderungan_grup_2 = grup[index_kecenderungan_grup_2]
            no_kecenderungan_grup_2 = list(df2['No Grup Riset'].loc[(df2['Nama Grup Riset'] == kecenderungan_grup_2)])
            # print(kecenderungan_grup_2)
            # print('')
            persentase_grup_2 = (secondmax / len(jumlah_publikasi)) * 100
            # print('')
            writer.writerow([nomor_dosen[0], data_dosen, no_kecenderungan_grup_1[0], kecenderungan_grup_1, no_grup_tertinggi_1, int(persentase_grup_1), no_kecenderungan_grup_2[0], kecenderungan_grup_2, secondmax, int(persentase_grup_2), deleted])
            no_grup_tertinggi_1 = 0

print('Proses Penentuan Kecenderungan Bidang Dosen berhasil dijalankan.')