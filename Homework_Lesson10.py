#Bài 1-2
# Dictionary ban đầu từ 1 đến 1

# numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
#            'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}

# # Dictionary từ 11 đến 20
# numbers_2 = {'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
#              'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}

# # Cập nhật numbers bằng cách thêm các cặp key-value từ numbers_2
# numbers.update(numbers_2)

# # Yêu cầu người dùng nhập số La Mã
# user_input = input("Nhập số La Mã (I đến XX): ")

# # Kiểm tra nếu số La Mã có trong dictionary
# if user_input in numbers:
#     arabic_number = numbers[user_input]
#     print(f"Số Ả Rập tương ứng là: {arabic_number}")
# else:
#     print("Không tìm thấy số La Mã trong từ điển.")

#Bài 3

# number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
#                'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

# # Chuyển list thành dictionary tương tự như 'numbers'
# numbers = {numeral: i + 1 for i, numeral in enumerate(number_list)}

# # Yêu cầu người dùng nhập số La Mã
# user_input = input("Nhập số La Mã (I đến XX): ")

# # Kiểm tra nếu số La Mã có trong dictionary
# if user_input in numbers:
#     arabic_number = numbers[user_input]
#     print(f"Số Ả Rập tương ứng là: {arabic_number}")
# else:
#     print("Not found")

# #Bài 4
# students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
#             {'firstName': 'Mervin', 'lastName': 'Friedland'},
#             {'firstName': 'Aron', 'lastName': 'Wilkins'}]

# print("Danh sách học sinh:")
# for student in students:
#     full_name = f"- {student['firstName']} {student['lastName']}"
#     print(full_name)

# #Bài 5
# names = {
#     'students': [
#         {'firstName': 'Nikki', 'lastName': 'Roysden'},
#         {'firstName': 'Mervin', 'lastName': 'Friedland'},
#         {'firstName': 'Aron', 'lastName': 'Wilkins'}
#     ],
#     'teachers': [
#         {'firstName': 'Amberly', 'lastName': 'Calico'},
#         {'firstName': 'Regine', 'lastName': 'Agtarap'}
#     ]
# }

# # In danh sách học sinh
# print("Danh sách học sinh:")
# for student in names['students']:
#     full_name = f"- {student['firstName']} {student['lastName']}"
#     print(full_name)

# # In danh sách giáo viên
# print("\nDanh sách giáo viên:")
# for teacher in names['teachers']:
#     full_name = f"- {teacher['firstName']} {teacher['lastName']}"
#     print(full_name)

# #Bài 6
# # Yêu cầu người dùng nhập chuỗi ký tự
input_string = input("Nhập vào một chuỗi ký tự: ")

# Sử dụng dictionary để đếm số lần xuất hiện của từng ký tự
char_count = {}

# Duyệt qua từng ký tự trong chuỗi
for char in input_string:
    # Kiểm tra xem ký tự đã tồn tại trong dictionary chưa
    if char in char_count:
        # Nếu đã tồn tại, tăng số lần xuất hiện lên 1
        char_count[char] += 1
    else:
        # Nếu chưa tồn tại, thêm vào dictionary với số lần xuất hiện là 1
        char_count[char] = 1

# In số lần xuất hiện của từng ký tự
print("Số lần xuất hiện của từng ký tự trong chuỗi:")
for x, y in char_count.items():
    print(f"{x}: {y}")


