import mysql.connector
import time

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="ebookingclass"
)
cursor = conn.cursor()

def login():
    from main_menu import admin_menu, mahasiswa_menu

    attempts = 0  # Hitungan percobaan login

    while attempts < 3:  # Memberikan 3 kali kesempatan login
        print("\n=== Login ===")
        email = input("Masukkan Email: ").strip()
        password = input("Masukkan Password: ").strip()

        cursor.execute("SELECT user_role FROM users WHERE email = %s AND password = %s", (email, password))
        result = cursor.fetchone()

        if result:
            role = result[0]
            print(f"Login berhasil sebagai {role}!")
            if role == 'admin':
                admin_menu()
            elif role == 'mahasiswa':
                mahasiswa_menu()
            break  # Keluar dari loop karena login berhasil
        else:
            print("Login gagal! Email atau password salah.")
            attempts += 1  # Increment percobaan login
            if attempts < 3:
                print(f"Sisa percobaan login: {3 - attempts}")
            else:
                print("Terlalu banyak percobaan gagal. Program akan pending selama 30 detik.")
                time.sleep(30)  # Menunggu selama 30 detik setelah 3 kali gagal

    cursor.close()
    conn.close()

# Menjalankan fungsi login
login()
