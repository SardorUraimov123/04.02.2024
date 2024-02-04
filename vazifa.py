#1-misol
# class Haftakunlar:
#     def __init__(self):
#         haftakunlari = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]

#     def __iter__(self):
#         self.index =0
#         return self
    
#     def __next__(self):
#         if self.index < len(self.haftakunlari):
#             kun = self.haftakunlari[self.index]
#             self.index +=1
#             return kun
#         else:
#             raise StopIteration
        
# haftakunlar = Haftakunlar()
# for i in haftakunlar:
#     print(i)
#2-misol
# class Oylar:
#     def __init__(self):
#         self.month = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]

#     def __iter__(self):
#         self.index = 0
#         return self
    
#     def __next__(self):
#         if self.index < len(self.month):
#             kun = self.month[self.index]
#             self.index += 1
#             return kun
#         else:
#             raise StopIteration

# oylar = Oylar()
# for i in oylar:
#     print(i)
#3-misol
class User:
    def __init__(self, f_name, l_name, email):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

user1 = User("Sardor", "Uraimov", "sardoruraimov14@gmail.com")
user2 = User("Jasurbek", "Murodilov", "byMurodilov@gmail.com")
user3 = User("MuhammadAzizxon", "Abuvahobov", "AzizxonAbduvahobov@gmail.com")

users = [user1, user2, user3]

for user in users:
    print(f"First Name: {user.f_name}, Last Name: {user.l_name}, Email: {user.email}")

