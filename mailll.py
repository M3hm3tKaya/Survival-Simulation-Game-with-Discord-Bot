import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import random
sayi = random.randint(1,999999)
sayi = str(sayi)

if len(sayi) == 1:
    sayi = f"00000{sayi}"
if len(sayi) == 2:
    sayi = f"0000{sayi}"
if len(sayi) == 3:
    sayi = f"000{sayi}"
if len(sayi) == 4:
    sayi = f"00{sayi}"
if len(sayi) == 5:
    sayi = f"0{sayi}"

mesaj=MIMEMultipart()
mesaj['from']="SENDER MAIL"
mesaj['to']="TO WHO MAIL"
mesaj['subject']=sayi

yazi="kodsu canım : " + sayi

mesaj_yapisi=MIMEText(yazi,'plain')
mesaj.attach(mesaj_yapisi)
try:
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login('SENDER MAIL','PASSWORD')
    mail.sendmail(mesaj['from'],mesaj['to'],mesaj.as_string())
    print ('Mail gönderildi')
    mail.close()
except:
    print('hata oluştu')

count = 3
while count > 0:
    auth = input("Doğrulama Kodunuzu Girin : ")

    if auth == sayi:
        print("DOĞRULANDI")
        break
    else:
        count -=1
        print(f"Yanlış KOD\nKalan Deneme Hakkın : {count}")
        continue
if count ==0:
    print("HAK KALMADI.")
















