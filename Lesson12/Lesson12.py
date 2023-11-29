# #Mở File trong Python chúng ta dùng open()
# #open (filepath, mode '', buffering=-1)
# #filepath: Là đường dẫn tới file
# #mode: r - read để đọc file , w - write để ghi file, a-add ghi thêm vô file, x - tạo file
# #   mode w: Mở file để ghi, nếu file không tồn tại -> tạo mới file; ghi đè
# #   mode a: Thêm vào cuối của file

# with open('./hello.txt', 'r') as file: 
#     contents = file.readlines()
#     print(contents)
#     contents.pop(1)
#     #content = file.read()
#     print(contents)
#     with open('./hello.txt', 'w') as file:
#         for content in contents:    # Duyệt từng phần từ trong chuỗi contents (nội dung của file)
#             file.write(content)         # Ghi từng dòng từ chuỗi contents vào tệp (hello.txt)

with open('./hello.txt', 'r') as file: 
    contents = file.readlines()
print(contents)

# # with open('./myfile.txt', 'a') as f:
# #     f.write("This is new content added to myfile.txt")

# # import os

# # os.remove('./hello1.txt')

# # read(): Đọc toàn bộ File
# # read(n): Đọc File với n ký tự
# # readline(): Đọc từng dòng của file

#1 Đọc, in nội dung của 1 file và cập nhật nội dung mới cho file đó
#2 Đếm số dùng, số từ, ký tự có trong file
#3 Sao chép nội dung từ file này sang file khác (thêm mới != ghi đè)
#4 Nối hai file thành 1 file

# def read_and_update_file():
#     file_path = input("Nhập filepath: ")

#     with open(file_path, "r") as f: 
#         contents = f.read()

#     print ("Nội dung file ban đầu")
#     print(contents)
    
#     new_contents = input("Nhập nội dung bạn muốn thêm vào: ")
#     updated_contents = contents + "\n" + new_contents

#     with open(file_path,"w") as f:
#         f.write(updated_contents)

# read_and_update_file()

# def count_lines_word_characters():
#     file_path = input("Nhập filepath: ")

#     with open(file_path, "r") as f: 
#         contents = f.read()

#     print ("Nội dung file ban đầu")
#     print(contents)  

#     lines = contents.split("\n")
#     words = contents.split(" ")
#     characters = len(contents)

#     print("Số dòng: ", len(lines))
#     print("Số từ: ", len(words))
#     print("Ký tự: ", characters)

# count_lines_word_characters()

# def copy_file():
#     source_file_path = input("Nhập file path ban đầu: ")

#     destination_file_path = input("Nhập file path đích: ")

#     with open(source_file_path, "r") as f_source:
#         contents = f_source.read()

#     with open(destination_file_path, "a") as f_destination: 
#         f_destination.wirte(contents)

# copy_file()

# def merge_file():

#     file_path_1 = input("Nhập file cần merge 1: ")
#     file_path_2 = input("Nhập file cần marge_2: ")
#     destination_file = input("Nhập file merge: ") # file mới 
#     with open(file_path_1, "r") as f1:
#         contents_1 = f1.read()
#     with open(file_path_2, "r") as f2:
#         contents_2 = f2.read()

#     contents = contents_1 + contents_2

#     with open(destination_file, "w") as f_destination:
#         f_destination.write(contents)

# merge_file()


# Hãy viết một mini game cho người dùng trả lời câu hỏi và tính điểm, dựa vào
# các câu hỏi trong file.
corrects = 0

with open('./question_bank.txt', 'r') as file: 
    for line in file: 
        question = line.split(',')
        print(question[0])
        if input() == question[1][:-1]: 
            #[:-1]: cú pháp để cắt chuỗi -> Lấy tất cả các phần tử cho đến vị trí áp chót
            corrects +=1

print(f"You have: {corrects} points")