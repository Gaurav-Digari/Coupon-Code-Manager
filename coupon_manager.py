import sys
import secrets
import os
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
      coupon+=secrets.choice(coupon_creation)
    print(coupon)
    try:
       with open ("coupan.txt","r") as file:
          for line in file:
            if secrets.compare_digest(line,coupon):
               i-=1
    except:
      pass
    
    with open ("coupon.txt","a") as file:
       file.write(coupon +" : ACTIVE\n")
  
def redeem_coupons():

   if not os.path.exists("coupon.txt"):
      print("No coupons found.")
   else :
      redeem=input("Enter coupon code: ").strip().upper()
      with open ("coupon.txt","r") as file:
         lines = file.readlines()
         print(lines)
      coupon_found=False
      coupon_used=False
      for i in range(len(lines)):
         code = lines[i][0:14]
         if secrets.compare_digest(code,redeem) :
            coupon_found=True
            if  "USED" in lines[i]:
               coupon_used=True
            else:
               lines[i] = code + " : USED\n"
               print(lines[i])
            break
      if coupon_found :
          if coupon_used :
            print("This coupon was already used.")
          else:
            # NEW: write the updated lines back to the file
            with open ("coupon.txt","w") as file:
               file.writelines(lines)
            print("Coupon redeemed successfully.")
      else:
         print("Invalid coupon code.")


def show_all_coupons():
    print("show_coupons")
    
    

def exit_program():
    sys.exit()
    

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


