# car = {
#     "brand": "Toyota",
#     "model": "Corolla",
#     "year": 2019,
#     "price": 10000
# }
# #print(car["model"]) # Toyota

# # Duyệt phần tử để in ra các giá trị trong dict 
# # for key, value in car.items():
# #     print("Key: ",key," Value: ",value)

# # car['Origin'] = 'Japan'
# # # Add phần tử mới vào dict
# # for key, value in car.items():
# #     print("Key: ",key," Value: ",value)

# # car['price'] = '20000'
# # del car["price"]
# # for key, value in car.items():
# #     print("Key: ",key," Value: ",value)
# # print("Length of dictionary: ", len(car))
# if 'engine'  in car: 
#     print ('Brand is exist')
# else: 
#     print('Brand not exist')

# Bài I) Init dictionary - Dưới đây là thông tin về số lượng máy tính theo hãng trong 1 kho của một shop:
# HP: 20
# DELL: 50
# MACBOOK: 12
# ASUS: 30
# Khai báo 1 dictionary để biểu diễn thông tin trên
# Read - Hiện ra số lương MACBOOK có trong kho
# Read - with key from input - Lặp lại câu 2 với hãng máy tính nhập bởi người dùng

# Ordinateur = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30
# }

# print("Số lượng MACBOOK: ", Ordinateur['MACBOOK'])

# Brand = input("Nhập hãng máy tính: ")
# if Brand in Ordinateur:
#     print ("So luong may",Brand, "cua hang la", Ordinateur[Brand])
# else: 
#     print("Hãng", Brand,"không tồn tại trong kho")

# Bài II) Init character dictionary - Dưới đây là mô tả một nhân vật trong 1 text adventure:
# Name: Light
# Age: 17
# Strength: 8
# Defense: 10
# HP: 100
# Backpack: Shield, Bread Loaf
# Gold: 100
# Level: 2
# Sử dụng 1 dictionary để mô tả nhân vật này
# Update character dictionary - Không chỉnh sửa khai báo, thêm 50 Gold cho nhân vật này
# Update character dictionary (2) - Không chỉnh sửa khai báo, thêm FlintStone vào Backpack của nhân vật này
# Update character dictionary (3) - Không chỉnh sửa khai báo, thêm mô tả Pocket cho nhân vật, 
#   trong Pocket chứa 1 danh sách các vật dụng bao gồm MonsterDex và Flashlight

character = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2
}
print (character)

# Cập nhật Gold của nhân vật thêm 50 Gold
character['Gold'] += 50
print("Gold: ", character['Gold'])

# Cập nhật thêm Flint Stone vào backpack của nhân vật
character['Backpack'].append('Flintstone')
print("Backpack: ", character['Backpack'])

#Tạo mô tả cho Pocket của nhân vật: 
# character['Pocket'] = {
#     'Danh sách vật dụng': ['MonsterDex', 'Flash Light']
# }

character.setdefault('pocket', ['monster dex', 'flashlight'])
# In ra thông tin nhân vật sau khi cập nhật 
print(character)

