"""
SIGINT Hub - Komple Örnek Kullanım
Developer: Bahattin Yunus Çetin (IT Architect)
Location: Trabzon / Of
GitHub: https://github.com/bahattinyunus

Bu script, SIGINT Hub'ın tüm özelliklerini gösteren kapsamlı bir örnektir.
"""

import numpy as np
import sys
import os

# Simülasyon modüllerini içe aktar
sys.path.append(os.path.join(os.path.dirname(__file__), 'simulations'))

from generator import generate_signal
from analyzer import perform_fft
from modulator import am_modulate, fm_modulate, bpsk_modulate, generate_baseband

def main():
    print("="*80)
    print(" " * 25 + "SIGINT HUB - KOMPLE DEMO")
    print("="*80)
    
    # 1. Sinyal Üretimi
    print("\n[1/4] Sinyal Üretimi...")
    FS = 2000.0
    DURATION = 1.0
    t, clean_signal = generate_signal(100.0, DURATION, FS, noise_level=0.05)
    print(f"✓ {len(t)} örnekli sinyal oluşturuldu.")
    
    # 2. FFT Analizi
    print("\n[2/4] FFT Analizi...")
    freqs, mag = perform_fft(clean_signal, FS)
    peak_idx = np.argmax(mag)
    peak_freq = freqs[peak_idx]
    print(f"✓ Tespit Edilen Frekans: {peak_freq:.2f} Hz")
    print(f"✓ Sinyal Gücü: {mag[peak_idx]:.2f}")
    
    # 3. Modülasyon Demosu
    print("\n[3/4] Modülasyon Simülasyonları...")
    t_mod, message = generate_baseband(DURATION, FS, freq=5.0)
    
    am_sig = am_modulate(t_mod, message, fc=200.0)
    print("✓ AM Modülasyonu tamamlandı.")
    
    fm_sig = fm_modulate(t_mod, message, fc=200.0, kf=50.0)
    print("✓ FM Modülasyonu tamamlandı.")
    
    bits = np.array([1, 0, 1, 1, 0, 0, 1, 0])
    bpsk_sig = bpsk_modulate(t_mod, bits, fc=200.0)
    print(f"✓ BPSK Modülasyonu tamamlandı (Bits: {bits}).")
    
    # 4. Sonuç Raporu
    print("\n[4/4] Operasyon Raporu")
    print("-"*80)
    print(f"Toplam İşlenen Sinyal Sayısı: 4")
    print(f"Tespit Edilen Taşıyıcı Frekans: {peak_freq:.2f} Hz")
    print(f"Modülasyon Teknikleri: AM, FM, BPSK")
    print(f"Operasyon Durumu: BAŞARILI ✓")
    print("="*80)
    print("\nTaktik dashboard için: python dashboard.py")

if __name__ == "__main__":
    main()
