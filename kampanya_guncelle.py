import pandas as pd
import sys
import os
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init()  
    RENKLI_CIKTI = True
except ImportError:
    RENKLI_CIKTI = False

def renkli_yazdir(metin, renk_kodu=None, stil=None):
    """Renklendirme kütüphanesi yüklüyse metni renklendirir"""
    if RENKLI_CIKTI and renk_kodu:
        stil_baslangic = Style.BRIGHT if stil else ""
        stil_son = Style.RESET_ALL if stil else ""
        print(f"{stil_baslangic}{renk_kodu}{metin}{stil_son}")
    else:
        print(metin)

baslık = "KAMPANYA FİYATI GÜNCELLEME ARACI"
renkli_yazdir(f"\n{'=' * 50}", Fore.CYAN, True)
renkli_yazdir(f"{baslık.center(50)}", Fore.CYAN, True)
renkli_yazdir(f"{'=' * 50}\n", Fore.CYAN, True)

try:
    if len(sys.argv) > 1:
        fark_yuzdesi = float(sys.argv[1])
    else:
        fark_yuzdesi = float(input("Fiyat farkı yüzdesi (örn: 5 için %5): "))

    renkli_yazdir(f"Belirlenen fiyat farkı eşiği: %{fark_yuzdesi}", Fore.GREEN)
except ValueError:
    renkli_yazdir("Geçerli bir sayı girmelisiniz. Varsayılan değer %5 olarak ayarlandı.", Fore.YELLOW)
    fark_yuzdesi = 5

excel_dosyasi = input("Excel dosyasının adını girin (varsayılan: kampanya.xlsx): ").strip()
if not excel_dosyasi:
    excel_dosyasi = "kampanya.xlsx"

cikti_dosyasi = input("Çıktı dosyasının adını girin (varsayılan: kampanya_guncellenmis.xlsx): ").strip()
if not cikti_dosyasi:
    cikti_dosyasi = "kampanya_guncellenmis.xlsx"

sadece_bos_guncelle = input("Sadece kampanya fiyatı boş olanları mı güncellemek istiyorsunuz? (E/H, varsayılan: E): ").strip().upper()
sadece_bos_guncelle = sadece_bos_guncelle != "H"  

try:
    if not os.path.exists(excel_dosyasi):
        renkli_yazdir(f"Hata: {excel_dosyasi} dosyası bulunamadı!", Fore.RED, True)
        exit(1)

    df = pd.read_excel(excel_dosyasi)
    renkli_yazdir(f"Excel dosyası başarıyla yüklendi. Toplam {len(df)} ürün bulundu.", Fore.GREEN)
except Exception as e:
    renkli_yazdir(f"Excel dosyası yüklenirken hata oluştu: {e}", Fore.RED, True)
    exit(1)

guncellenen_urun_sayisi = 0
guncellenen_urunler = []

for index, row in df.iterrows():
    try:
        mevcut_fiyat = row['Mevcut Satış Fiyatı']
        maksimum_fiyat = row['Maksimum Girebileceğin Fiyat']

        if pd.notna(mevcut_fiyat) and pd.notna(maksimum_fiyat):

            if sadece_bos_guncelle and pd.notna(row['Kampanyalı Satış Fiyatı']):
                continue

            fark = mevcut_fiyat - maksimum_fiyat
            fark_yuzdesi_hesaplanan = (fark / mevcut_fiyat) * 100

            if abs(fark_yuzdesi_hesaplanan) <= fark_yuzdesi:
                df.at[index, 'Kampanyalı Satış Fiyatı'] = maksimum_fiyat
                guncellenen_urun_sayisi += 1

                guncellenen_urunler.append({
                    'Barkod': row['Barkod'],
                    'Ürün Adı': row['Ürün Adı'],
                    'Mevcut Fiyat': mevcut_fiyat,
                    'Maksimum Fiyat': maksimum_fiyat,
                    'Fark Yüzdesi': abs(fark_yuzdesi_hesaplanan)
                })
    except Exception as e:
        renkli_yazdir(f"Satır {index+2} işlenirken hata oluştu: {e}", Fore.RED)

if guncellenen_urun_sayisi > 0:
    renkli_yazdir("\nGÜNCELLENEN ÜRÜNLER:", Fore.CYAN, True)
    renkli_yazdir("-" * 100, Fore.CYAN)

    format_str = "{:<15} {:<40} {:<15} {:<15} {:<15}"
    renkli_yazdir(format_str.format("BARKOD", "ÜRÜN ADI", "MEVCUT FİYAT", "MAKSİMUM FİYAT", "FARK %"), Fore.YELLOW)
    renkli_yazdir("-" * 100, Fore.CYAN)

    for urun in guncellenen_urunler:
        print(format_str.format(
            urun['Barkod'],
            urun['Ürün Adı'][:37] + "..." if len(urun['Ürün Adı']) > 40 else urun['Ürün Adı'],
            f"{urun['Mevcut Fiyat']:.2f} TL",
            f"{urun['Maksimum Fiyat']:.2f} TL",
            f"%{urun['Fark Yüzdesi']:.2f}"
        ))

    renkli_yazdir("-" * 100, Fore.CYAN)
    renkli_yazdir(f"\nToplam {guncellenen_urun_sayisi} ürünün kampanyalı fiyatı güncellendi.", Fore.GREEN, True)
else:
    renkli_yazdir("\nHiçbir ürünün fiyatı güncellenmedi!", Fore.YELLOW, True)

try:
    df.to_excel(cikti_dosyasi, index=False)
    renkli_yazdir(f"Güncellenmiş Excel dosyası '{cikti_dosyasi}' olarak kaydedildi.", Fore.GREEN)

    istatistik_dosyasi = f"rapor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(istatistik_dosyasi, "w", encoding="utf-8") as f:
        f.write(f"KAMPANYA FİYATI GÜNCELLEME RAPORU - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"{'=' * 70}\n\n")
        f.write(f"Excel dosyası: {excel_dosyasi}\n")
        f.write(f"Çıktı dosyası: {cikti_dosyasi}\n")
        f.write(f"Fiyat farkı eşiği: %{fark_yuzdesi}\n")
        f.write(f"Sadece boş fiyatlar güncellendi: {'Evet' if sadece_bos_guncelle else 'Hayır'}\n\n")
        f.write(f"Toplam ürün sayısı: {len(df)}\n")
        f.write(f"Güncellenen ürün sayısı: {guncellenen_urun_sayisi}\n\n")

        if guncellenen_urun_sayisi > 0:
            f.write("GÜNCELLENEN ÜRÜNLER:\n")
            f.write("-" * 100 + "\n")
            f.write("{:<15} {:<40} {:<15} {:<15} {:<15}\n".format(
                "BARKOD", "ÜRÜN ADI", "MEVCUT FİYAT", "MAKSİMUM FİYAT", "FARK %"))
            f.write("-" * 100 + "\n")

            for urun in guncellenen_urunler:
                f.write("{:<15} {:<40} {:<15} {:<15} {:<15}\n".format(
                    urun['Barkod'],
                    urun['Ürün Adı'][:37] + "..." if len(urun['Ürün Adı']) > 40 else urun['Ürün Adı'],
                    f"{urun['Mevcut Fiyat']:.2f} TL",
                    f"{urun['Maksimum Fiyat']:.2f} TL",
                    f"%{urun['Fark Yüzdesi']:.2f}"
                ))

    renkli_yazdir(f"Detaylı rapor '{istatistik_dosyasi}' dosyasına kaydedildi.", Fore.GREEN)

except Exception as e:
    renkli_yazdir(f"Excel dosyası kaydedilirken hata oluştu: {e}", Fore.RED, True)