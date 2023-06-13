import mysql.connector
import csv

with open('database/dosen.csv', 'w',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No Dosen', 'Nama Dosen', 'Link'])

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="database_skripsi_backup"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT ID_DOSEN, NAMA_DOSEN, LINK_SCHOLAR FROM dosen")

    myresult = mycursor.fetchall()

    for x in myresult:
      writer.writerow([list(x)[0], list(x)[1], list(x)[2]])

with open('id_dosen/id_dosen.csv', 'w',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No Dosen', 'Nama Dosen', 'Link'])

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="database_skripsi_backup"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT ID_DOSEN, NAMA_DOSEN, LINK_SCHOLAR FROM dosen WHERE LINK_SCHOLAR != '-'")

    myresult = mycursor.fetchall()

    for x in myresult:
      writer.writerow([list(x)[0], list(x)[1], list(x)[2]])

with open('database/bidang_penelitian.csv', 'w',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No Bidang', 'No Grup Riset', 'Bidang Penelitian'])

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="database_skripsi_backup"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT ID_BIDANG_PENELITIAN, ID_GROUP_RISET, BIDANG_PENELITIAN FROM bidang_penelitian")

    myresult = mycursor.fetchall()

    for x in myresult:
      writer.writerow([list(x)[0], list(x)[1], list(x)[2]])

with open('database/grup_riset.csv', 'w',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No Grup Riset', 'Nama Grup Riset'])

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="database_skripsi_backup"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT ID_GROUP_RISET, GROUP_RISET FROM group_riset")

    myresult = mycursor.fetchall()

    for x in myresult:
      writer.writerow([list(x)[0], list(x)[1]])

with open('database/grup_riset_dosen.csv', 'w',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No Grup Riset Dosen', 'No Dosen', 'No Grup Riset 1', 'No Grup Riset 2'])

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="database_skripsi_backup"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT ID_GROUP_RISET_DOSEN, ID_DOSEN, ID_GROUP_RISET_1, ID_GROUP_RISET_2 FROM group_riset_dosen")

    myresult = mycursor.fetchall()

    for x in myresult:
      writer.writerow([list(x)[0], list(x)[1], list(x)[2], list(x)[3]])

print('Proses Pengambilan Data Dari Database Berhasil.')


      


