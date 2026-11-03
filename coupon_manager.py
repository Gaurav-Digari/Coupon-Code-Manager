print("COUPON MANAGER")
print("==============")



def generate_coupons():
    print("generate_coupons")
    

def redeem_coupons():
    print("redeem_coupons")
    
    

def show_all_coupons():
    print("show_coupons")
    
    

def exit_program():
    print("exit_coupons")
    

while True:
    print("\n1. Generate coupons")
    print("2. Redeem coupon")
    print("3. Show all coupons")
    print("4. Exit")
    choice=int(input("Enter choice: "))
    if 4< choice or choice <1:
        print("Invalid choice")

    else:
        match choice:
         case 1:
            generate_coupons()
         case 2:
            redeem_coupons()
         case 3:
           show_all_coupons()
         case 4:
          exit_program()


