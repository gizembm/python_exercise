###############################
# Numpy & Pandas - Ödev Soruları
###############################

import numpy as np
import pandas as pd
import seaborn as sns

###############################
# Soru 1:
# 1D ve 2D array'ler oluşturun.
# Bu array’lerin boyut, eleman sayısı ve şekil bilgilerini yazdırın.

arr1D = np.arange(1,30,3)
arr2D = np.random.randint(1, 500, (2,3))

print("1.dizinin şekli:", arr1D.shape)
print("1.dizinin eleman sayısı:", arr1D.size)
print("1.dizinin boyut sayısı:", arr1D.ndim)

print("----------------------------------")
print("2.dizinin şekli :", arr2D.shape)
print("2.dizinin eleman sayısı:", arr2D.size)
print("2.dizinin boyut sayısı:", arr2D.ndim)

###############################
# Soru 2:
# 5 elemanlı rastgele sayılardan oluşan bir array oluşturun.
# Elemanların ortalamasını, standart sapmasını ve medyanını bulun.

new_arr = np.random.randint(1, 100, (5,))

print(new_arr)
print("new arr'ın ortalaması:" , new_arr.mean())
print("new arr'ın standart sapması:" , new_arr.std())
print("new arr'ın medyanı:" ,np.median(new_arr))

###############################
# Soru 3:
# 0 ile 1 arasında 10 eşit aralıklı sayı üretin.
# Bu sayılardan 0.5'ten büyük olanları filtreleyip yazdırın.

lin_arr = np.linspace(0, 1, 10)

print(lin_arr)

filtered = lin_arr[lin_arr > 0.5]
print("0.5'ten büyükler: ", filtered)

###############################
# Soru 4:
# Pandas Series kullanarak öğrencilerin yaşlarını tutan bir seri oluşturun.
# Yaş ortalamasını ve en küçük yaşı bulun.

yaslar = pd.Series([14, 22, 41, 43, 61, 74])
print("ortalama yas:" , yaslar.mean())
print("en küçük yaş:", yaslar.min())


###############################
# Soru 5:
# seaborn içerisinden "diamonds" veri setini alın.
# Sadece "carat" ve "price" sütunlarını içeren ilk 5 satırı yazdırın.

df = sns.load_dataset("diamonds")
df.head()

print(df[["carat","price"]].head())

###############################
# Soru 6:
# Fiyatı 15.000’den fazla olan kaç elmas var?

count = df[df["price"] > 15000].shape[0]
print("15.000'den pahalı elmas sayısı: ", count)



###############################
# Soru 7:
# “cut” sütunundaki her bir kesim tipi için ortalama fiyatı(price) hesaplayın.

ort_fiyat = df.groupby("cut")["price"].mean()
print(ort_fiyat)



###############################
# Soru 8:
# pivot_table kullanarak her “cut” tipi için hem ortalama “carat” hem de “price” değerlerini gösterin.

pivot_table = df.pivot_table(
    values = ["carat", "price"],
    index = ["cut"],
    aggfunc = "mean"
)

print(pivot_table)



###############################
# Soru 9:
# “color” sütununda kaç farklı renk olduğunu bulun. Her bir rengin kaç kez geçtiğini de yazdırın.

renk_sayisi = df["color"].nunique()
renk_frekans = df["color"].value_counts()

print("Farklı renk sayısı:", renk_sayisi)
print("Her rengin frekansı:\n", renk_frekans)


###############################
# Soru 10:
# “cut” ve “clarity” kombinasyonlarına göre ortalama fiyatları hesaplayın.

kombinasyon = df.groupby(["cut", "clarity"])["price"].mean()
print(kombinasyon)