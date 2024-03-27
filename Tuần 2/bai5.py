class PhanSo:
    tuSo: int
    mauSo: int
    
    def __init__(self, tuSo = 9, mauSo = 15):
        self.tuSo = tuSo
        self.mauSo = mauSo
        
    def nhap(self):
        self.tuSo = int(input("Nhap tu so: "))
        self.mauSo = int(input("Nhap mau so: "))
    
    def xuat(self):
        self.rutgon()
        return f'{self.tuSo}/{self.mauSo}'
    
    def rutgon(self):
        gcd = self.ucln()
        self.tuSo //= gcd
        self.mauSo //= gcd
        return self
        
    def ucln(self):
        a = self.tuSo
        b = self.mauSo
        while b != 0:
            a, b = b, a % b
        return a
        
    def cong(self, other):
        new_tuSo = self.tuSo * other.mauSo + self.mauSo * other.tuSo
        new_mauSo = self.mauSo * other.mauSo
        return PhanSo(new_tuSo, new_mauSo )
    
    def tru(self, other):
        new_tuSo = self.tuSo * other.mauSo - self.mauSo * other.tuSo
        new_mauSo = self.mauSo * other.mauSo
        return PhanSo(new_tuSo, new_mauSo)
        
    def nhan(self, other):
        new_tuSo = self.tuSo * other.tuSo
        new_mauSo = self.mauSo * other.mauSo
        return PhanSo(new_tuSo, new_mauSo)
    
    def chia(self, other):
        new_tuSo = self.tuSo * other.mauSo
        new_mauSo = self.mauSo * other.tuSo
        return PhanSo(new_tuSo, new_mauSo)
        
        
ps1 = PhanSo(3,4)
ps2 = PhanSo(9,15)

print(ps1.xuat())
print(ps2.xuat())

ps3 = ps1.cong(ps2)
ps4 = ps1.tru(ps2)
ps5 = ps1.nhan(ps2)
ps6 = ps1.chia(ps2)

print('Tong:', ps3.xuat())
print('Hiệu:', ps4.xuat())
print('Tích:', ps5.xuat())
print('Thương:', ps6.xuat())



        