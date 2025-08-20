def konversi_suhu(celcius):
    fahrenheit = (celcius * 9/5) + 32
    reamur = celcius * 4/5
    kelvin = celcius + 273.15
    return fahrenheit, reamur, kelvin

suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))
f, r, k = konversi_suhu(suhu_celcius)

print(f"Suhu dalam Fahrenheit: {f:.2f}°F")
print(f"Suhu dalam Reamur: {r:.2f}°R")
print(f"Suhu dalam Kelvin: {k:.2f}K")

