import mysql.connector

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="ebookingclass"
)
cursor = conn.cursor()

# Fungsi untuk membuat tabel
def create_tables():
    # Tabel users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(20) NOT NULL,
        user_role ENUM('admin','mahasiswa') NOT NULL
    )''')

    # Tabel mahasiswa
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mahasiswa (
        nim INT(7) NOT NULL PRIMARY KEY,
        nama VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        alamat TEXT NOT NULL,
        no_tlp VARCHAR(20) NOT NULL
    )''')

    # Tabel dosen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dosen (
        nip INT(20) NOT NULL PRIMARY KEY,
        nama VARCHAR(255) NOT NULL,
        alamat TEXT NOT NULL,
        email VARCHAR(255) NOT NULL,
        no_tlp VARCHAR(20) NOT NULL
    )''')

    # Tabel jadwal_dosen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jadwal_dosen (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nip INT(20) NOT NULL,
        hari ENUM('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu') NOT NULL,
        jam_mulai TIME NOT NULL,
        jam_selesai TIME NOT NULL,
        FOREIGN KEY (nip) REFERENCES dosen(nip)
    )''')

    # Tabel mata_kuliah
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mata_kuliah (
        kode_matkul VARCHAR(10) PRIMARY KEY,
        nama_matkul VARCHAR(255) NOT NULL
    )''')

    # Tabel kelas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kelas (
        kode_kelas VARCHAR(30) PRIMARY KEY,
        informasi_kelas TEXT NOT NULL
    )''')

    # Tabel detail_kelas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS detail_kelas (
        id_detail_kelas INT AUTO_INCREMENT PRIMARY KEY,
        kode_kelas VARCHAR(30),
        kode_matkul VARCHAR(10),
        waktu_penggunaan DATETIME NOT NULL,
        nip_dosen INT (20) NOT NULL,
        informasi_kelas TEXT NOT NULL,
        status ENUM('Tersedia','Tidak Tersedia') NOT NULL,
        FOREIGN KEY (kode_matkul) REFERENCES mata_kuliah(kode_matkul),
        FOREIGN KEY (nip_dosen) REFERENCES dosen(nip),
        FOREIGN KEY (kode_kelas) REFERENCES kelas(kode_kelas)
    )''')

    # Tabel pengajuan
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pengajuan (
        id_pengajuan INT AUTO_INCREMENT PRIMARY KEY,
        nim INT(7) NOT NULL,
        kode_kelas VARCHAR(30) NOT NULL,
        tanggal_pengajuan DATETIME NOT NULL,
        status_pengajuan ENUM('Berhasil','Gagal') NOT NULL,
        FOREIGN KEY (nim) REFERENCES mahasiswa(nim),
        FOREIGN KEY (kode_kelas) REFERENCES kelas(kode_kelas)
    )''')

    print("Tabel-tabel berhasil dibuat.")

# Eksekusi pembuatan tabel
create_tables()

# Tutup koneksi
conn.close()