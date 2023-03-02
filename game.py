import random
import json
import time

level = 0
puan = 0

with open('dict.json') as f:
    data = json.load(f)

while True:
    mod = 0
    while mod < 1 or mod > 5:
        print('Mod Seçin\n1: Kelime\n2: Telaffuz\n3: Sözlükte Hata Düzeltme\n4: Sözlüğe Kelime Ekle\n5: Programı sonlandır\n')
        mod = int(input())
        print('\n')
    if mod == 1 or mod == 2:
        while (level < 1 or level > 10):
            print('Zorluk Seviyesini Seçin(1-10)\n')
            level = int(input())
            print('\n')
    if mod == 1:
        sec = input('1: Kelime Oyununu Başlat\n2: Geri\nSeçiminiz: ')
        while puan < 100:
            q = int(input('1: Soru iste 2: Oyunu sonlandır Seçiminiz: '))
            if q == 2:
                print(f'Oyun sonlandırıldı. Puanınız: {puan}\n\n')
                break
            random_item = random.choice(data)
            soru = {}
            for key, value in random_item.items():
                soru[key] = value
            if "tr1" in soru:
                tur = [soru["tr1"]]
                if "tr2" in soru:
                    tur.append(soru["tr2"])
                if "tr3" in soru:
                    tur.append(soru["tr3"])
            eng = soru["eng"]
            sec = ['en', 'tr']
            sorudil = random.choice(sec)
            if sorudil == 'en':
                print(eng)
                yanıt = input()
                turkish = ", ".join(str(x) for x in tur)
                if yanıt in tur:
                    print(f'Doğru cevap! Ayrıca bakınız: {turkish}')
                    roundpuan = 1
                else:
                    print(f'Yanlış cevap! Doğrusu: {turkish}')
                    roundpuan = level * -1
                    time.sleep(5)
            elif sorudil == 'tr':
                print(tur)
                yanıt = input()
                if yanıt == eng:
                    print('Doğru cevap!')
                    roundpuan = 1
                else:
                    print(f'Yanlış cevap! Doğrusu: {eng}')
                    roundpuan = level * -1
                    time.sleep(5)
            puan += roundpuan
            if puan < 0:
                puan = 0
            print(f'Puanınız: {puan}\n')
            if puan >= 100:
                print('Tebrikler 100 Puana ulaştınız!\n\nOYUN BİTTİ')

    if mod == 2:
        sec = input('1: Telaffuz Oyununu Başlat\n2: Geri\nSeçiminiz: ')
        while puan < 100:
            q = int(input('1: Soru iste 2: Oyunu sonlandır Seçiminiz: '))
            if q == 2:
                print(f'\n\nOyun sonlandırıldı. Puanınız: {puan}\n\n')
                break
            random_item = random.choice(data)
            soru = {}
            for key, value in random_item.items():
                soru[key] = value
            eng = soru["eng"]
            prn = soru["prn"]
            print(eng)
            yanıt = input(':')

            if yanıt == prn:
                print('Doğru cevap!')
                roundpuan = 1
            else:
                print(f'Yanlış cevap! Doğrusu: {prn}\n')
                time.sleep(5)
                roundpuan = level * -1
            puan += roundpuan
            if puan < 0:
                puan = 0
            print(f'Puanınız: {puan}\n')
            if puan >= 100:
                print('Tebrikler 100 Puana ulaştınız!\n\nOYUN BİTTİ')

    if mod == 3:
        while True:
            sec = input('1: Kelime düzelt\n2: Geri\nSeçiminiz: ')
            anahtar = input("Düzelteceğiniz kelimenin ingilizcesini yazın: ")
            nesne = None
            for item in data:
                if 'eng' in item and item['eng'] == anahtar:
                    nesne = item
                    break
            if nesne is not None:
                print(nesne)
            else:
                print("Belirtilen kelime sözlükte yok.")
                continue
            while True:
                secim = input("1: Mevcut kelimenin değerlerini güncelle\n2: Yeni anlam ve değer ekle\n3: Başka bir kelimeyi düzenle\nSeçiminiz: ")
                print('\n\n')
                if secim == "1":
                    print("Mevcut anahtarlar:", list(nesne.keys()))
                    anahtar = input("Hangi kelimenin değerlerini güncellemek istersiniz? ")
                    if anahtar in nesne:
                        yeni_deger = input("Yeni değer: ")
                        nesne[anahtar] = yeni_deger
                        print(f"{anahtar} anahtarının değeri başarıyla güncellendi.")
                        print("Güncel:", nesne, "\n\n")
                        kayıt = input('Değişiklikleri kaydetmek istiyor musunuz?(y/n): ')
                        if kayıt.lower == 'y':
                            for item in data:
                                if item['eng'] == anahtar:
                                    data.remove(item)
                            with open('dict.json', 'w') as f:
                                json.dump(data, f)
                            new_item = nesne
                            data.append(new_item)
                            with open('dict.json', 'w') as f:
                                json.dump(data, f)
                            print('Değişiklikler kaydedildi!\n\n')
                    else:
                        print(f"{anahtar} anahtarı bulunamadı.")

                elif secim == "2":
                    anahtar = input("Yeni anahtar: ")
                    yeni_deger = input("Yeni değer: ")
                    nesne[anahtar] = yeni_deger
                    print(f"{anahtar} başarıyla eklendi.")
                    print("Güncel:", nesne, "\n\n")
                    kayıt = input('Değişiklikleri kaydetmek istiyor musunuz?(y/n): ')
                    if kayıt.lower == 'y':
                        for item in data:
                            if item['eng'] == anahtar:
                                data.remove(item)
                        with open('dict.json', 'w') as f:
                            json.dump(data, f)
                        new_item = nesne
                        data.append(new_item)
                        with open('dict.json', 'w') as f:
                            json.dump(data, f)
                        print('Değişiklikler kaydedildi!\n\n')
                elif secim == "3":
                    break
                else:
                    print("Geçersiz seçim.")

    if mod == 4:
        while True:
            sec = input('1: Yeni kelime ekle\n2: Geri\nSeçiminiz: ')
            if sec == '1':
                yenikelime = {}
                eng = input('İngilizce kelimeyi girin: ')
                yenikelime['eng'] = eng
                prn = input('Okunuşunu yazın: ')
                yenikelime['prn'] = prn
                tr1 = input('Türkçe karşılık ekleyin: ')
                yenikelime['tr1'] = tr1
                tr2 = input('Bir başka türkçe karşılık ekleyin: ')
                if tr2 != '':
                    yenikelime['tr2'] = tr2
                tr3 = input('Bir başka türkçe karşılık ekleyin: ')
                if tr3 != '':
                    yenikelime['tr3'] = tr3
                if eng == '' or prn == '' or tr1 == '':
                    print('İngilizce, Okunuş ve en az 1 türkçe karşılık girmek zorunludur.\n\n')
                    continue
                else:
                    data.append(yenikelime)
                    # JSON dosyasına kaydet
                    with open('dict.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
            else:
                break

    if mod == 5:
        print('Program sonlandırıldı')
        break