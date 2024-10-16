# Fungsi untuk mencetak pola
def print_pattern(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

# Input dari pengguna
try:
    n = int(input("Enter a value for n: "))
    
    # Memeriksa apakah input adalah bilangan bulat positif
    if n <= 0:
        print("Please enter a positive integer greater than zero.")
    else:
        print_pattern(n)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
