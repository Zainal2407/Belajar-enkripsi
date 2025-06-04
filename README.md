*Halo, Dunia!*
*Ini adalah proyek demo untuk mempelajari cara menggunakan Git.*

*Berikut adalah susunan direktori `Cabang master`:*
```
📁$HOME/                     # Home Termux
├──📄 .bashrc
├──📄 .gitconfig
├──📄 .ssh/
├──📄 .config/
├──📄 .termux/
├──📄 backup_HOME.sh
├──📄 cleaning_cache.py
├──📄 cek_device_id.sh
│──📂 storage/               # Home Storage (cabang master)
│   ├──📜 README.md
│   ├──📜 LICENSE
│   ├──🔒 SECURITY.md
│   ├──📄 api_key.py
│   ├──📄 Auth_config/
│   ├──📄 cli/
│   ├──📄 cleaning_cache.sh
│   ├──📄 downloads/
│   ├──📄 music/
│   ├──📄 movies/
│   ├──📄 pictures/
│   ├──📄 send_email.py
│   ├──📄 upload.sh
│   ├──📄 .bashrc
│   ├──📄 .gitignore
│   └──📂 Belajar-enkripsi/
│       ├──📂 .git/
│       ├──📜 README.md
│       ├──📜 LICENSE
│       ├──🔒 SECURITY.md
│       ├──📄 .gitignore
│       ├──📂 proyek/
├             ├──📂 config/
├             ├──📄 auth_config_test.go
│             ├──📄 config_test.go
│             ├──📄 migration/
│             ├──📄 config.go
│             ├──📄 migrate_test.go
│             └──📄 stub.go
│             ├──📂 go/               
│                └──📂 pkg/  
│                   └──📂 mod/
│                      ├──📂 cache/
├                      ├──📂 github.com/
│                      ├──📂 golang.org/
│                      └──📂 gopkg.in/
│ 
│

```

*Dan berikut adalah isi `README.md`:*

*Direktori Cabang master*

*Deskripsi*
Direktori `Cabang storage` ini digunakan sebagai pusat penyimpanan kode dan konfigurasi untuk proyek Belajar-enkripsi.

*Struktur Direktori*
- `cli`: Direktori untuk kode CLI
- `config`: Direktori untuk konfigurasi
- `storage`: Direktori untuk penyimpanan data

*File-file Penting*
- `api_key.py`: Kode untuk mengakses API key
- `auth_config.py`: Konfigurasi autentikasi
- `device_id.txt`: File untuk menyimpan ID perangkat

# Direktori dan Panduan Penggunaan

## Struktur Direktori

1. **Home Termux** (`$HOME`)
    - Menyimpan file konfigurasi utama dan script Termux.
    - Contoh: `.bashrc`, `.gitconfig`, `backup_HOME.sh`, `storage/`, dll.

2. **Home Storage** (`$HOME/storage`) — _cabang master_
    - Pusat penyimpanan kode, data, dan project.
    - Contoh: `README.md`, `LICENSE`, `cli/`, `Belajar-enkripsi/`, dll.

3. **Project: Belajar-enkripsi** (`$HOME/storage/Belajar-enkripsi`) — _cabang main_
    - Folder project dengan repo dan subfolder pengembangan.
    - Contoh: `proyek/`, `.git/`, `README.md`, dll.

---

## Cara Backup & Clone

### Backup Home Termux
```sh
bash ~/backup_HOME.sh

Clone Project via GitHub
cd ~/storage
git clone <url-repo-ini>
# atau untuk subproject:
cd ~/storage/Belajar-enkripsi
git clone git@github.com:Zainal2407/Belajar-enkripsi.git

*Catatan*
- Simpan file backup di luar folder utama home untuk menghindari backup berulang & pemborosan storage.
- Gunakan .gitignore untuk mengecualikan file sensitif atau besar.
- Untuk restore, cukup extract/clone repositori sesuai kebutuhan.

---
Silakan copas dan edit sesuai kebutuhanmu! Jika mau versi lebih singkat atau ingin tambahkan bagian lain, tinggal bilang 👍
