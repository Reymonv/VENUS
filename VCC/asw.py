def list_angka(nilai, target):
    for i in range(len(nilai)):
        if nilai[i] == target:
            return i
    return -1

list_saya = [4, 5, 2, 9, 1, 6, 3, 8, 7]
cari = int(input("Masukkan angka yang ingin dicari: "))
if cari in list_saya:
    hasil = list_angka(list_saya, cari)
    print(f"Angka {cari} ditemukan di indeks {hasil}")
else:
    print(f"Angka {cari} tidak ditemukan dalam list.")

