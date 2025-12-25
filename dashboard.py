"""
SIGINT Hub - Tactical Dashboard (CLI)
Developer: Bahattin Yunus Çetin (IT Architect)
Location: Trabzon / Of
GitHub: https://github.com/bahattinyunus
"""
import os
import time
import random
import numpy as np

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_header():
    print("\033[1;32m" + "="*80)
    print(" " * 20 + "SIGINT TACTICAL COMMAND CENTER v2.0")
    print("="*80 + "\033[0m")
    print(f"OPERATOR: Bahattin Yunus Cetin | ROLE: IT Architect | STATUS: \033[1;32mONLINE\033[0m")
    print("-" * 80)

def draw_signal_monitor(width=80, height=10):
    print("\n[ SIGNAL MONITOR - SPECTRUM ACTIVITY ]")
    samples = random.sample(range(1, height), width // 2)
    for h in range(height, 0, -1):
        line = ""
        for s in samples:
            if s >= h:
                line += "█ "
            else:
                line += "  "
        print(f"\033[1;36m{line}\033[0m")
    print("-" * 80)

def draw_system_status():
    status_msg = [
        "SDR INITIALIZED...",
        "FFT ENGINE RUNNING",
        "ENCRYPTION KEY DETECTED - ANALYZING",
        "FM FREQUENCY SHIFT DETECTED @ 144.500 MHz",
        "ELINT PULSE ACQUIRED - PRI: 250ms"
    ]
    print("\n[ SYSTEM LOGS ]")
    for msg in status_msg[-5:]:
        print(f"[\033[1;33m{time.strftime('%H:%M:%S')}\033[0m] {msg}")

def main():
    try:
        for _ in range(5): # Simülasyon döngüsü
            clear_screen()
            draw_header()
            draw_signal_monitor()
            draw_system_status()
            print("\n\033[1;31mCTRL+C TO EXIT MISSION\033[0m")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMISSION TERMINATED.")

if __name__ == "__main__":
    main()
