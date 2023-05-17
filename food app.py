class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class FoodMenu:
    def __init__(self):
        self.food_items = []

    def generate_food_id(self):
        if len(self.food_items) > 0:
            last_id = self.food_items[-1].food_id
            return last_id + 1
        else:
            return 1

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = self.generate_food_id()
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = food_id
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                break

    def view_food_items(self):
        for food_item in self.food_items:
            print(f"Food ID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print("")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                break
import random


food_items = {}


registered_users = {}


user_orders = {}


def generate_food_id():
    return str(random.randint(1000, 9999))


def register_user():
    print("Please enter the following details to register:")
    full_name = input("Full Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")
    user_id = str(random.randint(100000, 999999))
    registered_users[user_id] = {
        "Full Name": full_name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address,
        "Password": password,
    }
    print("User registered successfully!")
    return user_id

# Function to authenticate a user
def login_user():
    print("Please enter your Email and Password to login:")
    email = input("Email: ")
    password = input("Password: ")
    for user_id, user in registered_users.items():
        if user["Email"] == email and user["Password"] == password:
            print("Login successful!")
            return user_id
    print("Incorrect Email or Password.")
    return None

# Function to display all the food items
def display_food_items():
    if len(food_items) == 0:
        print("No food items available.")
    else:
        print("List of all food items:")
        for food_id, food in food_items.items():
            print(f"{food_id}. {food['Name']} ({food['Quantity']}) [INR {food['Price']}]")

# Function to add a new food item
def add_food_item():
    print("Please enter the following details to add a new food item:")
    name = input("Name: ")
    quantity = input("Quantity: ")
    price = input("Price: ")
    discount = input("Discount: ")
    stock = input("Stock: ")
    food_id = generate_food_id()
    food_items[food_id] = {
        "Name": name,
        "Quantity": quantity,
        "Price": price,
        "Discount": discount,
        "Stock": stock,
    }
    print(f"Food item {name} added successfully with FoodID {food_id}!")

# Function to edit a food item
def edit_food_item():
    food_id = input("Please enter the FoodID of the food item you want to edit: ")
    if food_id not in food_items:
        print("Invalid FoodID.")
    else:
        print(f"Editing food item with FoodID {food_id}:")
        print(f"1. Name: {food_items[food_id]['Name']}")
        print(f"2. Quantity: {food_items[food_id]['Quantity']}")
        print(f"3. Price: {food_items[food_id]['Price']}")
        print(f"4. Discount: {food_items[food_id]['Discount']}")
        print(f"5. Stock: {food_items[food_id]['Stock']}")
        choice = input("Enter the number of the field you want to edit: ")
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice.")
        else:
            new_value = input(f"Enter the new value for {choice}: ")
            if choice == "1":
                food_items[food_id]['Name'] = new_value
            elif choice == "2":
                food_items[food_id]['Quantity'] = new_value
            elif choice == "3":
                food_items[food_id]['Price'] = new_value
            elif choice == "4":
                food_items[food_id]['Discount'] = new_value
            elif choice == "5":
                food_items[food_id]['Stock'] = new_value
            print("Food item updated successfully!")

# Function to remove a food item
def remove_food_item():
    food_id = input("Please enter the FoodID of the food item you want to remove: ")
    if food_id not in food_items:
        print("Invalid FoodID.")
    else:
        del food_items[food_id]
        print("Food item removed successfully!")

# Function to place a new order
def place_new_order(user_id):
    if len(food_items) == 0:
        print("No food items available to place an order.")
        return
    print("Available food items:")
    for food_id, food in food_items.items():
        print(f"{food_id}. {food['Name']} ({food['Quantity']}) [INR {food['Price']}]")
    selected_items = input("Enter the FoodIDs of the food items you want to order (separated by commas): ")
    selected_items = [item.strip() for item in selected_items.split(",")]
    order_items = []
    total_amount = 0
    for item in selected_items:
        if item in food_items:
            order_items.append(food_items[item])
            total_amount += float(food_items[item]["Price"])
    if len(order_items) == 0:
        print("Invalid FoodIDs. No order placed.")
        return
    print("Selected food items:")
    for food in order_items:
        print(f"{food['Name']} ({food['Quantity']}) [INR {food['Price']}]")
    confirm_order = input("Do you want to place the order? (yes/no): ")
    if confirm_order.lower() == "yes":
        if user_id not in user_orders:
            user_orders[user_id] = []
        order_id = str(random.randint(1000000, 9999999))
        user_orders[user_id].append({
            "OrderID": order_id,
            "Items": order_items,
            "Total Amount": total_amount,
        })
        print(f"Order placed successfully! Your OrderID is {order_id}")
    else:
        print("Order cancelled.")

# Function to view order history
def view_order_history(user_id):
    if user_id not in user_orders or len(user_orders[user_id]) == 0:
        print("No order history found.")
    else:
        print("Order History:")
        for order in user_orders[user_id]:
            print(f"OrderID: {order['OrderID']}")
            print("Items:")
            for item in order["Items"]:
                print(f"- {item['Name']} ({item['Quantity']}) [INR {item['Price']}]")
            print(f"Total Amount: INR {order['Total Amount']}")
            print("")

# Function to update user profile
def update_profile(user_id):
    if user_id not in registered_users:
        print("Invalid User ID.")
    else:
        print("Please enter the following details to update your profile:")
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        password = input("Password: ")
        registered_users[user_id] = {
            "Full Name": full_name,
            "Phone Number": phone_number,
            "Email": email,
            "Address": address,
            "Password": password,
        }
        print("Profile updated successfully!")

# Main program loop
while True:
    print("------- Food Ordering App -------")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Admin functionality
        admin_username = "admin"
        admin_password = "pasword"
        username = input("Admin Username: ")
        password = input("Admin Password: ")
        if username == admin_username and password == admin_password:
            while True:
                print("------- Admin Panel -------")
                print("1. Add new food item")
                print("2. Edit food items")
                print("3. View list of all food items")
                print("4. Remove a food item")
                print("5. Logout")
                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    add_food_item()
                elif admin_choice == "2":
                    edit_food_item()
                elif admin_choice == "3":
                    display_food_items()
                elif admin_choice == "4":
                    remove_food_item()
                elif admin_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Incorrect Admin Username or Password.")
    elif choice == "2":
        # User functionality
        while True:
            print("------- User Panel -------")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                user_id = register_user()
            elif user_choice == "2":
                user_id = login_user()
                if user_id is not None:
                    while True:
                        print("------- User Options -------")
                        print("1. Place New Order")
                        print("2. Order History")
                        print("3. Update Profile")
                        print("4. Logout")
                        user_option = input("Enter your choice: ")

                        if user_option == "1":
                            place_new_order(user_id)
                        elif user_option == "2":
                            view_order_history(user_id)
                        elif user_option == "3":
                            update_profile(user_id)
                        elif user_option == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")

            elif user_choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Food Ordering App!")