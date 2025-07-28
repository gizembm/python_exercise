#####################################
# Python Temelleri - Ödev Scripti
#####################################

# Soru 1:
# Bir integer, bir float ve bir complex sayı tanımlayın.
# Bu sayıların türlerini yazdırın ve aralarında 1-2 işlem yapın.

x = 5
y = 25.4
z = 3 + 2j

print(type(x))
print(type(y))
print(type(z))

a = x + y
b = z * x

print(a)
print(b)

# Soru 2:
# İsminizi içeren bir string değişkeni oluşturun.
# Bu stringin ilk ve son karakterini yazdırın. Ayrıca tüm harfleri büyük yaparak ekrana yazdırın.

name = "gizem"

print(name[0])
print(name[-1])
print(name.upper())



# Soru 3:
# Aşağıdaki string içinde "veri" kelimesi geçiyor mu kontrol edin.
# Ardından bu stringi boşluklardan bölerek liste haline getirin.

sentence = "Veri bilimi yapay zeka ile birleştiğinde güçlü sonuçlar doğurabilir."

print("veri" in sentence.lower())

print(sentence.split())


# Soru 4:
# İçerisinde 3 farklı türde veri bulunan bir liste oluşturun.
# Listenin uzunluğunu, ilk ve son elemanını yazdırın.
# Ardından bu listeye yeni bir eleman ekleyin ve ikinci elemanı silin.

list = [1, "gizem", 125.4]

print(list[0])
print(list[-1])
print(len(list))

list.remove("seyma")
list.remove(125.4)

print(list)

# Soru 5:
# 2 parametre alan bir fonksiyon yazın. Bu fonksiyon, aldığı iki sayının ortalamasını dönsün.

def mean (x, y):
   return (x + y) / 2

mean(7, 9)


# Soru 6:
# Kullanıcının yaşına göre mesaj yazdıran bir fonksiyon yazın:
# 18'den küçükse "Çok gençsin!", 18-40 arasıysa "Harika bir yaştasın!", 40'tan büyükse "Deneyim önemli!" mesajını yazdırsın.

def yas_mesaj (yas):
    if yas < 18:
        print("Çok gençsin!")
    elif 18 <= yas <= 40:
        print("Harika bir yaştasın!")
    else :
        print("Deneyim önemli!")


yas_mesaj(35)
yas_mesaj(10)
yas_mesaj(87)

# Soru 7:
# İçerisinde sayılar olan bir liste içindeki sayıları dolaşarak 2 katını ekrana yazdırın (for döngüsü ile).

my_list = [10, 14, 74, 21, 17, 32, 54]

for x in my_list:
    new_my_list = []
    new_my_list.append(x * 2)
    print(new_my_list)

# Soru 8:
# 1'den başlayarak 20 dahil olacak şekilde çift sayıları yazdırın (while döngüsü ile).

sayi = 1

while sayi <= 20:
    if sayi % 2 == 0:
        print(sayi)
    sayi += 1



# Soru 9:
# Bir çalışanın haftalık maaşını hesaplayan bir fonksiyon yazın.
# Saatlik ücreti ve haftalık toplam çalışma saati parametre olarak alınsın.
# Haftada 40 saatten fazla çalıştıysa, fazla saatler için %50 zamlı ücret ödensin (mesai).
# Örnek: 45 saat çalışan biri için 5 saatlik mesai uygulanmalı.

def maas_hesapla(saatlik_ucret, calısma_saati):
    if calısma_saati <= 40:
        return saatlik_ucret * calısma_saati
    else:
        normal_saat =  saatlik_ucret * 40
        mesai_saat = saatlik_ucret * (calısma_saati - 40) * 1.5
        return normal_saat + mesai_saat

maas_hesapla(750, 30)
maas_hesapla(750, 41)