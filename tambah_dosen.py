import pandas as pd
import csv
import sys

with open('../../Program_Klasifikasi/data_dosen_sistem/id_dosen/id_dosen.csv', 'a+',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow([sys.argv[1], sys.argv[2]])

    print('Proses tambahkan dosen berhasil dijalankan')