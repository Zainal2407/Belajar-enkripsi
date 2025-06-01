#!/bin/bash

# Fungsi untuk mencetak log
log() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Fungsi untuk memvalidasi direktori sebelum penghapusan
delete_cache() {
  if [ -d "$1" ]; then
    rm -rf "$1"
    log "Berhasil menghapus cache di: $1"
  else
    log "Direktori tidak ditemukan: $1"
  fi
}

# Direktori yang akan dibersihkan
TARGETS=(
  "$HOME/storage/shared/Android/data/*/.cache/*"
  "$HOME/.cache/*"
)

# Konfirmasi sebelum penghapusan
echo "Script ini akan menghapus cache di direktori berikut:"
for TARGET in "${TARGETS[@]}"; do
  echo " - $TARGET"
done

read -p "Apakah Anda yakin ingin melanjutkan? (y/n): " CONFIRM

if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
  for TARGET in "${TARGETS[@]}"; do
    delete_cache "$TARGET"
  done
  log "Pembersihan cache selesai."
else
  log "Pembersihan cache dibatalkan."
fi
