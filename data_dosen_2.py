from bs4 import BeautifulSoup
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import requests
import csv
import re

import pandas as pd

headers_1 ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

df1 = pd.read_csv('id_dosen/id_dosen.csv', encoding='ISO-8859-1')

df3 = pd.read_csv('filter_2/filter.csv', encoding='ISO-8859-1')

filter_kata = list(df3['Kata'])

df4 = pd.read_csv('filter/filter.csv', encoding='ISO-8859-1')

filter_judul = list(df4['Kata'])

nama_dosen_dokumen = list(df1['Nama Dosen'])
link_dosen_dokumen = list(df1['Link'])

no_dosen_dokumen = 0

factory = StemmerFactory()
stemmer = factory.create_stemmer()

array_no = []
array_no_dosen = []
array_nama_dosen = []
array_judul = []
array_filter_kata = []

no_array_list_data = 0

nomor_judul = 1

with open('data/data_judul_dosen/data_judul_dosen.csv', 'w',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No Dosen', 'Nama Dosen', 'No Judul', 'Judul Jurnal', 'Kata Judul Jurnal Hasil Filter'])

df2 = pd.read_csv('data/data_judul_dosen/data_judul_dosen.csv', encoding='ISO-8859-1')

judul_terverifikasi = 0

mulai = 0

no_dosen = 0

if df2.empty:
    with open('data/data_judul_dosen/data_judul_dosen.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['No Dosen', 'Nama Dosen', 'No Judul', 'Judul Jurnal', 'Kata Judul Jurnal Hasil Filter'])


        while no_dosen_dokumen < len(nama_dosen_dokumen):
            # print(f'Nama Dosen: {nama_dosen_dokumen[no_dosen_dokumen]}')

            nomornya_dosen = list(df1['No Dosen'].loc[(df1['Nama Dosen'] == nama_dosen_dokumen[no_dosen_dokumen])])
            no_dosen = nomornya_dosen[0]

            mulai = 0
            while mulai <= 100:
                print(no_dosen_dokumen)
                url_2 = f'{link_dosen_dokumen[no_dosen_dokumen]}&cstart={mulai}&pagesize=100'

                print(link_dosen_dokumen[no_dosen_dokumen])

                print(url_2)

                response = requests.get(url_2, headers=headers_1)
                # print(response.status_code)

                print(response.status_code)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'lxml')
                    for td in soup.select('td.gsc_a_t'):
                        try:
                            # print('----------------------------------------')

                            judul_jurnal = td.select('a')[0].get_text()

                            judul = stemmer.stem(judul_jurnal)
                            judul = (re.sub('[():,.]', "", judul_jurnal))

                            judul = judul.replace('[PDF][PDF]', '')
                            judul = judul.replace('��', '')
                            judul = judul.replace('[PERNYATAAN][C]', '')
                            judul = judul.replace('[BUKU][B]', '')

                            # print(judul)

                            kata_dasar = stemmer.stem(judul)
                            judul_jurnal_split = kata_dasar.split()

                            cek_judul_jurnal_split = kata_dasar.split()

                            no_split = 0

                            no_split_cek = 0

                            while no_split_cek < len(cek_judul_jurnal_split):
                                if cek_judul_jurnal_split[no_split_cek] in filter_judul:
                                    judul_terverifikasi = 1
                                    while no_split < len(judul_jurnal_split):
                                        kata = judul_jurnal_split[no_split]

                                        panjang_data_kata = 1
                                        panjang_array_kata = len(filter_kata)

                                        s = dict()

                                        for i in range(panjang_array_kata):
                                            s[filter_kata[i]] = 1
                                        for i in range(panjang_data_kata):
                                            if kata not in s.keys():
                                                # print(kata)
                                                array_no_dosen.append(no_dosen)
                                                array_no.append(nomor_judul)
                                                array_nama_dosen.append(nama_dosen_dokumen[no_dosen_dokumen])
                                                array_judul.append(judul)
                                                array_filter_kata.append(kata)
                                        no_split += 1
                                        no_split_cek = 0
                                no_split_cek += 1

                            if judul_terverifikasi == 1:
                                nomor_judul += 1
                            judul_terverifikasi = 0

                        except Exception as e:
                            print('Data Pada Proses Crawling Tidak Dapat Ditemukan. Coba Lagi')
                            pass

                    while no_array_list_data < len(array_no):
                        writer.writerow([array_no_dosen[no_array_list_data], array_nama_dosen[no_array_list_data], array_no[no_array_list_data],
                                         array_judul[no_array_list_data], array_filter_kata[no_array_list_data]])
                        no_array_list_data += 1

                    no_array_list_data = 0

                    array_no_dosen = []
                    array_no = []
                    array_nama_dosen = []
                    array_judul = []
                    array_filter_kata = []
                else:
                    print('Data Tidak Dapat Dilakukan Proses Crawling. Coba Lagi')
                    no_dosen_dokumen = len(nama_dosen_dokumen)

                mulai += 100

            no_dosen_dokumen += 1

        print(
            'Proses Pengambilan Crawling Data Judul Publikasi Dosen Berhasil')

else:
    last_urutan_dosen = list(df2['Nama Dosen'].iloc[[-1]])
    index_urutan_dosen = nama_dosen_dokumen.index(last_urutan_dosen[0])

    no_dosen_dokumen = index_urutan_dosen + 1

    last_urutan_nomor = list(df2['No'].iloc[[-1]])
    nomor_judul = last_urutan_nomor[0] + 1

    with open('data/data_judul_dosen/data_judul_dosen.csv', 'a+', newline='') as file:
        writer = csv.writer(file)

        while no_dosen_dokumen < len(nama_dosen_dokumen):
            # print(f'Nama Dosen: {nama_dosen_dokumen[no_dosen_dokumen]}')
            mulai = 0
            while mulai <= 100:
                url_2 = f'{link_dosen_dokumen[no_dosen_dokumen]}&cstart={mulai}&pagesize=100'

                # print(url_2)

                response = requests.get(url_2, headers=headers_1)
                # print(response.status_code)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'lxml')
                    for td in soup.select('td.gsc_a_t'):
                        try:
                            # print('----------------------------------------')

                            judul_jurnal = td.select('a')[0].get_text()

                            judul = stemmer.stem(judul_jurnal)
                            judul = (re.sub('[():,.]', "", judul_jurnal))

                            judul = judul.replace('[PDF][PDF]', '')
                            judul = judul.replace('��', '')
                            judul = judul.replace('[PERNYATAAN][C]', '')
                            judul = judul.replace('[BUKU][B]', '')

                            # print(judul)

                            kata_dasar = stemmer.stem(judul)
                            judul_jurnal_split = kata_dasar.split()

                            cek_judul_jurnal_split = kata_dasar.split()

                            no_split = 0

                            no_split_cek = 0

                            while no_split_cek < len(cek_judul_jurnal_split):
                                if cek_judul_jurnal_split[no_split_cek] in filter_judul:
                                    judul_terverifikasi = 1
                                    while no_split < len(judul_jurnal_split):
                                        kata = judul_jurnal_split[no_split]

                                        panjang_data_kata = 1
                                        panjang_array_kata = len(filter_kata)

                                        s = dict()

                                        for i in range(panjang_array_kata):
                                            s[filter_kata[i]] = 1
                                        for i in range(panjang_data_kata):
                                            if kata not in s.keys():
                                                # print(kata)
                                                array_no.append(nomor_judul)
                                                array_nama_dosen.append(nama_dosen_dokumen[no_dosen_dokumen])
                                                array_judul.append(judul)
                                                array_filter_kata.append(kata)
                                        no_split += 1
                                        no_split_cek = 0
                                no_split_cek += 1

                            if judul_terverifikasi == 1:
                                nomor_judul += 1
                            judul_terverifikasi = 0

                        except Exception as e:
                            print('Data Pada Proses Crawling Tidak Dapat Ditemukan. Coba Lagi')
                            pass
                    while no_array_list_data < len(array_no):
                        writer.writerow([array_no[no_array_list_data], array_nama_dosen[no_array_list_data],
                                         array_judul[no_array_list_data], array_filter_kata[no_array_list_data]])
                        no_array_list_data += 1

                    no_array_list_data = 0

                    array_no = []
                    array_nama_dosen = []
                    array_judul = []
                    array_filter_kata = []

                else:
                    print('Data Tidak Dapat Dilakukan Proses Crawling. Coba Lagi')
                    no_dosen_dokumen = len(nama_dosen_dokumen)

                mulai += 100

            no_dosen_dokumen += 1

        print(
            'Proses Pengambilan Crawling Data Judul Publikasi Dosen Berhasil.')





