"""
SIGINT Hub - Spectrogram Visualizer
Developer: Bahattin Yunus Çetin (IT Architect)
Location: Trabzon / Of
GitHub: https://github.com/bahattinyunus
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_spectrogram(signal, fs, window_size=256, noverlap=128):
    """Sinyal için spektrogram verisi oluşturur."""
    # plot.specgram returns (spectrum, freqs, times, im)
    Sxx, f, st, im = plt.specgram(signal, NFFT=window_size, Fs=fs, noverlap=noverlap)
    return f, st, Sxx

if __name__ == "__main__":
    # Örnek sinyal: Frekans kayması (LFM - Linear Frequency Modulation)
    fs = 2000.0
    duration = 2.0
    t = np.linspace(0, duration, int(fs * duration))
    # 50 Hz'den 500 Hz'e yükselen sinyal
    signal = np.sin(2 * np.pi * (50 + 225 * t) * t)
    
    f, st, Sxx = generate_spectrogram(signal, fs)
    
    print("Spektrogram Analizi Tamamlandı.")
    print(f"Frekans Aralığı: {f.min():.1f} - {f.max():.1f} Hz")
    print(f"Zaman Aralığı: {st.min():.1f} - {st.max():.1f} s")
    
    # ASCII Temelli Görselleştirme (Basit)
    # Gerçek bir görselleştirme için dashboard.py kullanılacak
    print("\n[SPEKTROGRAM ÖNİZLEME]")
    rows, cols = Sxx.shape
    for i in range(min(10, rows)):
        row_str = ""
        for j in range(min(20, cols)):
            if Sxx[i, j] > np.max(Sxx) * 0.1:
                row_str += "#"
            else:
                row_str += "."
        print(row_str)
