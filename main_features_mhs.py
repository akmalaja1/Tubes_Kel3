import mysql.connector
from admin_db_info import get_current_mysql_password

# Koneksi ke database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=get_current_mysql_password(),
    database="ebookingclass"
)

def ajukan_kelas():
    cursor = conn.cursor()
    kode_kelas = input("Masukkan Kode Kelas yang ingin diajukan: ").strip()
    nim = input("Masukkan NIM Anda: ").strip()
    try:
        cursor.execute('''
        INSERT INTO pengajuan (nim, kode_kelas, tanggal_pengajuan, status_pengajuan)
        VALUES (%s, %s, NOW(), 'Berhasil')
        ''', (nim, kode_kelas))
        conn.commit()
        print("Pengajuan kelas berhasil!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()