try:
    angka = int(input("Masukkan angka: "))
    pembagi = int(input("Masukkan pembagi: "))
    hasil = angka / pembagi
    print(f"Hasil pembagian: {hasil}")
except ValueError:
    print("Input harus berupa angka!")
except ZeroDivisionError:
    print("Pembagi tidak boleh nol!")