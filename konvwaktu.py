detik = int(input("Masukkan detik= "))

hari = detik / 86400
sisa1 = detik % 86400
jam = sisa1 / 3600
sisa2 = detik % 3600
menit = sisa2 / 60
dtk = sisa1 % 60

print(hari, "D", " " ,jam, "H", " ", menit, "m"," ", dtk, "s")

