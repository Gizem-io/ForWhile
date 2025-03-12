class ToplamHesapla:
    def __init__(self, sayi):
        self.sayi = sayi

    def for_ile_toplam(self):
        toplam = 0
        for i in range(1, self.sayi + 1):
            toplam += i
        return toplam

    def while_ile_toplam(self):
        toplam = 0
        i = 1
        while i <= self.sayi:
            toplam += i
            i += 1
        return toplam

if __name__ == "__main__":
    try:
        girilen_sayi = int(input("Bir sayı giriniz: "))
        if girilen_sayi < 1:
            print("Lütfen pozitif bir tam sayı giriniz!")
        else:
            hesaplayici = ToplamHesapla(girilen_sayi)
            
            for_sonuc = hesaplayici.for_ile_toplam()
            while_sonuc = hesaplayici.while_ile_toplam()
            
            print(f"For döngüsü ile hesaplanan toplam: {for_sonuc}")
            print(f"While döngüsü ile hesaplanan toplam: {while_sonuc}")
            
    except ValueError:
        print("Lütfen geçerli bir tam sayı giriniz!")
