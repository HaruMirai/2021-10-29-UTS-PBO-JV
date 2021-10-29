detik = int(input("Masukkan detik= "))

jam = detik / 3600
sisa1 = detik % 3600
menit = sisa1 / 60
dtk = sisa1 % 60

print(jam, "H", " ", menit, "m"," ", dtk, "s")

