import mysql.connector
from admin_db_info import get_current_mysql_password

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=get_current_mysql_password(),
    database="ebookingclass"
)
cursor = conn.cursor()

def valid_email(email):
    return email.endswith('@gmail.com')

def register_user():
    print("\n=== Register ===")
    username = input("Masukkan Nama: ").strip()
    email = input("Masukkan Email: ").strip()
    password = input("Masukkan Password: ").strip()
    role = "mahasiswa" 

    # if role not in ['admin', 'mahasiswa']:
    #     print("Role tidak valid. Silakan gunakan 'admin' atau 'mahasiswa'.")
    #     return

    try:
        cursor.execute('''
        INSERT INTO users (username, email, password, user_role)
        VALUES (%s, %s, %s, %s)
        ''', (username, email, password, role))
        conn.commit()
        print("Registrasi berhasil!")
    except mysql.connector.IntegrityError:
        print("Email sudah digunakan!")
    finally:
        cursor.close()
        conn.close()