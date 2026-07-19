print(4)
print(3+4)
print(2*(3+4))

#Phép toán chia lấy phần dư 
print(10 % 3)

number = 10 
print(str(number) + " là số chẵn")

#abs là Absolute trị tuyệt đối 
print(abs(-5))

#pow là phép tính lũy thừa 
print(pow(2, 3))    

#max và min để tìm giá trị lớn nhất và nhỏ nhất
print(max(4, 7, 19))
print(min(4, 7))

#round là làm tròn số
print(round(3.14))
print(round(3.8))

#import math là hàm toán học mã nguồn bên ngoài

number = 2.3
print(round(number))

import math

number = 2.3
print(math.ceil(number)) #làm tròn lên
number = 36
print(math.sqrt(number)) #tính căn bậc 2

#thư viện math có nhiều hàm toán học khác nhau, ví dụ như sin, cos, tan, log, exp, v.v. Bạn có thể sử dụng chúng bằng cách gọi math.<tên_hàm>(<tham_số>).
#cac thao tac voi string
print("Tờ mờ sáng học lập trình Python")

print("Tờ mờ sáng \nhọc lập trình Python")

print("Tờ mờ sáng \n\"học lập trình Python\"")

print("Tờ mờ sáng \"học lập trình Python\"")

channel_name = "Tờ mờ sáng học lập trình Python"
print(channel_name + " dễ hiểu quá!")

print(channel_name.isupper())

print(channel_name.upper().isupper())

channel_name = "Tờ mờ sáng học lập trình Python"
print(channel_name[1])
print(channel_name.index("s"))
#index cho biết vị trí của chữ cái mình tìm kiếm trên dòng 
#\n trong đó n là viết tắt của newline 
print(channel_name.replace("Tờ mờ sáng học lập trình Python", "Kênh học lập trình Python"))
#replace là thay thế 
