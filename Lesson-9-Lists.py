cars = ['bmw', 'vw', 'seat', 'skoda', 'kada']

for x in cars:
    print(x.upper())

for x in range(1, 6):
    print(x)

mynuber_list = list(range(0,10))
print(mynuber_list)
print("--------------------------------------")

for x in mynuber_list:
    x = x*2
    print(x)
mynuber_list.sort(reverse=True)
print(mynuber_list)

print(max(mynuber_list))
print("Max number is:" + str(max(mynuber_list)))
print("--------------------------------------")
cars = ['bmw', 'vw', 'seat', 'skoda', 'kada']

mycars = cars[1:3]
print(mycars)
mycars = cars[:4]
print(mycars)
mycars = cars[:]            #eto kopia nezavisimogo massiva



