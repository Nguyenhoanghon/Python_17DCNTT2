# Hàm đếm chữ số chẵn và lẻ
def dem_chan_le(n):
    chan = 0
    le = 0
    while n > 0:
        chu_so = n % 10
        if chu_so % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10
    return chan, le


# --- Chương trình chính ---
n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    so_chan, so_le = dem_chan_le(n)
    print(f"Số {n} có {so_chan} chữ số chẵn và {so_le} chữ số lẻ.")
