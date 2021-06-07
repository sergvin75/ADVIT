mystring = "Bla bla bla"
name = "vasya pupkin"
print(name.title())
print(name.upper())
print(name.lower())

print("Privet stroka nomer1\nPrivet stroka 2\n\nStroka 3")
print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEND")
print("Lower name:" + name.lower())
print("----------------------------\n\n")

a = ".... dadya vasya ...."
print(a)
print(a.rstrip())
print(a.lstrip())
print(a.strip())
print(a.strip("."))
a = a.strip(".")        #Udalenie tochek
a = a.strip()           #Udalenie probelov
print(a)