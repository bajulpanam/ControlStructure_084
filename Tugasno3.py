# Fungsi untuk menghasilkan deret Fibonacci hingga n
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# Input dari pengguna
n = int(input("Enter the value of n: "))

# Mencetak deret bonacci
print(f"Fibonacci series up to {n}:")
fibonacci(n)
