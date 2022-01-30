def cach1():
    try:
        kytu = "*"
        chieudai = 50
        n = int(input("Nhập 1 số từ 1-9: "))
        print("-"*50)
        if n<1 or n>9:
            print("Chi tinh duoc bang cuu chuong 1 den 9 thoi!")
        else:

            print("Bẳng cửu chuong ",n)
            for i in range(1, 10):
                print("{} x {} = {}".format(n, i, n*i))

    except:
        print("Dinh dang dau vao khong hop le!")

cach1()
