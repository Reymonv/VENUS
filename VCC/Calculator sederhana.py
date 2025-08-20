nilai_a = int(input("MASUKAN NILAI A: "))
nilai_b = int(input("MASUKAN NILAI B: "))
operasi = input("MASUKAN OPERASI (+, -, *, /): ")

# Program Kalkulator Sederhana
if operasi == "+":
    print(f"Hasil dari {nilai_a} + {nilai_b} = {nilai_a + nilai_b}")
elif operasi == "-":
    print(f"Hasil {nilai_a} - {nilai_b} = {nilai_a - nilai_b}")
elif operasi == "*":
    print(f"Hasil {nilai_a} * {nilai_b} = {nilai_a * nilai_b}")
elif operasi == "/":
    if nilai_b != 0:
        print(f"Hasil {nilai_a} / {nilai_b} = {nilai_a / nilai_b}")
    else:
        print("Pembagian dengan nol tidak diperbolehkan.")
else :
    print("Operasi tidak dikenali.")
