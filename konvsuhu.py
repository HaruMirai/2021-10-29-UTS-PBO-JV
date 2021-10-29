jenis = input("Masukkan jenis suhu (celcius/fahrenheit/reamur)= ")
suhu = int(input("Masukkan suhu= "))

if jenis == "celcius":
    fahrenheit = (suhu * 9/5) + 32
    reamur = 4/5 * suhu
    print("Suhu Fahrenheit=", fahrenheit)
    print("Suhu Reamur=", reamur)
elif jenis == "fahrenheit":
    celcius = 5/9 * (suhu - 32)
    reamur = 4/9 * (suhu - 32)
    print("Suhu Celcius=", celcius)
    print("Suhu Reamur=", reamur) 
elif jenis == "reamur":
    fahrenheit = (9/4 * suhu) + 32
    celcius = 5/4 * suhu
    print("Suhu Celcius=", celcius)
    print("Suhu Fahrenheit=", fahrenheit) 
else:
    print("Input jenis suhu salah!")