
def ten_ham(tham_so1, tham_so2, tham_so_mac_dinh=20):
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

# Python truyền tham số theo "tham chiếu đối tượng":
# - Kiểu bất biến (int, str, tuple): trông như "truyền bởi giá trị" vì không thể sửa tại chỗ.
# - Kiểu có thể biến đổi (list, dict, set): chỉnh sửa tại chỗ sẽ phản ánh ra ngoài.

# 1) Bất biến: giống truyền bởi giá trị (không ảnh hưởng biến bên ngoài)
def tang_so(n):
    # n là biến cục bộ mới trỏ tới giá trị khác
    n += 1
    print(f"Trong hàm tang_so, n = {n}")

so_ban_dau = 10
tang_so(so_ban_dau)
print(f"Ngoài hàm, so_ban_dau vẫn = {so_ban_dau}")

# 2) Có thể biến đổi: chỉnh sửa tại chỗ (giống truyền bởi tham chiếu)
def them_phan_tu(ds):
    # Thao tác tại chỗ làm thay đổi cùng một đối tượng list
    ds.append(99)
    print(f"Trong hàm them_phan_tu, ds = {ds}")

danh_sach = [1, 2]
them_phan_tu(danh_sach)
print(f"Ngoài hàm, danh_sach = {danh_sach}")

# 3) Gán lại tham số bên trong hàm KHÔNG ảnh hưởng biến ngoài
def gan_lai_danh_sach(ds):
    ds = ["moi"]  # trỏ tới đối tượng list khác
    print(f"Trong hàm gan_lai_danh_sach, ds (mới) = {ds}")

gan_lai_danh_sach(danh_sach)
print(f"Sau gan_lai_danh_sach, danh_sach ngoài vẫn = {danh_sach}")

# 4) Tránh bị thay đổi: truyền bản sao (shallow copy)
def them_an_toan(ds):
    ban_sao = ds.copy()
    ban_sao.append("X")
    return ban_sao

ban_sao = them_an_toan(danh_sach)
print(f"ban_sao sau khi thêm = {ban_sao}")
print(f"danh_sach gốc vẫn = {danh_sach}")

# 5) Mô phỏng 'truyền bởi tham chiếu' cho giá trị bất biến bằng wrapper (dict/list)
def tang_trong_hop(hop):
    hop["gia_tri"] += 1  # sửa tại chỗ bên trong container

hop = {"gia_tri": 5}
tang_trong_hop(hop)
print(f"Giá trị trong hop sau khi tăng = {hop['gia_tri']}")