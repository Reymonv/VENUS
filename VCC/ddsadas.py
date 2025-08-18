def linear_search(nilai, target):
    for i in range(len(nilai)):
        if nilai[i] == target:
            return i
    return -1

list_saya = ["Aston", "Budi", "Citra", "Dewi", "Eko", "Fani"]
cari = input("Masukkan nama yang ingin dicari: ")
if cari in list_saya:
    hasil = linear_search(list_saya, cari)
    print(f"Nama {cari} ditemukan di indeks {hasil}")
else:
    print(f"Nama {cari} tidak ditemukan dalam list.")