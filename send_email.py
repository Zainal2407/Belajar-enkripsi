import smtplib

sender = 'muhammadfauzi190291@gmail.com'
receiver = 'muhammadzainal240787@gmail.com'
password = 'L!n9kuku0k'
subject = 'Notifikasi Git Commit'
body = 'Ada commit baru di repository!'

message = f"Subject: {subject}\n\n{body}"

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
