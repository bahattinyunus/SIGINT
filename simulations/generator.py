import numpy as np
import matplotlib.pyplot as plt

def generate_signal(frequency, duration, sampling_rate, noise_level=0.1):
    """
    Simüle edilmiş bir sinyal oluşturur (Sinüs dalgası + Gürültü).
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    noise = np.random.normal(0, noise_level, signal.shape)
    return t, signal + noise

if __name__ == "__main__":
    # Parametreler
    FREQ = 10.0  # 10 Hz
    DURATION = 1.0  # 1 saniye
    SAMPLING_RATE = 1000.0  # 1 kHz
    
    t, signal = generate_signal(FREQ, DURATION, SAMPLING_RATE)
    print(f"Sinyal Oluşturuldu: {FREQ} Hz, {SAMPLING_RATE} Hz örnekleme hızı.")
    
    # Basit bir çıktı (CSV olarak kaydedilebilir)
    with open("assets/signal_sample.txt", "w") as f:
        f.write("Time,Amplitude\n")
        for i in range(100): # İlk 100 örnek
            f.write(f"{t[i]:.4f},{signal[i]:.4f}\n")
    print("Sinyal verisi 'assets/signal_sample.txt' dosyasına kaydedildi.")
