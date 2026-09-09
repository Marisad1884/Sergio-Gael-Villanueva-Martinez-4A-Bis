class keyboard:
    def __init__(self, brand,model,connection):
        self.brand = brand
        self.model = model
        self.connection = connection

    def move(self):
            print("The keyboard is moving")


    def describe(self):
            print(f"The keyboard is a {self.brand} {self.model} with a {self.connection} connection.")

#create multiple instances using the class "Keyboard"   
#instance 1
keyboard1 = keyboard("Logitech", "K120", "USB")
keyboard2 = keyboard("Razer", "BlackWidow", "Wireless")

print(keyboard1.model)
print(keyboard2.model)
keyboard1.describe()
keyboard2.describe()

#Lab 1 Bank Account Class
class BankAccount:
      def __init__(self,holder,curr_balance):
            self.holder = holder
            self._balance = curr_balance

        def deposit(self, amount):

        def withdraw(self, amount):

        def get_balance(self):