#!/usr/bin/python
import os
import shutil
from datetime import datetime

# Fungsi untuk mencetak log
def log(message):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")

# Fungsi untuk memvalidasi direktori sebelum penghapusan
def delete_cache(target):
    if os.path.exists(target):
        try:
            shutil.rmtree(target)
            log(f"Berhasil menghapus cache di: {target}")
        except Exception as e:
            log(f"Gagal menghapus cache di: {target} - {str(e)}")
    else:
        log(f"Direktori tidak ditemukan: {target}")

# Direktori yang akan dibersihkan
targets = [
    os.path.join(os.path.expanduser("~"), "storage/shared/Android/data/*/.cache/*"),
    os.path.join(os.path.expanduser("~"), "data/data/com.termux/files/home/*/.cache/*")
]

# Konfirmasi sebelum penghapusan
print("Script ini akan menghapus cache di direktori berikut:")
for target in targets:
    print(f" - {target}")

confirm = input("Apakah Anda yakin ingin melanjutkan? (y/n): ")
if confirm.lower() == "y":
    import glob
    for target in targets:
        for path in glob.glob(target):
            delete_cache(path)
    log("Pembersihan cache selesai.")
else:
    log("Pembersihan cache dibatalkan.")
