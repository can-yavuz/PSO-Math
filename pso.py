import tkinter as tk
import random


def hedef_fonksiyon(parcacik): #textbox'a girilecek x degeri parametre olarak alindi, bu x degerinde parcaciklar denenerek optimum sonuca ulasilmasi hedeflenmektedir

    try:
        fonksiyon = textbox_fonksiyon.get() 
        result = eval(fonksiyon, {'x': parcacik})
        return result
    except ZeroDivisionError:
        result2 = eval(fonksiyon, {'x': parcacik + random.random()})
        return result2

def pso():

    parcacik_sayisi = 20

    #kullanicidan alinan parametreler
    iterasyon_sayisi = int(textbox_iterasyon.get())
    aralik_baslangic = int(textbox_min.get())
    aralik_bitis = int(textbox_max.get())

    w = 0.5 # agirlik faktoru
    c1 = 0.5 # sabit degerler
    c2 = 0.9

    particles = []
    velocities = []

    # parcacik sayisi kadar verilen aralikta parcaciklar olusturma
    for i in range(parcacik_sayisi):
        particles.append(random.uniform(aralik_baslangic, aralik_bitis))

    for i in range(parcacik_sayisi):
        velocities.append(0)

    personal_best = particles # parcaciklarin son konumlarini guncellemek icin olusturulan kopya array
    global_best = particles[0] # tum parcaciklarin icindeki en iyi konum
    global_best_fitness = hedef_fonksiyon(particles[0]) #g_best degerinin fonksiyona yerlestirilmesi

    #onceki iterasyonlari temizleme
    text_islemler.delete("1.0", tk.END)

    for iterasyon in range(iterasyon_sayisi):
        
        for i in range(parcacik_sayisi):

            #0-1 araliginda random sayilar uretme
            r1 = random.random()
            r2 = random.random()

            #PSO FORMULU
            #parçacığın hızını belirleme
            velocities[i] = w * velocities[i] + c1 * r1 * (personal_best[i] - particles[i]) + c2 * r2 * (global_best - particles[i])
            #parçacığın değerini güncelleme
            particles[i] = particles[i] + velocities[i]

            #parcaciklarin konumunu verilen aralikta tutma
            if particles[i] < aralik_baslangic:
                particles[i] = aralik_baslangic

            if particles[i] > aralik_bitis:
                particles[i] = aralik_bitis

            #parcacigi matematiksel fonksiyonda x yerine yazip sonuc degerini alma
            fonksiyonun_sonucu = hedef_fonksiyon(particles[i])

            #fonksiyonun sonucunu karsilastirarak optimum degeri bulma
            if fonksiyonun_sonucu > hedef_fonksiyon(personal_best[i]):
                personal_best[i] = particles[i]

            if fonksiyonun_sonucu > global_best_fitness:
                global_best = particles[i]
                global_best_fitness = fonksiyonun_sonucu
                
            #ciktilari ekrana yazdırma
            text_islemler.insert("1.0","iterasyon: " + str(iterasyon+1) +
            "\tParçacık: "+str(i+1) +
            "\tFonksiyonun sonucu: " + str(hedef_fonksiyon(particles[i])) +
             "\tX degeri: "+str(particles[i])+ "\n")

    textbox_sonuc.delete(0, tk.END)
    textbox_sonuc.insert(0, str(global_best))

#GUI
root = tk.Tk()
root.title("PSO ile Matematiksel İfadeyi Maksimum Yapan X Değeri Bulma")

label_fonksiyon = tk.Label(root, text="Matematiksel İfade", font=('Cascadia Code', 15))
label_fonksiyon.pack()
textbox_fonksiyon = tk.Entry(root, width=50, font=('Cascadia Code', 15))
textbox_fonksiyon.pack()

label_minmax = tk.Label(root, text="X değeri aralığı", font=('Cascadia Code', 15))
label_minmax.pack()
textbox_min = tk.Entry(root, width=10, font=('Cascadia Code', 15))
textbox_min.pack()
textbox_max = tk.Entry(root, width=10, font=('Cascadia Code', 15))
textbox_max.pack()

label_iterasyon = tk.Label(root, text="İterasyon Sayısı", font=('Cascadia Code', 15))
label_iterasyon.pack()
textbox_iterasyon = tk.Entry(root, width=10, font=('Cascadia Code', 15))
textbox_iterasyon.pack()

buton_hesapla = tk.Button(root, text="Hesapla",command=pso, font=('Cascadia Code', 15))
buton_hesapla.pack()

label_sonuc = tk.Label(root, text="Fonksiyonun En Büyük Değerini Veren X Değeri", font=('Cascadia Code', 15))
label_sonuc.pack()
textbox_sonuc = tk.Entry(root, width=50, font=('Cascadia Code', 15))
textbox_sonuc.pack()

text_islemler = tk.Text(root, width=800, font=('Cascadia Code', 15))
text_islemler.pack()

root.mainloop()