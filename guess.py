secret_word = "Python"
hint = "Goi y: Day la ten cua mot loai ngon ngu lap trinh"
guess = ""
guess_count = 0
guess_limit = 3

print(hint)

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Ban doan day la tu gi?")
        guess_count += 1
    else:
        break
    #break la ham chan de khong cho doan nua  

if guess == secret_word:
    print("Ban da doan chinh xac!")
else:
    print("Thang loser")

