print("Basit Hesap Makinası v.3 Türkçe")

num_1 = float(input("İlk Sayıyı Girin: "))    #ilk sayıyı gir
num_2 = float(input("İkinci Sayıyı Girin: ")) #ikinci sayıyı gir
op = input("Hangi işlemi yapmak istersiniz? (+, -, *, /): ")       #işlemi gir
if op == "+":
    print("Toplam:", num_1, "+", num_2, "=", num_1 + num_2)
elif op == "-":
    print("Kalan:", num_1, "-", num_2, "=", num_1 - num_2)
elif op == "*":
    print("Çarpım:", num_1, "*", num_2, "=", num_1 * num_2)
elif op == "/":
    print("Bölünen:", int(num_1))
    print("Bölen:", int(num_2))
    print("Bölüm:", int(num_1 / num_2))
    print("Kalan:", int(num_1 % num_2))
    print("Kesirli Bölüm:", num_1, "/", num_2, "=", (num_1 / num_2))
else:
    print("Bir yerde hata yaptın!")