# keo,bua,bao voi may tinh
from random import randint
print("Hãy chọn ĐẤM, BAO hoặc KÉO")
# menh de player
player = input()
print("------")
print('Bạn chọn', player)
# menh de computer
computer = randint(0,2)
if computer == 0:
    if player == "ĐẤM":
        print("Máy tính chọn Đấm, bạn chọn Đấm, hòa")
    if player == "KÉO":
        print("Máy tính chọn Đấm, bạn chọn Kéo, máy tính thắng, bạn thua")
    if player == "BAO":
        print("Máy tính chọn Đấm, bạn chọn Bao, máy tính thua, bạn thắng")
if computer == 1:
    if player == "KÉO":
        print("Máy tính chọn Kéo, bạn chọn Kéo, hòa")
    if player == "ĐẤM":
        print("Máy tính chọn Kéo, bạn chọn Đấm, máy tính thua, bạn thắng")
    if player == "BAO":
        print("Máy tính chọn Kéo, bạn chọn Bao, máy tính thắng, bạn thua")
if computer == 2:
    if player == "BAO":
        print("Máy tính chọn Bao, bạn chọn Bao, hòa")
    if player == "ĐẤM":
        print("Máy tính chọn Bao, bạn chọn Đấm, máy tính thắng, bạn thua")
    if player == "KÉO":
        print("Máy tính chọn Bao, bạn chọn Kéo, máy tính thua, bạn thắng")
# END 