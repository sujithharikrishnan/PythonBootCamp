print("Welcome to the Tip calculator!")
total_bill = float(input("Enter the total bill amount: "))
tip_percent = int(input("How much would you like to tip? 10 or 12 or 15?"))
person_count = int(input("How many people to share the amount?"))

tip_amount = total_bill * (tip_percent/100)
final_amount = total_bill + tip_amount
share_amount = final_amount / person_count
print(f"Each person should share: {"%.2f" % share_amount}")

