nilai_a = int(input("MASUKAN NILAI A: "))
nilai_b = int(input("MASUKAN NILAI B: "))
operasi = input("MASUKAN OPERASI (+, -, *,): ")
hasil = nilai_a + nilai_b 
if operasi == "+":
    print(f"Hasil dari {nilai_a} + {nilai_b} = {nilai_a + nilai_b}")
elif operasi == "-":
    print(f"Hasil {nilai_a} - {nilai_b} = {nilai_a - nilai_b}")
elif operasi == "*":
    print(f"Hasil {nilai_a} * {nilai_b} = {nilai_a * nilai_b}")
else :
    print("Operasi tidak dikenali.")