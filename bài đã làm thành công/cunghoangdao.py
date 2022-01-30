print("12 Cung Hoàng Đạo")
print("Bạn thuộc cung nào?")
print("Nhập ngày,tháng sinh của bạn vào đây: ")
print("-"*40)
ngaysinh=int(input("Ngày sinh: "))
thangsinh=int(input("Tháng sinh: "))
print("Ngày %s, Tháng %s" % (ngaysinh,thangsinh))

#12 Cung Hoàng Đạo
#Nhân Mã
if ngaysinh>=23 and thangsinh==11 and ngaysinh<=31:
    print("bạn thuộc cung Nhân Mã")
elif thangsinh==12 and ngaysinh<=21 and ngaysinh>=1:
    print("bạn thuộc cung Nhân Mã")

#Mã kết
if ngaysinh>=22 and thangsinh==12 and ngaysinh<=31:
    print("bạn thuộc cung Mã Kết")
elif thangsinh==1 and ngaysinh<=19 and ngaysinh>=1:
    print("bạn thuộc cung Mã Kết")

#Bảo bình
if ngaysinh>=20 and thangsinh==1 and ngaysinh<=31:
    print("bạn thuộc cung Bảo Bình")
elif thangsinh==2 and ngaysinh<=18 and ngaysinh>=1:
    print("bạn thuộc cung Bảo Bình")

#Song Ngư
if ngaysinh>=19 and thangsinh==2 and ngaysinh<=31:
    print("bạn thuộc cung Song Ngư")
elif thangsinh==3 and ngaysinh<=20 and ngaysinh>=1:
    print("bạn thuộc cung Song Ngư")

#Sư Tử
if ngaysinh>=23 and thangsinh==7 and ngaysinh<=31:
    print("bạn thuộc cung Sư Tử")
elif thangsinh==8 and ngaysinh<=22 and ngaysinh>=1:
    print("bạn thuộc cung Sư Tử")

#Xử Nữ
if ngaysinh>=23 and thangsinh==8 and ngaysinh<=31:
    print("bạn thuộc cung Xử Nữ")
elif thangsinh==9 and ngaysinh<=22 and ngaysinh>=1:
    print("bạn thuộc cung Xử Nữ")

#Thiên Bình
if ngaysinh>=23 and thangsinh==9 and ngaysinh<=31:
    print("bạn thuộc cung Thiên Bình")
elif thangsinh==10 and ngaysinh<=23 and ngaysinh>=1:
    print("bạn thuộc cung Thiên Bình")

#Bọ Cạp
if ngaysinh>=24 and thangsinh==10 and ngaysinh<=31:
    print("bạn thuộc cung Bọ Cạp")
elif thangsinh==11 and ngaysinh<=21 and ngaysinh>=1:
    print("bạn thuộc cung Bọ Cạp")

#Bạch Dương
if ngaysinh>=21 and thangsinh==3 and ngaysinh<=31:
    print("bạn thuộc cung Bạch Dương")
elif thangsinh==4 and ngaysinh<=19 and ngaysinh>=1:
    print("bạn thuộc cung Bạch Dương")

#Kim Ngưu
if ngaysinh>=20 and thangsinh==4 and ngaysinh<=31:
    print("bạn thuộc cung Kim Ngưu")
elif thangsinh==5 and ngaysinh<=20 and ngaysinh>=1:
    print("bạn thuộc cung Kim Ngưu")
#Song Tử
if ngaysinh>=21 and thangsinh==5 and ngaysinh<=31:
    print("bạn thuộc cung Kim Ngưu")
elif thangsinh==6 and ngaysinh<=21 and ngaysinh>=1:
    print("bạn thuộc cung Kim Ngưu")

#Cự Giải
if ngaysinh>=22 and thangsinh==6 and ngaysinh<=31:
    print("bạn thuộc cung Kim Ngưu")
elif thangsinh==7 and ngaysinh<=22 and ngaysinh>=1:
    print("bạn thuộc cung Kim Ngưu")

input()