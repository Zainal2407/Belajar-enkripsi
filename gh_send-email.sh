#!/data/data/com.termux/files/usr/bin/bash

# Buat issue di GitHub
gh issue create --title "Pesan dari Termux" --body "Pemberitahuan login jika ini anda masukkan kode autentiknya"

# Autentikasi gh dan meminta kode otorisasi
gh auth login
