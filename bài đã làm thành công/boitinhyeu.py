#làm code tiên tri tình yêu

def boi_tinh_yeu(ten_nam, ten_nu):

	#Chuyển thành viết thường
	ten_nam=ten_nam.lower()
	ten_nu=ten_nu.lower()

	#Chính
	dem=0
	#Chuyển bảng chữ cái thành số
	for bang_chu_cai in range(ord('a'), ord('z')+1):
		#tổng 2 số trùng nhau từ tên
		if (chr(bang_chu_cai) in ten_nam) and (chr(bang_chu_cai) in ten_nu):
			#Biến đểm để đếm các sỗ được lấy từ tên nam và tên nữ trùng nhau
			dem=dem+1

	#Bói
	if dem==0:
		ket_qua= "Không hợp nhau"
	elif dem < 4:
		ket_qua= "Bạn bè"
	else:
		ket_qua="Hợp nhau"
	return ket_qua

#đầu vàp
print("Nhập tên bạn nam: ")
ten_nam=input()
print("Nhập tên bạn nữ: ")
ten_nu=input()

#đầu ra
print("Kết quả của 2 bạn là: " + boi_tinh_yeu(ten_nam, ten_nu))