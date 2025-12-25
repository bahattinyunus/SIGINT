"""
SIGINT Hub - FFT Analyzer
Developer: Bahattin Yunus Çetin (IT Architect)
Location: Trabzon / Of
GitHub: https://github.com/bahattinyunus
"""
import numpy as np

def perform_fft(signal, sampling_rate):
    """
    Sinyal üzerinde Hızlı Fourier Dönüşümü (FFT) gerçekleştirir.
    """
    n = len(signal)
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n, 1/sampling_rate)
    
    # Sadece pozitif frekansları al
    positive_freqs = freqs[:n//2]
    magnitude = np.abs(fft_result[:n//2]) * 2 / n
    
    return positive_freqs, magnitude

if __name__ == "__main__":
    from generator import generate_signal
    
    FS = 1000.0
    t, signal = generate_signal(50.0, 1.0, FS) # 50 Hz sinyal
    
    freqs, mag = perform_fft(signal, FS)
    
    # En yüksek frekansı bul (Tepe Tespiti)
    peak_idx = np.argmax(mag)
    peak_freq = freqs[peak_idx]
    
    print(f"ANALİZ SONUCU:")
    print(f"----------------")
    print(f"Tespit Edilen Taşıyıcı Frekans: {peak_freq:.2f} Hz")
    print(f"Sinyal Genliği: {mag[peak_idx]:.2f}")
