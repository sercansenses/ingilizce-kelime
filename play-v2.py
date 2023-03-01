import random
import time
import csv

score = 0
puan = 0

with open('dict.csv', mode='r', encoding='utf-8') as dict_file:
    dict_reader = csv.reader(dict_file)
    sozluk = {rows[0]: rows[1:] for rows in dict_reader}

with open('pronunc.csv', mode='r', encoding='utf-8') as pronunc_file:
    pronunc_reader = csv.reader(pronunc_file)
    pronunc = {rows[0]: rows[1] for rows in pronunc_reader}

print('Aşağıdaki listeden bir uygulama seçin ve sayısını yazın.\n')
print('1 - Telaffuz\n2 - Kelime\n3 - Hata düzeltme\n')
mod = int(input())
while True:
    if mod < 1 or mod > 3:
        mod = int(input('\nLütfen geçerli bir uygulama numarası yazın.\n1 - Telaffuz\n2 - Kelime\n3 - Hata düzeltme'))
        continue
    else:
        break

if mod == 1 or mod == 2:
    level = int(input("\nZorluk seviyesini seçin (1-10): "))
    while level < 1 or level > 10:
        level = int(input("Geçersiz değer. Zorluk seviyesini seçin (1-10): "))

if mod == 1:
    while True:
        random_key = random.choice(list(pronunc.keys()))
        print("İngilizce: ", random_key)
        user_input = input("Lütfen telaffuzunu yazın\n")
        if pronunc[random_key] == user_input:
            print("\nDoğru!")
            puan += 1
            print(f'Puanınız: {puan}\n')
        else:
            print("\nYanlış!\n")
            if puan < 0:
                puan = 0
            else:
                puan -= level
                if puan < 0:
                    puan = 0
            print(f'Doğrusu şu şekilde okunuyor:{pronunc[random_key]}')
            print(f'Puanınız: {puan}\n')
            time.sleep(5)

if mod == 2:
    with open('dict.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        sozluk = {}
        for row in reader:
            sozluk[row[0]] = row[1:]
            
    while score < 100:
        # Rastgele kelime seç
        word = random.choice(list(sozluk.keys()))
        values = sozluk[word]
        # İngilizce-Türkçe sorusu yap
        if random.choice([True, False]):
            answer = input("\nWhat is the Turkish equivalent of '{}'?\n".format(word))
            correct_answers = [value for value in values if answer.lower() == value.lower()]
            if correct_answers:
                print("Correct!")
                score = max(score + len(correct_answers), 0)
            else:
                print("Wrong!")
                score = max(score - level, 0)
            # doğru cevapları göster
            print("The correct answer: {}.".format(", ".join(values)))
        # Türkçe-İngilizce sorusu yap
        else:
            answer = input("\nWhat is the English equivalent of '{}'?\n".format(", ".join(values)))
            if answer.lower() == word.lower():
                print("Correct!")
                score = max(score + 1, 0)
            else:
                print("Wrong!")
                score = max(score - level, 0)
            # doğru cevabı göster
            print("The correct answer: '{}'.".format(word))
        # Puanı yazdır
        print("Your score is {}.".format(score))
        print('\n')
        time.sleep(5)
    # Oyun bitti
    print("Congratulations, you scored 100 points!")


if mod == 3:
    while True:
        # CSV dosyasını oku ve bir sözlük oluştur
        with open('dict.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            dictionary = {row['English']: row['Turkish'] for row in reader}

        # Kullanıcıdan kelime iste
        word = input('Türkçe karşılığını düzeltmek istediğiniz ingilizce kelimeyi yazın: ')

        # Türkçe karşılıkları göster
        if word in dictionary:
            print(f"Mevcut türkçe karşılıkları bunlar: '{word}':")
            print(dictionary[word])
        else:
            print(f"Bu kelimenin türkçe karşılığını bulamadım: '{word}'")

        # Kullanıcıdan düzeltme yapmasını iste
        if word in dictionary:
            correction = input(f"Düzeltilmiş halini yazın: '{dictionary[word]}': ")
            dictionary[word] = correction

            # Dosyayı güncelle
            with open('dict.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['English', 'Turkish']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for word, translation in dictionary.items():
                    writer.writerow({'English': word, 'Turkish': translation})
