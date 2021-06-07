x = 25

if x == 25:
    print("Yes you right")
else:
    print("No you are wrong")

all_cars = ["chrusler", "dacia", "bmw", "KIA", "vw", "seat", "skoda", "lada", "audi", "ford", "Chevrolett"]
german_cars = ["bmw", "vw", "audi"]

#if "lada" in all_cars:
#    print("Yes LADA is in the list")
#else:
#    print("LADA Not in the list")

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is German Car")
    else:
        print(xxxx + " is not German car")
