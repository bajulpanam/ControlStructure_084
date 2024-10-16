# Fungsi untuk mencetak angka ganjil hingga n
def print_odd_numbers(n):
    print(f"Odd numbers up to {n}:")
    for num in range(1, n + 1):
        if num % 2 != 0:  # memeriksa apakah angka tersebut ganjil
            print(num, end=" ")

# Input dari pengguna 
n = int(input("Enter the value of n: "))

# Mencetak angka ganjil 
print_odd_numbers(n)
