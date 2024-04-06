# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:39:21 2024

@author: lenovo
"""

#While Örnekleri
i=0
while (i<10):
    print(i)
    i+=1

k=0
while(k<20):
    print(k)
    k+=3
    
j=0    
liste=[2,5,6,8,7,8,111,55,1,33]
while(j<len(liste)):
    print("İndeks : ",j,"Değeri : ",liste[j])
    j +=1
    
    
#Break Continue

i = 0
while(i<15):
    print(i)
    if(i==10):
        break
    i +=1
    
    
for i in range(0,20):
    if(i == 10 ):
        break # 10 u yazmaz 
    print(i)
    
for i in range(0,20):
    print(i)
    if(i == 10 ):
        break # 10 u yazar
        
        
while True:
    isim = input("İsminizi yazınız (Çıkış için c):")
    if(isim == "c" or isim == "C"):
        print("Çıkıs Yapılıyor")
        break
    print(isim)
    
    
while True:
    Sayı= input("Lütfen Bir Sayı Giriniz (Çıkıs için -1): ")
    if(Sayı== "-1"):
        print("Çıkış Yapılıyor")
        break
    print(Sayı)
    
    
#FaktoriyelHesaplama
           
while True:
    Sayı= int(input("Lütfen Bir Sayı Giriniz (Çıkıs için -1): "))
    if(Sayı == -1 or Sayı < 0 ):
        print("Çıkış Yapılıyor")
        break
    
    faktoriyel = 1
    for i in range(2,Sayı+1):
        faktoriyel *= i
        print(faktoriyel)
        

    
    
            
            
    
    

    
