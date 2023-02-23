# Membuat Kalkulator Sederhana Menggunakan Python
def awal():
    print("KALKULATOR SEDERHANA")
    print(22*"=")
    print("\t1. Penjumlahan")
    print("\t2. Pengurangan")
    print("\t3. Perkalian")
    print("\t4. Pembagian")
    print("\t5. Modulus")
    print("\t6. Pangkat")
    print(22*"=")
awal()
pilihan = input("SILAHKAN PILIH OPERATOR MATEMATIKA = ")

while pilihan not in ('1', '2', '3', '4','5','6'):
    print("MASUKAN DENGAN BENAR,SILAHKAN COBA LAGI")
    pilihan = input("SILAHKAN PILIH OPERATOR MATEMATIKA = ")

nilaiA = int(input("Masukan Nilai A = "))
nilaiB = int(input("Masukan Nilai B = "))

if pilihan == "1":
    print("OPERATOR PENJUMLAHAN")
    hasil = nilaiA + nilaiB
    print(nilaiA," + ",nilaiB, " = ", hasil)
elif pilihan == "2":
        print("OPERATOR PENGURANGAN")
        hasil = nilaiA - nilaiB
        print(nilaiA, " - ", nilaiB, " = ", hasil)
elif pilihan == "3":
        print("OPERATOR PERKALIAN")
        hasil = nilaiA * nilaiB
        print(nilaiA, " * ", nilaiB, " = ", hasil)
elif pilihan == "4":
        print("OPERATOR PEMBAGIAN")
        hasil = nilaiA / nilaiB
        print(nilaiA, " / ", nilaiB, " = ", hasil)
elif pilihan == "5":
        print("OPERATOR MODULUS")
        hasil = nilaiA % nilaiB
        print(nilaiA, " mudulus ", nilaiB, " = ", hasil)
elif pilihan == "6":
        print("OPERATOR PANGKAT")
        hasil = nilaiA ** nilaiB
        print(nilaiA, " pangkat ", nilaiB, " = ", hasil)
else:
    print("Input yang di masukkan salah")