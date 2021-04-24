"""
24.04.2021
Udemy ileri seviye python kursu class ödevi
Plazm4
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------0

import time
import random

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------1

class pc ():

    def __init__(self,pc_durum = "Kapalı",pc_ekran_par = 5,pc_ses = 50):

        self.pc_durum = pc_durum
        self.pc_ekran_par = pc_ekran_par
        self.pc_ses = pc_ses

    def pc_aç (self):

        if self.pc_durum == "Açık":
            print("\nBilgisayar zaten açık!")

        else:
            self.pc_durum = "Açık"
            print("\nBilgisayar Açıldı...")

    def pc_kapat(self):

        if self.pc_durum == "Kapalı":
            print("\nBilgisayar zaten kapalı!")

        else:
            print("\nBilgisayar kapatılıyor...")
            self.pc_surum = "Kapalı"

    def sistem_ses (self):

        print("""
            Sesi yükseltmek için '+' tuşlayın
            Sesi kısmak için '-' tuşlayın
            Çıkış için 'e' tuşlayın
            """)

        while True:

            ses_işlem = input("Yapmak istediğiniz ses ayarını giriniz: ")

            if ses_işlem == "+":
                if self.pc_ses != 100:
                    self.pc_ses +=10
                    print("Yeni ses: ",self.pc_ses)
                else:
                    print("Maksimum ses 100'dür!")

            elif ses_işlem == "-":
                if self.pc_ses != 0:
                    self.pc_ses -=10
                    print("Yeni ses: ",self.pc_ses)
                else:
                    print("Minumum ses 0'dır!")

            elif ses_işlem == "e" or ses_işlem == "E":
                print("Çıkış yapılıyor...Son ses: ",self.pc_ses,"\n")
                break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------2

def hesap_makinesi():

    def asal(sayı):
        for i in range(2,sayı):
            if sayı % i == 0  :
                return sayı, "sayısı asal değildir."
                break
        else:
            return sayı,"sayısı asaldır."

    def faktoriyel (sayı):
        toplam = 1
        for i in range(1,sayı+1):
            toplam *=i
        return(toplam)

    def mükemmel (sayı):
        toplam = 0
        for i in range(1,sayı):
            if sayı % i == 0:
                toplam += i
            if (toplam == sayı):
                return sayı,"mükemmel sayıdır."
                break
        else:
            return sayı,"Mükemmel sayı değildir."
        
    def toplama (a,b):
        return a+b

    def üslü (a,b):
        c = a**b 
        return c


    print("""
    ****************************************************
        - Faktoriyel bulmak için BİRİ tuşlayın

        - Mükemmel sayıyı bulmak için İKİYİ tuşlayın

        - Üslü sayı işlemi yapmak için ÜÇÜ tuşlayın

        - Asal sayı bulmak için DÖRDÜ tuşlayın

        - Uygulamadan çıkma için X tuşunu girin !

    ****************************************************
        """)
    while True:
        islem = input("İşleminizi giriniz:")

        if(islem == "1"):
            sayıf = int(input("Faktoriyeli bulunmak istenen sayıyı giriniz:"))
            time.sleep(1)
            print(faktoriyel(sayıf))
                
        elif(islem == "2"):
            sayım = int(input("Mükemmel sayıyı bulun:"))
            time.sleep(1)
            print(mükemmel(sayım))

        elif(islem == "3"):
            sayıu1 = int(input("Bulunmak istenen üslü sayının tabanını giriniz:"))
            sayıu2 = int(input("Bulunmak istenen üslü sayının üssünü giriniz:"))
            time.sleep(1)
            print(üslü(sayıu1,sayıu2))
  
        elif(islem == "4"):
            sayıa = int(input("Asal sayı kontrol edici:"))
            time.sleep(1)
            print(asal(sayıa))

        elif (islem == "x"):
            time.sleep(1)
            print("Çıkış yapılıyor...")
            break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------3

def tahmin_oyunu():

    print("""
        *********************
        *                   *
        * Sayı Tahmin Oyunu *
        *                   *
        *********************
        """)

    ara = int(input("Birle kaç arasını tutmak istersin: "))

    hak = int(input("Kaç hakkın olsun:"))

    kafa = random.randint(1,ara)

    while True:
        tahmin = int(input("\nTahmininizi giriniz:"))
            
        if tahmin == kafa :
            time.sleep(0.5)
            print("\nDoğru bildin ! Tuttuğum sayı",tahmin)

        elif tahmin != kafa:
            time.sleep(0.5)
            hak -= 1
            print("\nTahminin doğru değil!!!")

            if hak == 0:
                print("\nBen kazandım!!! Tuttuğum sayı şuydu :",kafa,"\n")
                break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------4
            
pc = pc()

print("""
----------------------------------
  Bilgisayarı açmak '1' tuşlayın
----------------------------------
""")

while True:

    işlem = input("----> ")
    
    if işlem == "1":
        time.sleep(2)
        pc.pc_aç()

        print("""
        ---------------------------------------------------

          * Bilgisayarı kapatmak için 'q' tuşlayın.
          * Sistemin sesini açmak için 's' tuşlayın.
          * Hesap makinesini açmak için 'h' tuşlayın.
          * Sayı tahmi oyununu oynamak için 'o' tuşlayın.

        ---------------------------------------------------
        """)

        while True:
            açık_işlem = input("Yapmak istediğiniz işlemi girin: ")

            if açık_işlem == "q" or açık_işlem == "Q":
                time.sleep(2)
                pc.pc_kapat()
                break

            elif açık_işlem == "s" or açık_işlem == "S":
                pc.sistem_ses()

            elif açık_işlem == "h" or açık_işlem == "H":
                hesap_makinesi()

            elif açık_işlem == "o" or açık_işlem == "O":
                tahmin_oyunu()
        
    else:
        print("Böyle bir işlem bulunmamaktadır!")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------5
