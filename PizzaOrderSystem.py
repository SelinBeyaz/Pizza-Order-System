#KÜTÜPHANELER
import csv 
import datetime

#Menu.txt açılır
f = open("MENU.txt", "r")
print(f.read())


#Pizza sınıfı olusturuldu
class pizza():

    def get_description(self,description): #Açıklamalar için metod olusturuldu
        return description

    def get_cost(self,cost): #fiyat için metod olusturuldu
        return cost

#PİZZA TABANLARI
#Pizza tabanları için classlar oluşturuldu
class klasikpizza(pizza):
    description = "Ananas, jambon, domates sos" #Pizza açıklaması
    cost = 120 #Pizza fiyatı

class margaritapizza(pizza):
    description = "Domates, mozzarella, fesleğen"
    cost =125

class turkpizza(pizza):
    description="Domates sos, zeytinyaği, kekik, sarimsak. Peynir yok."
    cost=130

class sadepizza(pizza):
    description="Jambon, mantar, enginar"
    cost =110

#objeler olusturuldu
klasik = klasikpizza()
margarita=margaritapizza()
turkpizza=turkpizza()
sadepizza=sadepizza()



#SOSLAR
#Decorator sınıfı pizza sınıfının alt sınıfı olarak olusturuldu
class decorator(pizza):

    def get_cost(self,cost):
        return cost

class zeytin(decorator):
    cost=5

class mantar(decorator):
    cost=7

class kecipeyniri(decorator):
    cost=6

class et(decorator):
    cost=10

class sogan(decorator):
    cost=5

class misir(decorator):
    cost=9

#objeler olusturuldu
zeytin = zeytin()
mantar = mantar()
kecipeyniri = kecipeyniri()
et = et()
sogan = sogan()
misir = misir()


#SECİMLER
print("Secimleri menudeki yazi stili seklinde yazmaya dikkat ediniz!!")
pizza_tabani = input("PİZZA TABANİ SECİNİZ : ") #pizza tabani ve sosu kullanıcıdan istenir
sos = input("PİZZA SOSU SECİNİZ : ")

#SECİLEBİLECEK OLASI BİRLEŞİMLER
match pizza_tabani,sos:
    case "Klasik Pizza" , "Zeytin" :
        print("SEPETİNİZ: Klasik Taban + Zeytin")
        total = klasik.get_cost(klasik.cost)+zeytin.get_cost(zeytin.cost) #pizza tabanı fiyatı ve sos fiyatı toplamı total'e esitlendi
        print(f"TOPLAM TUTAR : {total} TL")
        

    case "Klasik Pizza" , "Mantar" :
        print("SEPETİNİZ: Klasik Taban + Mantar")
        total = klasik.get_cost(klasik.cost)+mantar.get_cost(mantar.cost)
        print(f"TOPLAM TUTAR: {total} TL")
        
        
    case "Klasik Pizza" , "Keci Peyniri" :
        print("SEPETİNİZ: Klasik Taban + Keci Peyniri")
        total = klasik.get_cost(klasik.cost)+kecipeyniri.get_cost(kecipeyniri.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Klasik Pizza" , "Et" :
        print("SEPETİNİZ: Klasik Taban + Et")
        total = klasik.get_cost(klasik.cost)+et.get_cost(et.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Klasik Pizza" , "Sogan" :
        print("SEPETİNİZ: Klasik Taban + Sogan")
        total = klasik.get_cost(klasik.cost)+sogan.get_cost(sogan.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Klasik Pizza" , "Misir" :
        print("SEPETİNİZ: Klasik Taban + Misir")
        total = klasik.get_cost(klasik.cost)+misir.get_cost(misir.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Margarita Pizza" , "Zeytin" :
        print("SEPETİNİZ: Margarita Taban + Zeytin")
        total = margarita.get_cost(margarita.cost)+zeytin.get_cost(zeytin.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Margarita Pizza" , "Mantar" :
        print("SEPETİNİZ: Margarita Taban + Mantar")
        total = margarita.get_cost(margarita.cost)+mantar.get_cost(mantar.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Margarita Pizza" , "Keci Peyniri" :
        print("SEPETİNİZ: Margarita Taban + Keci Peyniri")
        total = margarita.get_cost(margarita.cost)+kecipeyniri.get_cost(kecipeyniri.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Margarita Pizza" , "Et" :
        print("SEPETİNİZ: Margarita Taban + Et")
        total = margarita.get_cost(margarita.cost)+zeytin.get_cost(zeytin.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Margarita Pizza" , "Sogan" :
        print("SEPETİNİZ: Margarita Taban + Sogan")
        total = margarita.get_cost(margarita.cost)+sogan.get_cost(sogan.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Margarita Pizza" , "Misir" :
        print("SEPETİNİZ: Margarita Taban + Misir")
        total = margarita.get_cost(margarita.cost)+misir.get_cost(misir.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Turk Pizza" , "Zeytin" :
        print("SEPETİNİZ: Turk Pizza Taban + Zeytin")
        total = turkpizza.get_cost(turkpizza.cost)+zeytin.get_cost(zeytin.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Turk Pizza" , "Mantar" :
        print("SEPETİNİZ: Turk Pizza Taban + Mantar")
        total = turkpizza.get_cost(turkpizza.cost)+mantar.get_cost(mantar.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Turk Pizza" , "Keci Peyniri" :
        print("SEPETİNİZ: Turk Pizza Taban + Keci Peyniri")
        total = turkpizza.get_cost(turkpizza.cost)+kecipeyniri.get_cost(kecipeyniri.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Turk Pizza" , "Et" :
        print("SEPETİNİZ: Turk Pizza Taban + Et")
        total = turkpizza.get_cost(turkpizza.cost)+et.get_cost(et.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Turk Pizza" , "Sogan" :
        print("SEPETİNİZ: Turk Pizza Taban + Sogan")
        total = turkpizza.get_cost(turkpizza.cost)+sogan.get_cost(sogan.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Turk Pizza" , "Misir" :
        print("SEPETİNİZ: Turk Pizza Taban + Misir")
        total = turkpizza.get_cost(turkpizza.cost)+misir.get_cost(misir.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Sade Pizza" , "Zeytin" :
        print("SEPETİNİZ: Sade Taban + Zeytin")
        total = sadepizza.get_cost(sadepizza.cost)+zeytin.get_cost(zeytin.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Sade Pizza" , "Mantar" :
        print("SEPETİNİZ: Sade Taban + Mantar")
        total = sadepizza.get_cost(sadepizza.cost)+mantar.get_cost(mantar.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Sade Pizza" , "Keci Peyniri" :
        print("SEPETİNİZ: Sade Taban + Keci Peyniri")
        total = sadepizza.get_cost(sadepizza.cost)+kecipeyniri.get_cost(kecipeyniri.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Sade Pizza" , "Et" :
        print("SEPETİNİZ: Sade Taban + Et")
        total = sadepizza.get_cost(sadepizza.cost)+et.get_cost(et.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Sade Pizza" , "Sogan" :
        print("SEPETİNİZ: Sade Taban + Sogan")
        total = sadepizza.get_cost(sadepizza.cost)+sogan.get_cost(sogan.cost)
        print(f"TOPLAM TUTAR : {total} TL")


    case "Sade Pizza" , "Misir" :
        print("SEPETİNİZ: Sade Taban + Misir")
        total = sadepizza.get_cost(sadepizza.cost)+misir.get_cost(misir.cost)
        print(f"TOPLAM TUTAR : {total} TL")


print("SECİMİNİZİ YAPTİNİZ.")

#SİPARİS BİLGİLERİ
class kullanici_kimlik(): #kullanıdan ad soyad ve kimlik no istenir
    ad_soyad= input("Adinizi ve Soyadinizi Giriniz : ")
    TC= input("TC kimlik no giriniz : ")
    
class kullanici_kart(): #kullanıcıdan kredi kart no ve kredi kart sifresi istenir
    kredikartno= input("Kredi Karti Numaranizi Giriniz : ")
    kredikartsifre= input("Kredi Kart Sifrenizi Giriniz : ")

#obje olusturuldu
kullanici_kimlik = kullanici_kimlik()
kullanici_kart = kullanici_kart()

#Bilgiler ekrana yazdırıldı
print(kullanici_kimlik)
print(kullanici_kart)

#Siparis saati ve tarihi 
an = datetime.datetime.now()
tarih = datetime.datetime.strftime(an, '%c')

#csv dosyası için bilgiler yazıldı
veriler = [{"--KULLANICI AD-SOYAD--"},{kullanici_kimlik.ad_soyad},
        {"--KULLANICI TC NO--"},{kullanici_kimlik.TC},
        {"--KREDI KARTI NO--"},{kullanici_kart.kredikartno},
        {"--KREDI KART SIFRE--"},{kullanici_kart.kredikartsifre},
        {"--PIZZA TABANI--"},{pizza_tabani},
        {"--SOS--"},{sos},
        {"--SIPARIS TARIHI--"},{tarih}]
#csv dosyası açıldı
with open("Orders_Database.csv","w" ) as dosyam:
    yazici = csv.writer(dosyam)
    yazici.writerows(veriler)

print("SIPARISINIZ ALINMISTIR...")
#SON
