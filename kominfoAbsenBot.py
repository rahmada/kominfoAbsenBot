import random
import datetime as dt
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def rnd_minute(waktu):
    date_awal = dt.datetime.combine(dt.datetime.today(),waktu)
    return date_awal + dt.timedelta(minutes=random.randint(1,59))

def absenIn(username,password):
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.set_page_load_timeout(10)
    #portal login
    portal_login(driver,username,password)
    time.sleep(1)
    
    #insert check health here
    try:
        driver.get("https://apik.kominfo.go.id/index.php/screeningCovid")
        time.sleep(1)
        driver.find_element_by_id("ScreeningCovid_answer_1_0").click()
        time.sleep(1)
        driver.find_element_by_id("ScreeningCovid_answer_2_0").click()
        time.sleep(1)
        driver.find_element_by_id("ScreeningCovid_answer_3_0").click()
        time.sleep(1)
        driver.find_element_by_name("yt0").click()
        time.sleep(1)
    except:
        print("Cek Kesehatan Gagal")
    
    #insert check in here
    driver.get("https://portal.kominfo.go.id/site/mypreauth/id/apik")
    time.sleep(1)
    try:
        driver.find_element_by_id("checkin").click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="OK"]').click()
        time.sleep(1)
        driver.find_element_by_name("swal2-radio").click()
        time.sleep(1)
        print ("Check-in Sukses")
    except:
        print("Elemen/button tidak ditemukan!")
    
    driver.close()
    
def absenOut(username,password):
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.set_page_load_timeout(10)
    
    #portal login
    portal_login(driver,username,password)

    #insert check out here
    time.sleep(1)
    try:
        driver.find_element_by_id("checkout").click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="OK"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="Sesuai"]').click()
        time.sleep(1)
    except:
        print("Elemen/button tidak ditemukan!")
        
    driver.close()

def portal_login(ddriver,uusername,ppassword):
    ddriver.get("https://portal.kominfo.go.id")
    user_form = ddriver.find_element_by_id("LoginForm_username")
    user_form.clear()
    user_form.send_keys(uusername)
    user_form = ddriver.find_element_by_id("LoginForm_password")
    user_form.clear()
    user_form.send_keys(ppassword)
    user_form.send_keys(Keys.ENTER) 
    time.sleep(1)
    ddriver.get("https://portal.kominfo.go.id/site/mypreauth/id/apik")
    time.sleep(1)
    
    #insert check title here
    while (ddriver.title!="Absensi Elektronik KOMINFO - Site"):
        print("Judul nggak cocok, refresh...")
        driver.get("https://portal.kominfo.go.id/site/mypreauth/id/apik")
    print("Judul cocok.. lanjut proses..")

#time_variable
wkt_datang = dt.time(6,0,0)
wkt_pulang = dt.time(16,35,0)
wkt_chday = dt.time(1,0,0)
date_datang = dt.datetime.combine(dt.datetime.today(),wkt_datang)
date_pulang = dt.datetime.combine(dt.datetime.today(),wkt_pulang)
date_chday = dt.datetime.combine(dt.datetime.today(),wkt_chday)

#username password
user = "riko001"
passwd = "myAkbar221018!"

#randomize pulang & datang
date_datang=rnd_minute(wkt_datang)
date_pulang=rnd_minute(wkt_pulang)
print("Tanggal : ", dt.datetime.today().strftime("%d/%m/%y")," Datang : ", date_datang.strftime("%H:%M:%S")," Pulang : ", date_pulang.strftime("%H:%M:%S") )

while True:
    date_skrg = dt.datetime.today()    
   
    #print every seconds
    print(date_skrg.strftime("%H:%M:%S"),end='\r')
    time.sleep(1)
    
    #if its hit waktu datang & waktu pulang & ganti hari
    if (date_skrg.strftime("%H:%M:%S") == date_datang.strftime("%H:%M:%S")) : #waktu datang
        print("Waktu Absen Masuk!")
        absenIn(user,passwd)
    elif (date_skrg.strftime("%H:%M:%S") == date_pulang.strftime("%H:%M:%S")) : #waktu pulang
        print("Waktu Absen Pulang!")
    elif (date_skrg.strftime("%H:%M:%S") == date_chday.strftime("%H:%M:%S")) : #ganti hari, randomize waktu masuk dan pulang
        print("Tengah malam, randomizing new time")
        date_datang=rnd_minute(wkt_datang)
        date_pulang=rnd_minute(wkt_pulang)
        print("Tanggal : ", dt.datetime.today().strftime("%d/%m/%y")," Datang : ", date_datang.strftime("%H:%M:%S")," Pulang : ", date_pulang.strftime("%H:%M:%S") )
    