import mysql.connector
from main_features import add_mata_kuliah, view_dosen, view_kelas, ajukan_kelas, input_jadwal_dosen, buat_kelas, edit_jadwal_dosen, view_jadwal_dosen, tampilkan_kelas
from register import register_user
from login import login

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="ebookingclass"
)
cursor = conn.cursor()

# Menu untuk admin
def admin_menu():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Mata Kuliah")
        print("2. Lihat Data Dosen")
        print("3. Input Jadwal Kosong Dosen")
        print("4. Lihat Jadwal Kosong Seluruh Dosen")
        print("5. Edit Jadwal Kosong Dosen")
        print("6. Buat Kelas")
        print("7. Kelas dibuat")
        print("8. Data Ruang Kelas")
        print("9. Logout")
        
        choice = input("Pilih menu: ").strip()

        if choice == '1':
            add_mata_kuliah()
        elif choice == '2':
            view_dosen()
        elif choice == '3':
            input_jadwal_dosen()
        elif choice == '4':
            view_jadwal_dosen()
        elif choice == '5':
            edit_jadwal_dosen()
        elif choice == '6':
            buat_kelas()
        elif choice == "7":
            tampilkan_kelas()
        elif choice == '8':
            view_kelas()
        elif choice == '9':
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid! Pilih sesuai menu di atas!")

# Menu untuk mahasiswa
def mahasiswa_menu():
    while True:
        print("\n=== Menu Mahasiswa ===")
        print("1. Lihat Kelas")
        print("2. Ajukan Kelas")
        print("3. Lihat Profil (maintenance)")
        print("4. Logout")
        
        choice = input("Pilih menu: ").strip()

        if choice == '1':
            view_kelas()
        elif choice == '2':
            ajukan_kelas()
        # elif choice == '3':
        #     profile_menu()  # Bila ada menu profil
        elif choice == '4':
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")

# Main program
def main():
    while True:
        print("\n=== Sistem E-Booking Class ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        
        choice = input("Pilih menu: ").strip()

        if choice == '1':
            user_role = login()
            if user_role == 'admin':
                admin_menu()  # Arahkan ke menu admin setelah login admin
            elif user_role == 'mahasiswa':
                mahasiswa_menu()  # Arahkan ke menu mahasiswa setelah login mahasiswa
            else:
                print("Role tidak ditemukan!")
        elif choice == '2':
            register_user()
        elif choice == '3':
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program utama
main()

# Tutup koneksi
cursor.close()
conn.close()
