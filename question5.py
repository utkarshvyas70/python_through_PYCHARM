
#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user
purchased_quantity=float(input("Cost of your shopping:"))
if purchased_quantity>1000:
    print("You are eligible for discount")
    print("Your final payable amount is:",purchased_quantity+purchased_quantity*0.1)