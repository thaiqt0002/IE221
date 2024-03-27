class SoNguyen:
    def __init__(self, value):
        self.value = value

    def nhap(self):
        self.value = int(input("Nhập số nguyên: "))

    def xuat(self):
        print("Số nguyên:", self.value)

    def cong(self, other):
        return self.value + other.value

    def tru(self, other):
        return self.value - other.value

    def nhan(self, other):
        return self.value * other.value

    def chia(self, other):
        if (other.value):
            return self.value / other.value
        else:
            return 'null'

so1 = SoNguyen(0)
so2 = SoNguyen(0)

so1.nhap()
so2.nhap()

print("Tổng:", so1.cong(so2))
print("Hiệu:", so1.tru(so2))
print("Tích:", so1.nhan(so2))
print("Thương:", so1.chia(so2))