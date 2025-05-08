# Örnek Excel Şablonu

Bu dosya, projeyi kullanmak isteyenler için örnek bir Excel şablonu formatını açıklamaktadır.

## Excel Dosya Formatı

Kampanya Fiyatı Güncelleme Aracı'nın bekleyeceği Excel dosya formatı aşağıdaki sütunları içermelidir:

| Sütun Adı | Açıklama |
|-----------|----------|
| Barkod | Ürün barkod numarası |
| Ürün Adı | Ürünün tam adı |
| Ürün Kodu | Ürünün kodu |
| Kategori | Ürün kategorisi |
| Marka | Ürünün markası |
| Renk | Ürünün rengi (opsiyonel) |
| Beden | Ürünün bedeni (opsiyonel) |
| Stok Kodu | Stok kodu |
| Mevcut Stok | Mevcut stok adedi |
| Mevcut Satış Fiyatı | Ürünün güncel satış fiyatı |
| Maksimum Girebileceğin Fiyat | Kampanya için girilebilecek maksimum fiyat |
| Kampanyalı Satış Fiyatı | Kampanya fiyatı (boş olabilir, program bu alanı dolduracak) |
| Ürün Komisyon Tarifesi | Komisyon bilgisi |
| ListingId | Ürün listesi kimliği |

## Örnek Veri

```
Barkod	Ürün Adı	Ürün Kodu	Kategori	Marka	Renk	Beden	Stok Kodu	Mevcut Stok	Mevcut Satış Fiyatı	Maksimum Girebileceğin Fiyat	Kampanyalı Satış Fiyatı	Ürün Komisyon Tarifesi	ListingId
ST89702	KAYIŞ SCOOTER 125 CC HONDA FIZY [743 X 20 X 30] #53040	ST89702	Motosiklet Yedek Parçalar	Michelin			ST89702	3	638,28	622,47		Yok	ee44936eb3417e243aa2e647daabb282
ST91502	KAYIŞ DIO [799 x 19.5 x 30] #53063	ST91502	Motosiklet Yedek Parçalar	Michelin			ST91502	20	599,98	585,12		Yok	11a8fce9ba6a8b15d9a0d9caef3db529
```

## Notlar

1. Tüm fiyat sütunları sayısal değerler içermelidir
2. Boş değer olabilen alanlar: Renk, Beden, Kampanyalı Satış Fiyatı
3. Program, Mevcut Satış Fiyatı ile Maksimum Girebileceğin Fiyat arasındaki fark belirtilen yüzde değerinden az ise Kampanyalı Satış Fiyatı sütununu dolduracaktır 