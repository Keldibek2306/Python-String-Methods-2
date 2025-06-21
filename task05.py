template = "{son1} + {son2} = {natija}"

son1 = int(input("son1: "))
son2 = int(input("son2: "))

natija = son1 + son2
 
print(template.format(son1=son1, son2=son2, natija=natija))
