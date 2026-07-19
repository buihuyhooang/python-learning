#ung dung may tinh
num01 = input("So thu nhat: ")
num02 = input("So thu hai: ")
sum = float(num01) + float(num02)
print(sum)

#int là viết tắt của integer, nó giúp mình chuyển đổi chuỗi sang số nguyên.
#float là viết tắt của floating point, nó giúp mình chuyển đổi chuỗi sang số thực.

#cai tien ung dung may tinh 
num1 = float(input("Nhap so thu nhat: "))
num2 = float(input("Nhap so thu hai:"))
operator = input("Nhap vao toan tu: ")

if (operator == "+"):
    print(num1 + num2)
elif (operator == "-"):
    print(num1 - num2)
elif (operator == "*"):
    print(num1 * num2)
elif (operator == "/"):
    print(num1 / num2)
else: 
    print("Toan tu khong hop le!!!")







