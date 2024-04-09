class Stall:
    def __init__(self, stall_number, area):
        self.stall_number = stall_number
        self.area = area

    def calculate_rental_fee(self):
        rental_fee = 40000000 * self.area
        return rental_fee

    def calculate_tax(self):
        return 0.0


class FoodStall(Stall):
    def __init__(self, stall_number, area, cold_storage_fee):
        super().__init__(stall_number, area)
        self.cold_storage_fee = cold_storage_fee

    def calculate_tax(self):
        tax = 0.05 * self.calculate_rental_fee()
        return tax


class ClothingStall(Stall):
    def calculate_tax(self):
        tax = 0.1 * self.calculate_rental_fee()
        return tax


class JewelryStall(Stall):
    def __init__(self, stall_number, area, annual_revenue):
        super().__init__(stall_number, area)
        self.annual_revenue = annual_revenue

    def calculate_tax(self):
        if self.annual_revenue <= 100000000:
            tax = 0.2 * self.calculate_rental_fee()
        else:
            tax = 0.3 * self.calculate_rental_fee()
        return tax


def main():
    stalls = []
    total_rental_fee = 0

    # Input information for each stall
    n = int(input("Enter the number of stalls: "))
    for i in range(n):
        stall_number = input("Enter the stall number: ")
        area = float(input("Enter the area of the stall: "))
        stall_type = input("Enter the type of stall (food/clothing/jewelry): ")

        if stall_type == "food":
            cold_storage_fee = float(input("Enter the cold storage fee: "))
            stall = FoodStall(stall_number, area, cold_storage_fee)
        elif stall_type == "clothing":
            stall = ClothingStall(stall_number, area)
        elif stall_type == "jewelry":
            annual_revenue = float(input("Enter the annual revenue: "))
            stall = JewelryStall(stall_number, area, annual_revenue)
        else:
            print("Invalid stall type!")
            continue

        stalls.append(stall)
        total_rental_fee += stall.calculate_rental_fee() + stall.calculate_tax()

    print("Total rental fee to be paid annually: ", total_rental_fee)


if __name__ == "__main__":
    main()
