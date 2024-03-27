class BanhMi:
    def __init__(self, ma_banh, ten_banh, loai_banh, nuoc_san_xuat, han_su_dung, gia_ban):
        self.ma_banh = ma_banh
        self.ten_banh = ten_banh
        self.loai_banh = loai_banh
        self.nuoc_san_xuat = nuoc_san_xuat
        self.han_su_dung = han_su_dung
        self.gia_ban = gia_ban

    def in_thong_tin(self):
        print("Thông tin ổ bánh mì:")
        print("Mã bánh:", self.ma_banh)
        print("Tên bánh:", self.ten_banh)
        print("Loại bánh:", self.loai_banh)
        print("Nước sản xuất:", self.nuoc_san_xuat)
        print("Hạn sử dụng:", self.han_su_dung)
        print("Giá bán:", self.gia_ban)

    def tinh_tien(self, n):
        return self.gia_ban * n


class BanhMiKhong(BanhMi):
    def __init__(self, ma_banh, ten_banh, loai_banh, nuoc_san_xuat, han_su_dung):
        super().__init__(ma_banh, ten_banh, loai_banh, nuoc_san_xuat, han_su_dung, 5000)


class BanhMiCuaMe(BanhMi):
    def __init__(self, ma_banh, ten_banh, loai_banh, nuoc_san_xuat, han_su_dung):
        super().__init__(ma_banh, ten_banh, loai_banh, nuoc_san_xuat, han_su_dung, 20000)


p = int(input("Nhập số lượng ổ bánh mì \"không\": "))
q = int(input("Nhập số lượng ổ bánh mì \"của mẹ\": "))

banh_mi_khong = BanhMiKhong("BM001", "Bánh mì không", "Không", "Việt Nam", "30/09/2022")
banh_mi_cua_me = BanhMiCuaMe("BM002", "Bánh mì của mẹ", "Của mẹ", "Việt Nam", "30/09/2022")

tong_tien = banh_mi_khong.tinh_tien(p) + banh_mi_cua_me.tinh_tien(q)
print("Tổng số tiền cần trả:", tong_tien, "đồng")