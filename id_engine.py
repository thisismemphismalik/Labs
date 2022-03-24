# from datetime import datetime
# from random import randint
#
# letters = "AZERTYUPQSDFGHJKLMWXCVBN"
# digits = "23456789"
#
#
# def create():
#     a = ""
#     c = [None, None]
#
#     for item in range(3):
#         for j in range(2):
#             a = a + digits[randint(0, 7)]
#         a = a + letters[randint(0, 23)]
#
#         if item != 2:
#             a = a + "-"
#     b = datetime.utcnow()
#
#     c[0] = a
#     c[1] = b
#
#     # return {a: f"{b}"}
#     return a
#
#
# with open("./code.txt", "a+") as file:
#
#     for i in range(1000000000):
#         file.seek(0)
#
#         a = create()
#
#         while a in file.readlines():
#             print("double")
#             a = create()
#
#         file.write(f"{create()}\n")
#
#         file.seek(0)
#         print(len(file.readlines()))
#

import qrcode

img = qrcode.make("I AM QUEER")
img.save("./test.png")
