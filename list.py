teams = ["Team A", "Team B", "Team C"]
print(teams[-2])
print(teams)

#các hàm thao tác với list
student_names = ["Hùng, Yến, Diễm, Mạnh, Huy, Kiệt, Nhân"]
math_scores = [2, 10, 9, 8, 9, 6, 7]


student_names.extend(math_scores)
print(student_names)
#extend dùng để nối danh sách

student_names.append("Nam")
print(student_names)
#append dùng để thêm phần tử riêng lẻ vào cuối danh sách

 
#insert dùng để thêm vào các vị trị ở giữa 
#remove dùng để xóa phần tử 
#clear dùng để xóa toàn bộ danh sách 
#pop dùng xóa phần tử cuối cùng 
#index dùng để kiểm tra phần tử xem có phần tử nào đó không, khi đó vị trí của phần tử sẽ được hiển thị 
#count dùng đếm phần tử xuất hiện bao nhiêu lần 
#sort dùng để sắp xếp danh sách theo thứ tự tăng dần của bảng chữ cái và tăng dần của số
#reverse thứ tự sắp xếp ngược lại với sort  
#copy dùng sao chép biến 