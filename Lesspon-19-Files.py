inputfile = "use_names.txt"

myfile = open(inputfile, mode="r+", encoding ="utf_8")  #"utf_8"
#for line in myfile:
#    print("Hello " + line.strip())

for num, line in enumerate(myfile, 1):
    if "Davidson" in line:
       print("Line №: " + str(num) + " : " + line.strip())

myfile.close()