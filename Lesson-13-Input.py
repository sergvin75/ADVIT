#name = input('Please enter Your name:')

#print(name)

#num1 = input("Enter X:")
#num2 = input("Enter Y:")

#suma = int(num1) + int(num2)
#print(suma)
#message = ''

#while True:
#    message = input("Enter Password ")
#    if  message == 'sekret':
#        break
#    print(message + "Password Not Correct")
#print("Password was:" + message)

mylist = []

msg = ''

while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish ")
    mylist.append(msg)

print(mylist)

