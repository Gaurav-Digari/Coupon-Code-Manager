import sys
import secrets
print("COUPON MANAGER")
print("==============")



def generate_coupons():
   count=int(input("How many coupons (1-10)? "))
   if count>10 or count <1:
      print("Number must be between 1 and 10")
      return

   coupon_creation=("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
   print("Generated:")
   for i in range(0,count):
    coupon=""
    for i in range(1,15):
     if i==5 or i==10:
       coupon+="-"
     else:
      coupon+=(secrets.choice(coupon_creation))
    print(coupon)
    with open ("coupon.txt","a") as file:
       file.write(coupon +" : ACTIVE\n")
  
   

    

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


