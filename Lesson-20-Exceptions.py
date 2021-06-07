filename = "Lesson_List.txt"

try:
    print("Inside TRY")
    myfile = open(filename, mode = 'r', encoding ="utf_8")
except Exception:
    print("Inside Except")
    print("Error Found!")
else:
    print("Inside Else")
    print(myfile.read())
finally:
    print("Inside Finally")

print("===========EOF=============")