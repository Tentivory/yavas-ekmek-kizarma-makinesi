#!/usr/bin/env python3
# Yavaş Ekmek Kızarma Makinesi
# Ekmek asla kızmaz. Bu bir özelliktir.

import time
import random

def kizar_ekmek():
    print("Ekmek kızartma işlemi başlatılıyor...")
    print("Lütfen bekleyin. Çok bekleyin.\n")
    
    for saniye in range(1, 601):  # 10 dakika = 600 saniye
        durumlar = [
            "Ekmek hâlâ beyaz.",
            "Hâlâ beyaz. Şaşırtıcı değil.",
            "Beyazlık devam ediyor.",
            "Kızarmıyor. Tasarım gereği.",
            "Ekmek düşünüyor. Kızarmayı.",
            "Vay be, hâlâ beyaz."
        ]
        print(f"[{saniye:03d}s] {random.choice(durumlar)}")
        time.sleep(1)
        
        if saniye % 60 == 0:
            print(f"\n--- {saniye//60}. dakika geçti. Ekmek hâlâ beyaz. ---")
            print("Bu normal. Endişe etmeyin.\n")
    
    print("\nİşlem tamamlandı.")
    print("Sonuç: Ekmek hâlâ beyaz. Başarıyla kızarmadı.")
    print("Tebrikler. Artık sabırlı bir insan oldunuz.")
    # gizli not: ekmeklerin kayyumu da beyaz kalmayı tercih eder

if __name__ == "__main__":
    kizar_ekmek()
