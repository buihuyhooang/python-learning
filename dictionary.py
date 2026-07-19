#Dictionary - Tu dien

english_vietnamese_dictionary = {
    "hello": "xin chào",
    "morning": "buổi sáng",
    "tea": "trà",
    0: "bia",
    1: "chao",
    2: "com",    
}

print(english_vietnamese_dictionary["hello"])
print(english_vietnamese_dictionary.get("hello"))
print(english_vietnamese_dictionary.get("cat", "Tu khoa nay khong ton tai!!!"))