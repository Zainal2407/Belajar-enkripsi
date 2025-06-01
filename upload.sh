#!/bin/bash

# Tambahkan semua perubahan
git add .

# Commit dengan timestamp
git commit -m "Update otomatis pada $(date '+%Y-%m-%d %H:%M:%S')"

# Push ke GitHub
git push origin master
