print("-------------------- WELCOME TO AENS PIZZA --------------------\n")

while True:
        name = input("Please enter your name: ")

        print("""
                    List Menu Pizza:
        1. Frankfurter BBQ      - Rp 85.000
        2. Meat Monster         - Rp 110.000
        3. Super Supreme        - Rp 100.000
        4. Supreme Chicken      - Rp 94.000
        5. Meat Lover           - Rp 115.000
        6. Chicken Lovers       - Rp 92.000
        7. Cheese Lovers        - Rp 90.000
        8. American Pizza       - Rp 105.000
        """)

        pizza_name = ""
        crust_pizza = ""
        size_pizza = ""
        extra_cheese = ""
        total_bill = 0

        while True:
                choice_pizza = input("Choose your pizza by number: ")

                if choice_pizza == "1":
                    total_bill += 85000
                    pizza_name = "Frankfurter BBQ (Rp 85.000)"
                    break
                elif choice_pizza == "2":
                    total_bill += 110000
                    pizza_name = "Meat Monster (Rp 110.000)"
                    break
                elif choice_pizza == "3":
                    total_bill += 100000
                    pizza_name = "Super Supreme (Rp 100.000)"
                    break
                elif choice_pizza == "4":
                    total_bill += 94000
                    pizza_name = "Supreme Chicken (Rp 94.000)"
                    break
                elif choice_pizza == "5":
                    total_bill += 115000
                    pizza_name = "Meat Lover (Rp 115.000)"
                    break
                elif choice_pizza == "6":
                    total_bill += 92000
                    pizza_name = "Chicken Lovers (Rp 92.000)"
                    break
                elif choice_pizza == "7":
                    total_bill += 90000
                    pizza_name = "Cheese Lovers (Rp 90.000)"
                    break
                elif choice_pizza == "8":
                    total_bill += 105000
                    pizza_name = "American Pizza (Rp 105.000)"
                    break
                else:
                    print("Your choice is not available.")

        print("""
        \nChoice Crust:
        1. Thin Crust          - Rp 25.000
        2. Thick Crust         - Rp 30.000
        3. Stuffed Crust       - Rp 35.000
        4. Pizza Pan           - Rp 31.000
        """)

        while True:
                choice_crust = input("Choose crust by number: ")

                if choice_crust == "1":
                    total_bill += 25000
                    crust_pizza = "Thin Crust (Rp 25.000)"
                    break
                elif choice_crust == "2":
                    total_bill += 30000
                    crust_pizza = "Thick Crust (Rp 30.000)"
                    break
                elif choice_crust == "3":
                    total_bill += 35000
                    crust_pizza = "Stuffed Crust (Rp 35.000)"
                    break
                elif choice_crust == "4":
                    total_bill += 31000
                    crust_pizza = "Pizza Pan (Rp 31.000)"
                    break
                else:
                    print("Your choice is not available.")

        print("""
        \nChoice Size:
        1. Small  - Rp 5.000
        2. Medium - Rp 10.000
        3. Large  - Rp 15.000
        """)
        while True:
                choice_size = input("Choose size by number: ")

                if choice_size == "1":
                    total_bill += 5000
                    size_pizza = "Small (Rp 5.000)"
                    break
                elif choice_size == "2":
                    total_bill += 10000
                    size_pizza = "Medium (Rp 10.000)"
                    break
                elif choice_size == "3":
                    total_bill += 15000
                    size_pizza = "Large (Rp 15.000)"
                    break
                else:
                    print("Your choice is not available.")
                    
        extra_cheese = input("\nWould you like extra cheese for Rp 15.000? (yes/no): ")

        if extra_cheese.lower() == "yes":
            total_bill += 15000
            extra_cheese = "Yes (Rp 15.000)"
        elif extra_cheese.lower() == "no":
             extra_cheese = "No (Rp 0)"
        else:
            print("Your choice is not available.")

        print("\n\n-------------------- ORDER SUMMARY --------------------")
        print(f"Name          : {name}")
        print(f"Pizza         : {pizza_name}")
        print(f"Crust         : {crust_pizza}")
        print(f"Size          : {size_pizza}")
        print(f"Extra Cheese  : {extra_cheese}")
        print(f"Total Bill    : Rp {total_bill:,.0f}")

        choice=input("Is your order correct? (yes/no) :")

        if choice.lower()=="yes":
             break
        elif choice.lower()=="no":
             print("\nplease make your order again\n")
             continue
        else:
             print("your choice is not available")

print("\nThank you for your order!<3\n")
