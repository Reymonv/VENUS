try:
    ipk = float(input( "MASUKAN IPK: "))
    semester = int(input("MASUKAN SEMESTER: "))
    if ipk >= 3.0 or semester >= 2:
        print("Anda memenuhi syarat untuk mendapatkan beasiswa.")
    else :
        print("Anda tidak memenuhi syarat untuk mendapatkan beasiswa.")

except ValueError:
    print("Input tidak valid. Pastikan Anda memasukkan angka yang benar.")

    
