# Tarih: 22.04.2021
# Udemy muratçoşkun kumanda classı denemesi
# Plazm4

import random


class kumanda():

    def __init__(self,tv_durum = "Kapalı",tv_ses = 6,tv_kanal = ["Trt"],kanal = "Trt"):

        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.tv_kanal = tv_kanal
        self.kanal = kanal

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------0

    def tv_aç(self):

        if (self.tv_durum == "Açık" ):
            print ("Tv zaten açık...")

        else:
            print("Tv açılıyor...")
            self.tv_durum = "Açık"
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------1

    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Tv zaten kapalı...")

        else:
            print("Tv kapatılıyor..."),

            self.tv_durum = "Kapalı"
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------2

    def ses (self):

        print("""
              Sesi açmak için '+' tuşuna basın
              Sesi kapatmak için '-' tuşuna basın
              Ses işleminden çıkmak için 'q' tuşuna basın:\n""")

        while True:
            ses_işlem = input("İşlemi seçiniz:")

            if ses_işlem == "+":
                self.tv_ses += 2
                print("Ses arttırıldı:{}".format(self.tv_ses))
                if self.tv_ses == 32:
                    print("Ses daha fazla arttırılamaz. Maksimum ses: 32")
                    break

            elif ses_işlem == "-":
                self.tv_ses -= 2
                print("Ses azaltıldı:{}".format(self.tv_ses))
                if self.tv_ses == 0:
                    print("Ses daha fazla azaltılamaz. Minimum ses: 0")
                    break

            elif ses_işlem == "q":
                print("Ses ayarından çıkış yapılıyor... Son ses düzeyi: {}".format(self.tv_ses))
                break

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------3

    def kanal_ras (self):

        rastgele = random.randint(0,len(self.tv_kanal)-1)

        self.kanal = self.tv_kanal[rastgele]

        print("Rastgele açılan kanal:",self.kanal)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------4

    def kanal_ekleme(self):

        ekleme = input("Eklemek istediğiniz kanalın ismini giriniz:")

        self.tv_kanal.append(ekleme)

        print(self.tv_kanal)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------5

    def __len__(self):

        return len(self.tv_kanal)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------6

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.tv_kanal,self.kanal)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------7

kumanda = kumanda()

print("""
----------------------------------------------------

   * Tv açmak için 1 tuşlayın

   * Tv kapatmak için 2 tuşlayın

   * Tv ses ayarı için 3 tuşlayın

   * Rastgale kanal açmak için 4 tuşlayın

   * Kanal eklemek için 5 tuşlayın

   * Tv son durumunu öğrenmek için 6 tuşlayın

   - Tvdeki kanal sayısını öğrenmek için 7 tuşlayın

   * Menüden çıkmak için 'e' tuşlayın

----------------------------------------------------
""")

while True:

    işlem = input("\nYapmak istediğiniz işlem: ")

    if işlem == "e":
        print("Menüden çıkılıyor...")
        break

    if işlem == "1":

        kumanda.tv_aç()

    elif işlem == "2":

        kumanda.tv_kapat()

    elif işlem == "3":

        kumanda.ses()

    elif işlem == "4":

        kumanda.kanal_ras()

    elif işlem == "5":

        kumanda.kanal_ekleme()

    elif işlem == "6":

        print(kumanda)

    elif işlem == "7":

        print("Kanal Sayısı: ",len(kumanda))

    else:
        print("\nKumanda da böyle bir seçenek yok lütfen başka bir işlem seçiniz!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------8
