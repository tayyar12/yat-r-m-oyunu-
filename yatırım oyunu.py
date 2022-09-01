
import time

print("monopoly oynamaya hazırsan başlıyoruz")
time.sleep(3)
print ("89000 yada 10000000 kredi ile başlamak için sorduğum soruyu doğru bilmelisin tek kişilik bir oyundur ")
time.sleep(3)
print("önce bilgilerini girmelisin")
time.sleep(3)

isim = input("ismin: ")
time.sleep(2)
yas = int(input("yasın nedir: "))
time.sleep(2)

class player:
    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas

player1 = player(isim,yas)

print(f"demek ismin {player1.isim} ve {player1.yas} yasındasın hala gençsin bugün şanslı gününde olsan iyi olur :)")
time.sleep(2)
print("şimdi ise sorduğum soruyu bilmelisin etmelisin ")

time.sleep(2)
soru = print("dünyanın en yakışıklı adı nedir ?")
time.sleep(2)
   
yanıt = input("cevabın nedir: ")

cevap = "onur bayırlı"
time.sleep(2)
if yanıt == cevap:
    print("tebrikler gerçekten şanslı günündesin adamım")
    kredi = 10000000
    time.sleep(2)
    print("bunu hakettin belki işine yarar ")
    time.sleep(5)
    print(f"-tayyar bankanıza  {kredi} lira ekledi")
    time.sleep(3)

else:
    print("gerçekten ne yapmak istediği anlamadım ")
    time.sleep(4)
    bahtsızkredisi = 89000
    print(f" sana {bahtsızkredisi}  lira veriyorum ne yzkki :)")
    time.sleep(3)



time.sleep(1)

print("4 tane harcama var mantıklı olanı seçersen oyunu kazanırsın...")
time.sleep(1)

class harcamalar:
    def __init__(self  ,şuankidegeri,türü,taleparzoranı):
        self.şuankidegeri = şuankidegeri
        self.türü = türü
        self.taleparzoranı = taleparzoranı

evalmak = harcamalar(300000,"bina","fazla talep")
arabaalmak = harcamalar(90000,"araba","normal")
israfedipharcamak = harcamalar(88000,"eğlence","nefsi istek")
işyeriaçmak = harcamalar(100000,"işyeri","çok fazla")

print("işyeri açmak = 85k , talep oranı çok fazla")
time.sleep(2)
print("ev almak = 300k , talep oranı fazla")
time.sleep(2)
print("arkadaşlar ile takılmak = 88k , eğlence ,nefsi istek ")
time.sleep(2)
print("işyeri açmak = 100k , fazla talepli ")

cevab = input ("hamlen nasıl olacak: ")

if   cevab == "araba almak":
    print("iyi son ")
elif cevab == "işyeri açmak":
    print("mükemmel son")
elif cevab == "ev almak":
    print("eh işte son")
elif cevab == "israfedip harcamak":
    print("kötü son ")
time.sleep(3)


print("iyi günler dilerim:) bu sona müzik eklenebilseydi çok güzel olurdu")
