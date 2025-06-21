template = "Fayl: {fayl_name}{fayl_turi}"

fayl_name = input("fayl_name: ")
fayl_turi = input("fayl_turi: ")

print(template.format(fayl_name=fayl_name, fayl_turi=fayl_turi))