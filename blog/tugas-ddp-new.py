# Nama : Fatah Muhammad Fikrudin
# NIM : 0110121162
# Kelas : SI08

def check():
	import re
	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	email = input("Masukkan email: ")
	if(re.fullmatch(regex, email)):
		print("Valid Email")
	else:
		print("Invalid Email, Try it again.")
		return check()
def validPass(password):
    chaeSept = ["!", "@", "#", "$"]
    if len(password) >= 8:
        if any(word.isnumeric() for word in password):
            if any(word.islower() for word in password):
                if any(word.isupper() for word in password):
                    if any(word in chaeSept for word in password):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

print("\n")
print("Fitur Belanja")

i = 0
j = 0
while True:
    print()
    a = str(input("Masukkan nama produk yang akan dibeli atau X untuk selesai: "))
    if a == "X" or a == "x" and i == 0:
        quit()
    if a == "X" or a == "x" and i != 0:
        print()
        print("Total produk yang dibeli: ", i)
        print("Harga produk yang dibeli: ", j)
        print("\n")
        break
    else:
        b = int(input("Masukkan harga produk: "))
        print("Berhasil menambahkan", a, "dengan harga", float(b))
        print()
        i += 1
        j += b
anggota = str(input("Apakah anda seorang anggota? (Y/T): "))
if anggota == "Y" or anggota == "y":
    check()
    password = input("Masukkan Password: ")
    while True:
        if validPass(password):
            print("Password Valid")
            break
        else:
            password = input("Password tidak valid, ulangi: ")
    level = input("Masukkan Level Kepesertaan Anda (Silver/Gold/Diamond): ")
    print("\n")
    while level != "Silver" and level != "Gold" and level != "Diamond":
        level = input ("Masukkan tidak valid, ulangi: ")
    else:
        if level == "Silver":
            if i < 5:
                diskon = j * (5/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 5%")
            else:
                diskon = j * (10/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
        elif level == "Gold":
            if i < 5:
                diskon = j * (10/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
            else:
                diskon = j * (15/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
        elif level == "Diamond":
            if i < 5:
                diskon = j * (15/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
            else:
                diskon = j * (20/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 20%")
        setelah_diskon = j - diskon
        print("Total Harga yang harus dibayar: ", float(setelah_diskon))
print()
print("Terimakasih sudah belanja di Toko Kami!")