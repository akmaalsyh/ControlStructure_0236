def performa_siswa(persentase):
    if persentase >= 90:
        return "Excellent"
    elif persentase >= 80:
        return "Very Good"
    elif persentase >= 70:
        return "Good"
    elif persentase >= 60:
        return "Average"
    else:
        return "Needs improvement"
persentase = float(input("Masukkan persentase: "))
print(performa_siswa(persentase))

def angka_terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >=a and b >= c:
        return b
    else:
        return c
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))
print("Angka terbesarnya adalah:", angka_terbesar(a, b, c))

def fibonacci(n):
    deret_fib = [0, 1]
    for i in range (2, n):
        nomor_selanjutnya = deret_fib[i-1] + deret_fib[i-2]
        deret_fib.append(nomor_selanjutnya)
    return deret_fib[:n]
n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin dicetak: "))
print("Deret Fibonacci hingga ke-(n) adalah: ", fibonacci(n))

def bilangan_ganjil(n):
    for i in range (1, n+1, 2):
        print (i, end=" ")
n = int(input("Masukkan batas atas untuk bilangan ganjil: "))
bilangan_ganjil(n)

def pola_segitiga(n):
    for i in range(1, n+1):
        print((str(i) + " " ) *i)
n = int(input("Masukkan nilai n untuk pola segitiga: "))
pola_segitiga(n)
