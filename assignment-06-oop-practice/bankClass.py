class Bank:
    bank_name = "Al falah"
    def __init__ (self):
        Bank.bank_name
        print(f"Bank {Bank.bank_name}")

    @classmethod
    def change_name(cls):
        Bank.bank_name = input("Enter new name to change your bank name ")
        print(f"your new bank name is {cls.bank_name}")
    

owner1 = Bank()
owner1.change_name()
