import os

print("===========================================================")
print("|                       Easy PC                           |")
print("===========================================================")
name = input("Please enter your name: ")
question = input("Do you want to enter?(y/n) ")
if question == "y":
    print("===========================================================")
    print ("Welcome, Sir/Ma'am " + name + " to Easy PC!")
    print ("Navigation:")
    print ("1. About Us")
    print ("2. Order")
    print ("3. Products")
    print ("4. Contacts")
    print ("5. Location")
    print ("6. Exit")
    nav = input("Please choose a number to navigate our page: ")
    print("===========================================================")
    os.system('cls')
    if nav == "1":
        print ("EasyPC is a computer retail business founded on the values of convenience, accessibility, and excellent customer service.")
    elif nav == "2":
        print ("Order")
        pd = input("Enter a product number: ")
        pr = int(input("Enter a product price: "))
        qt = int(input("Enter a Quantity: "))
        tc = pr * qt
        print ("Total Price: " + str(tc))
        atp = int(input("Amount to Pay: "))
        print ("List of mode of payments: ")
        print ("1. Pay at the Counter / Cash")
        print ("2. GCash")
        print ("3. Maya")
        mp = input("Select Payment: ")
        if mp == "1":
            print ("Please go to counter 1 or 2 and show your receipt for your payment. Thank you!")
            print ("Order Receipt")
            print ("Product Number: " + pd)
            print ("Price: " + str(pr))
            print ("Quantity: " + str(qt))
        elif mp == "2":
            print ("Here's our GCash Number:")
            print ("09123456789 Ronian S.")
        elif mp == "3":
            print ("Here's our Maya Number:")
            print ("09123456789 Ronian S.")
    elif nav == "3":
        print("List of Products")
        print("0001 - Asrock RX 6600 8G CHALLENGER D 8gb 128bit GDdr6 Dual Fan Design, Super Alloy Striped Axial Fan Gaming Videocard = ₱11,790.00")
        print("0002 - PNY GTX 1650 Dual Fan 4gb 128bit GDdr6 Gaming Videocard = ₱8,695.00")
        print("0003 - Team Elite Vulcan TUF 16gb 2x8 3200mhz Ddr4 Gaming Memory = ₱2,415.00")
        print("0004 - Team Elite TForce Delta 16gb 2x8 3200mhz Ddr4 RGB Memory White = ₱3,105.00")
        print("0005 - Samsung LF24T350FHEXXP 24in 75Hz AMD FreeSync, 3-Sided bezel-less display, IPS Panel Monitor = ₱4,950.00")
    elif nav == "4":
        print("Contacts:")
        print("Customer Service Hotline: 09123456789")
        print("Email: sales@easypc.com.ph")
        print("Facebook Messenger: www.fb.com/easypc.ph")
    elif nav == "5":
        print("Store Locations:")
        print("EasyPC Fairview Branch")
        print("Unit 3 to 5 Ground Floor Yaya Dub Apartelle Quirino Highway Greater Lagro Fairview, Quezon City, Metro Manila, Philippines")
        print("EasyPC Bacoor Branch")
        print("EasyPC, 234 Emilio Aguinaldo HwyEASYPC Bacoor: 248 Aguinaldo Hi-way, Brgy. Panapaan 4, Bacoor, Cavite Philippines")
        print("EasyPC Monumento")
        print("Unit CS202 Philtrust Bank Bldg., Samson Road, Brgy. 77, Caloocan City, Metro Manila Philippines")
    elif nav == "6":
        print("Thank you for visiting our site!")
        quit()
else:
    print ("Thank you for visiting our site!")


