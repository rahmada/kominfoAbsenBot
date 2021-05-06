from datetime import datetime
from webbot import Browser
import time
import random

waktuawal="06:00:00"
waktuakhir="15:00:00"
alarm1=waktuawal
alarm2=waktuakhir
randomTime="00:22:00"
username = "riko001"
password = "myAkbar221018!"

def randomize():
    global alarm1
    global alarm2
    addMinute=random.randint(10,59)
    arrayTime=alarm1.split(":")
    addMinute=addMinute+int(arrayTime[1])
    arrayTime[1]=str(addMinute)
    alarm1 = ":".join(arrayTime)
    addMinute=random.randint(10,59)
    arrayTime=alarm2.split(":")
    addMinute=addMinute+int(arrayTime[1])
    arrayTime[1]=str(addMinute)
    alarm2 = ":".join(arrayTime)



def absenIn():
    print(" ")
    print("Checking In...")
    rambah = Browser()
    rambah.go_to("https://portal.kominfo.go.id")
    rambah.type(username,into='Username', id="LoginForm_username")
    rambah.type(password,into='Password', id="LoginForm_password")
    rambah.click(text='LOGIN')
    time.sleep(5)
    rambah.go_to("https://portal.kominfo.go.id/site/mypreauth/id/apik")
    judul = rambah.get_title()
    print(judul[0:7]+" Ini Judul")
    while (judul[0:7]!="Absensi"):
        print("Judul nggak cocok!)")
        rambah.go_to("https://portal.kominfo.go.id/site/mypreauth/id/apik")
        time.sleep(5)
        judul = rambah.get_title()
    rambah.click(text='CHECK-IN')
    rambah.click(text='OK')
    rambah.click(text='Kantor')
    rambah.click(text='Sesuai')
    print("Checking in success..")
    rambah.quit()

def absenOut():
    print(" ")
    print("Checking Out...")
    rambah = Browser()
    rambah.go_to("https://portal.kominfo.go.id")
    rambah.type(username,into='Username', id="LoginForm_username")
    rambah.type(password,into='Password', id="LoginForm_password")
    rambah.click(text='LOGIN')
    time.sleep(5)
    rambah.go_to("https://portal.kominfo.go.id/site/mypreauth/id/apik")
    judul = rambah.get_title()
    print(judul[0:7]+" Ini Judul")
    while (judul[0:7]!="Absensi"):
        print("Judul nggak cocok!)")
        rambah.go_to("https://portal.kominfo.go.id/site/mypreauth/id/apik")
        time.sleep(5)
        judul = rambah.get_title()
    rambah.click(text='CHECK-OUT')
    rambah.click(text='OK')
    rambah.click(text='Sesuai')
    print("Checking out success...")
    rambah.quit()

#absenIn()

#randomize();
#print(alarm1)
#print(alarm2)

while True:
    sekarang = datetime.now()
    jam = sekarang.strftime("%H")
    menit = sekarang.strftime("%M")
    detik = sekarang.strftime("%S")
    waktu = jam+":"+menit+":"+detik
    alarmNote=""
    if (waktu==alarm1):
        absenIn()
    elif (waktu==alarm2):
        absenOut()
    elif(waktu==randomTime):
        alarm1=waktuawal
        alarm2=waktuakhir
        randomize()
        print("Randomizing Time...")
        print("waktu In : " +alarm1)
        print("waktu out : "+alarm2)
        print("   ")
    else:
        #print('waktu saat ini ',waktu,alarmNote,end='\r')
        print('waktu saat ini ',waktu,alarmNote)
    time.sleep(1)
