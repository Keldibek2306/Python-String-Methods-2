template = "Salom, mening ismim {name} va yoshim {age}."

name = input("name: ")
age = int(input("age: "))

print(template.format(name = name, age = age))
