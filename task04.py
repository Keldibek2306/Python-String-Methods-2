template = "Bugun {hafta_kuni} kuni, dars soat {soat} da."

hafta_kuni = input("hafta_kuni: ")
soat = int(input("soat: "))

print(template.format(hafta_kuni=hafta_kuni, soat=soat))