class Customer:
    def __init__(self, name, id_number, package, duration):
        self.name = name
        self.id_number = id_number
        self.package = package
        self.duration = duration

    def get_total_cost(self):
        base_fee = self.package.base_fee
        class_fee = self.package.class_fee
        steam_fee = self.package.steam_fee
        pt_fee = self.package.pt_fee

        total_cost = base_fee + class_fee + steam_fee + pt_fee
        return total_cost


class Package:
    def __init__(self, base_fee, class_fee, steam_fee, pt_fee):
        self.base_fee = base_fee
        self.class_fee = class_fee
        self.steam_fee = steam_fee
        self.pt_fee = pt_fee


class PremiumPackage(Package):
    def __init__(self):
        super().__init__(1000, 0, 0, 0)


class BasicPackage(Package):
    def __init__(self):
        super().__init__(500, 100, 0, 100)


class NonMemberPackage(Package):
    def __init__(self):
        super().__init__(200, 0, 0, 200)


def main():
    customers = []

    while True:
        print("1. Add customer")
        print("2. Display customer information")
        print("3. Find customer with highest spending")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            id_number = input("Enter customer ID number: ")

            print("Select package:")
            print("1. Premium")
            print("2. Basic")
            print("3. Non-member")

            package_choice = input("Enter package choice: ")

            if package_choice == "1":
                package = PremiumPackage()
            elif package_choice == "2":
                package = BasicPackage()
            elif package_choice == "3":
                package = NonMemberPackage()
            else:
                print("Invalid package choice. Please try again.")
                continue

            duration = input("Enter duration (in months): ")

            customer = Customer(name, id_number, package, duration)
            customers.append(customer)
            print("Customer added successfully.")

        elif choice == "2":
            if len(customers) == 0:
                print("No customers found.")
            else:
                for customer in customers:
                    print("Name:", customer.name)
                    print("ID Number:", customer.id_number)
                    print("Package:", customer.package.__class__.__name__)
                    print("Duration:", customer.duration)
                    print("Total Cost:", customer.get_total_cost())
                    print()

        elif choice == "3":
            if len(customers) == 0:
                print("No customers found.")
            else:
                max_spending_customer = max(customers, key=lambda x: x.get_total_cost())
                print("Customer with highest spending:")
                print("Name:", max_spending_customer.name)
                print("ID Number:", max_spending_customer.id_number)
                print("Package:", max_spending_customer.package.__class__.__name__)
                print("Duration:", max_spending_customer.duration)
                print("Total Cost:", max_spending_customer.get_total_cost())
                print()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
