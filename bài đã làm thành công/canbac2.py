a=int(input("Hãy nhập số thứ 1 vào đây: "))
b=int(input("Hãy nhập số thứ 2 vào đây: "))
c=int(input("Hãy nhập số thứ 3 vào đây: "))
delta = b*b - 4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    x= -b/(2*a)
    print("Phương trình có nghiệm kép x=", x)
elif delta>0:
    x1=(-b-delta**(1/2))/(2*a)
    x2=(-b+delta**(1/2))/(2*a)
    print("Phương trình có 2 nghiệm phân biệt x1= ", x1, ", x2= ", x2)

input()
