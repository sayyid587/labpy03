import random

# Meminta input dari pengguna untuk nilai N
n = int(input("Masukkan nilai N: "))

# Inisialisasi counter
i = 1

# Menggunakan while loop untuk menghasilkan dan menampilkan n bilangan acak
while i <= n:
    # Menghasilkan bilangan acak
    angka_acak = random.random()
    
    # Memastikan bilangan acak lebih kecil dari 0.5
    if angka_acak < 0.5:
        print(f"data ke: {i} => {angka_acak}")
        i += 1

print("Selesai")
