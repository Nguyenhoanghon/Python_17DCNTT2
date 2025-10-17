# Cú pháp khai báo hàm với số lượng tham số thay đổi trong Python
# Có hai cách:
# 1. Sử dụng *args - cho phép truyền nhiều tham số vị trí
# 2. Sử dụng **kwargs - cho phép truyền nhiều tham số có tên

# Ví dụ 1: Sử dụng *args để nhận nhiều tham số vị trí
pri
def tinh_tong_so(*args):
    """Hàm tính tổng các số được truyền vào."""
    tong = 0
    for so in args:
        tong += so
    return tong

# Sử dụng hàm với số lượng tham số khác nhau
print("Tổng của 1, 2:", tinh_tong_so(1, 2))
print("Tổng của 1, 2, 3, 4, 5:", tinh_tong_so(1, 2, 3, 4, 5))
print("Không có tham số:", tinh_tong_so())

# Ví dụ 2: Sử dụng **kwargs để nhận nhiều tham số có tên
def thong_tin_sinh_vien(**kwargs):
    """Hàm hiển thị thông tin sinh viên."""
    for ten, gia_tri in kwargs.items():
        print(f"{ten}: {gia_tri}")

# Sử dụng hàm với các tham số có tên
print("\nThông tin sinh viên 1:")
thong_tin_sinh_vien(ho_ten="Nguyễn Văn A", tuoi=20, lop="17DCNTT2")

print("\nThông tin sinh viên 2:")
thong_tin_sinh_vien(ho_ten="Trần Thị B", tuoi=21, lop="17DCNTT2", diem_tb=8.5)

# Ví dụ 3: Kết hợp tham số bắt buộc, *args và **kwargs
def thong_tin_khoa_hoc(ten_khoa_hoc, *hoc_sinh, **thong_tin_khac):
    """Hàm hiển thị thông tin khóa học."""
    print(f"Tên khóa học: {ten_khoa_hoc}")
    
    print("Danh sách học sinh:")
    for hoc_sinh in hoc_sinh:
        print(f"- {hoc_sinh}")
    
    print("Thông tin khác:")
    for ten, gia_tri in thong_tin_khac.items():
        print(f"- {ten}: {gia_tri}")

# Sử dụng hàm kết hợp
print("\nThông tin khóa học Python:")
thong_tin_khoa_hoc("Python cơ bản", 
                   "Nguyễn Văn A", "Trần Thị B", "Lê Văn C",
                   thoi_gian="3 tháng", hoc_phi=5000000, dia_diem="Online")