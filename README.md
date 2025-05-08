# Kampanya Fiyatı Güncelleme Aracı

Bu araç, e-ticaret platformları için ürün listesi Excel dosyasındaki kampanyalı satış fiyatlarını belirli kurallara göre otomatik olarak güncelleyen bir Python scriptidir.

## Özellikler

- Mevcut satış fiyatı ile maksimum girilebilecek fiyat arasındaki fark belirli bir yüzdenin altındaysa kampanyalı fiyatı otomatik olarak günceller
- Kullanıcı fiyat farkı yüzdesini belirleyebilir
- Sadece boş olan kampanyalı fiyatları veya tüm ürünleri güncelleme seçeneği
- Renkli ve detaylı konsol çıktısı ile kolay kullanım
- Otomatik rapor oluşturma ve Excel çıktısı
- Özelleştirilebilir giriş ve çıkış dosya adları



## Gereksinimler

- Python 3.6 veya üzeri
- Pandas
- Openpyxl
- Colorama (opsiyonel, renkli çıktı için)

## Kurulum

1. Projeyi klonlayın:
```
git clone https://github.com/Xrutincc/kampanya-fiyat-guncelleme.git
cd kampanya-fiyat-guncelleme
```

2. Gerekli kütüphaneleri yükleyin:
```
pip install -r requirements.txt
```

## Kullanım

1. Excel dosyanızı projenin ana dizininde `kampanya.xlsx` olarak kaydedin veya çalıştırırken kendi dosya adınızı belirtin

2. Scripti çalıştırın:
```
python kampanya_guncelle.py
```

3. İstenilen bilgileri girin:
   - Fiyat farkı yüzdesi (örn: 5 için %5)
   - Excel dosyasının adı
   - Çıktı dosyasının adı
   - Sadece boş olan kampanya fiyatlarını mı güncellemek istediğiniz (E/H)

4. Script çalıştıktan sonra:
   - Güncellenen ürünlerin listesi ekranda gösterilecek
   - Güncellenmiş Excel dosyası kaydedilecek
   - Detaylı bir rapor dosyası oluşturulacak

### Komut Satırı Parametreleri

Fiyat farkı yüzdesini doğrudan komut satırı parametresi olarak verebilirsiniz:

```
python kampanya_guncelle.py 3.5
```

Bu komut, fiyat farkı eşiğini %3.5 olarak ayarlayacaktır.

## Excel Dosya Formatı

Uygulamanın beklediği Excel dosya formatı için [örnek şablon açıklaması](ornek_kampanya.xlsx.md) dosyasına bakın.

