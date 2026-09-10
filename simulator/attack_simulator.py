import os
import time

print("=" * 60)
print("AI Malware Analyzer - Attack Simulator")
print("=" * 60)

print("\nSimulating Suspicious Activity...\n")

# Simulate CPU spike
while True:

    for i in range(10000000):
        x = i * i

    print("[SIMULATION] High CPU activity generated")

    time.sleep(1)