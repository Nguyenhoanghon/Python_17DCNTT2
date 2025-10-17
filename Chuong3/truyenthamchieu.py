
# Ví dụ khác về truyền tham chiếu
def changeme( songuyen ):
    songuyen = songuyen + 100
    print ("Gia tri ben trong ham la: ", songuyen)
    biencucbo = 200
    return
# Bay gio ban co the goi ham changeme function
songuyen = 50
changeme()
print ("Gia tri ben ngoai ham la: ", songuyen)
