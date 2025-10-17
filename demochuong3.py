def function_name(parameter1, parameter2=default_value, *args, **kwargs):
    """
    This is a docstring: used to explain what the function does,
    what parameters it takes, and what it returns.
    """
    # Function body - code that gets executed when the function is called
    # You can perform operations here
    
    # Optional: return statement
    return result

    def ten_ham(tham_so1, tham_so2, tham_so_mac_dinh=123):
        """
        Đây là docstring: dùng để giải thích hàm làm gì,
        nhận các tham số nào, và trả về giá trị gì.
        """
        # Thân hàm - code được thực thi khi hàm được gọi
        ket_qua = tham_so1 + tham_so2
        
        # Trả về kết quả (tùy chọn)
        return ket_qua

    # Ví dụ gọi hàm
    ket_qua = ten_ham(5, 10)
    print(f"Kết quả: {ket_qua}")

    # Hàm không có giá trị trả về
    def chao_hoi(ten):
        print(f"Xin chào {ten}!")
        # Không có return, mặc định trả về None

    chao_hoi("Nguyễn Văn A")