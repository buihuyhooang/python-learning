def translate(text):
    translation = ""
    for character in text:
        if character.lower() in "áàảãạ":
            if character.isupper():
                translation = translation + "A"
            else:
                translation = translation + "a"
        else: 
            translation = translation + character 
    
    return translation

text = input("Nhap vao van ban ma ban muon dich: ")
print(translate(text))