
# Ví dụ khác về truyền tham chiếu
def modify_dict(my_dict):
    """Thay đổi dictionary đã truyền cho hàm"""
    my_dict['new_key'] = 'new_value'
    print("Giá trị dictionary trong hàm:", my_dict)
    return

# Gọi hàm modify_dict
my_dict = {'name': 'Python', 'version': 3.9}
print("Trước khi gọi hàm:", my_dict)
modify_dict(my_dict)
print("Sau khi gọi hàm:", my_dict)