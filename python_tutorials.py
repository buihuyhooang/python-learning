#cac_toan_tu_logic
a = 500
b = 100
c = 300
#toan tu and va or
if a > b and a > c:
    print("a la so lon nhat")
#chi tra gia tri khi ca hai deu dung
if (a == b) or (a == c):
    print("co it nhat mot so bang voi gia tri cua a")
#chi khong tra gia tri khi ca hai deu sai
a = True 
print(not a)
#dung dao nguoc ket qua diu kien trong if
d = 100 
e = 200
if not a > b: 
    print("a KHONG lon hon b")
#a nho hon b nen ke qua la sai nhung do dung ham not nentra ve ket qua nguoc lai tuc la true ne print thoa man