from functools import reduce

# Cú pháp và ví dụ về hàm nặc danh (lambda) trong Python

# Cú pháp cơ bản: lambda arguments: expression
square = lambda x: x**2
print(f"Bình phương của 5: {square(5)}")

# Hàm lambda với nhiều tham số
sum_two = lambda x, y: x + y
print(f"Tổng của 3 và 4: {sum_two(3, 4)}")

# Sử dụng lambda với các hàm có sẵn
numbers = [1, 5, 4, 3, 2, 6]

# Sắp xếp danh sách
sorted_numbers = sorted(numbers)
print(f"Danh sách đã sắp xếp: {sorted_numbers}")

# Sử dụng lambda với sorted() để sắp xếp theo giá trị tuyệt đối
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print(f"Danh sách sắp xếp theo giá trị tuyệt đối: {sorted_by_abs}")

# Sử dụng lambda với filter() để lọc số chẵn
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Các số chẵn: {even_numbers}")

# Sử dụng lambda với map() để áp dụng một hàm cho mỗi phần tử
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Bình phương các số: {squared_numbers}")

# Kết hợp lambda với reduce() từ functools
product = reduce(lambda x, y: x * y, numbers)
print(f"Tích của tất cả các số: {product}")

# Sử dụng lambda trong list comprehension (ít phổ biến)
result = [(lambda x: x * 2)(num) for num in numbers]
print(f"Gấp đôi các số: {result}")