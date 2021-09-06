# Tampilkan menu
print()
print("--Program Konversi Suhu--")
print("1. Celcius \t=> Fahrenheit")
print("2. Celcius \t=> Kelvin")
print("3. Celcius \t=> Reamur")
print("4. Fahrenheit \t=> Celcius")
print("5. Fahrenheit \t=> Kelvin")
print("6. Fahrenheit \t=> Reamur")
print("7. Kelvin \t=> Celcius")
print("8. Kelvin \t=> Fahrenheit")
print("9. Kelvin \t=> Reamur")
print("10.Reamur \t=> Celcius")
print("11.Reamur \t=> Fahrenheit")
print("12.Reamur \t=> Kelvin")
print()

# Terima pilihan user tipe data string

pilihan = input("silahkan pilih menu diatas: ")

# Buat kondisi berdasarkan pilihan user
if pilihan == "1":
    nilaiAwal = int(input("Masukkan nilai celcius: "))
    nilaiAkhir = (nilaiAwal * 9/5) + 32
    print(nilaiAkhir, "F")
elif pilihan == "2":
    nilaiAwal = int(input("Masukkan nilai celcius: "))
    nilaiAkhir = (nilaiAwal * 1/273) 
    print(nilaiAkhir, "K")
elif pilihan == "3":
    nilaiAwal = int(input("Masukkan nilai celcius: "))
    nilaiAkhir = (nilaiAwal * 5/4)
    print(nilaiAkhir, "R")
elif pilihan == "4":
    nilaiAwal = int(input("Masukkan nilai Fahrenheit: "))
    nilaiAkhir = (nilaiAwal * 5/9) - 32
    print(nilaiAkhir, "C")
elif pilihan == "5":
    nilaiAwal = int(input("Masukkan nilai Fahrenheit: "))
    nilaiAkhir = (nilaiAwal - 32) * 5/9 + 273
    print(nilaiAkhir,"K")
elif pilihan == "6":
    nilaiAwal = int(input("Masukkan nilai Fahrenheit: "))
    nilaiAkhir = (nilaiAwal * 4/9) - 32
    print(nilaiAkhir, "R")
elif pilihan == "7":
    nilaiAwal = int(input("Masukkan nilai Kelvin: "))
    nilaiAkhir = (nilaiAwal - 273) 
    print(nilaiAkhir, "C")
elif pilihan == "8":
    nilaiAwal = int(input("Masukkan nilai Kelvin: "))
    nilaiAkhir = (nilaiAwal * 9/5) - 237 + 32
    print(nilaiAkhir, "F")
elif pilihan == "9":
    nilaiAwal = int(input("Masukkan nilai Kelvin: "))
    nilaiAkhir = (nilaiAwal * 4/5) - 273
    print(nilaiAkhir, "R")
elif pilihan == "10":
    nilaiAwal = int(input("Masukkan nilai Reamur: "))
    nilaiAkhir = (nilaiAwal * 5/4)
    print(nilaiAkhir, "C")
elif pilihan == "11":
    nilaiAwal = int(input("Masukkan nilai Reamur: "))
    nilaiAkhir = (nilaiAwal * 9/4) + 32
    print(nilaiAkhir, "F")
elif pilihan == "12":
    nilaiAwal = int(input("Masukkan nilai Reamur: "))
    nilaiAkhir = (nilaiAwal * 5/4) + 273
    print(nilaiAkhir, "K")

