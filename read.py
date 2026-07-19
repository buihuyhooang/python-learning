# r chế độ chỉ đọc 
# w chế độ cho phép sửa
# a chế độ chỉ cho phép thêm vào cuối trang 

phone_book = open("phone_book.txt", "r")

for person in phone_book.readlines():
    person = person.replace("\n", "")
    print(person)

phone_book.close()
