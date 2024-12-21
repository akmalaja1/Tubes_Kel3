import mysql.connector
import time
from admin_db_info import get_current_mysql_password
import bcrypt
import unicodedata

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=get_current_mysql_password(),
    database="ebookingclass"
)
cursor = conn.cursor()

def login():
    from main_menu import admin_menu, mahasiswa_menu

    attempts = 0  # Hitungan percobaan login

    while attempts < 3:  # Memberikan 3 kali kesempatan login
        print("\n=== Login ===")
        nim = input("Masukkan NIM: ").lower()
        password = input("Masukkan Password: ")
        password = unicodedata.normalize("NFKC", password).strip()

        # Check Email
        cursor.execute(f"SELECT password FROM users WHERE nim = \"{nim}\"")
        password_result = cursor.fetchone()

        # Jika email tidak valid, maka password tidak ada
        if (password_result == None):
            print("Login gagal! Email atau password salah.")
            attempts += 1
            if attempts < 3:
                print(f"Sisa percobaan login: {3 - attempts}")
            else:
                print("Terlalu banyak percobaan gagal. Program akan pending selama 30 detik.")
                time.sleep(30)  # Menunggu selama 30 detik setelah 3 kali gagal
        
        # Jika email valid, password ada
        else:
            hashed_password = password_result[0]
            
            # login berhasil jika password = hashed password
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")):
                cursor.execute(f"SELECT user_role FROM users WHERE nim = \"{nim}\"")
                role = cursor.fetchone()
                print(f"current role: {role[0]}")
                print(f"Login berhasil sebagai {role[0]}!")
                if role[0] == 'admin':
                    admin_menu()
                elif role[0] == 'mahasiswa':
                    mahasiswa_menu()
                break  # Keluar dari loop karena login berhasil
            
            # gagal jika password =/= hashed password
            else:
                print("Login gagal! NIM atau password salah.")
                attempts += 1  # Increment percobaan login
                if attempts < 3:
                    print(f"Sisa percobaan login: {3 - attempts}")
                else:
                    print("Terlalu banyak percobaan gagal. Program akan pending selama 30 detik.")
                    time.sleep(30)  # Menunggu selama 30 detik setelah 3 kali gagal

    cursor.close()
    conn.close()
