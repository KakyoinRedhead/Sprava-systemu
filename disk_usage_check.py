import shutil

# Práh využití disku (v procentech)
threshold = 80

# Kontrola využití disku
total, used, free = shutil.disk_usage("/")

used_percent = (used / total) * 100

if used_percent > threshold:
    print(f"Varování! Využití disku je {used_percent:.2f}% a přesáhlo prahovou hodnotu {threshold}%!")
else:
    print(f"Využití disku je v pořádku: {used_percent:.2f}%")
