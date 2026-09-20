# ==============================================================================
# PROJECT TITLE: ATM Cash Withdrawal Project
# DESCRIPTION: A Python program simulating an ATM machine user flow including
#              PIN authentication, transaction selection, preset amounts, card 
#              ejection safety warnings, and receipt options.
# ==============================================================================

# Cash Withdrawal from ATM Machine

print("Please insert your card.")

correct_pin = 1234
attempts = 3

# PIN verification loop
for i in range(attempts):
    pin = int(input("Enter your 4-digit card PIN: "))
    if pin == correct_pin:
        print("PIN verified successfully!")
        break
    else:
        print("Your PIN is incorrect. Try again!")

if pin == correct_pin:
    transaction_selection = input("Enter your transaction type (Withdrawal / Check balance or statement / Deposit): ").lower()

    if transaction_selection == "withdrawal":
        preset_amounts = {
            "1": 1000,
            "2": 10000,
            "3": 50000
        }
        
        print("\nPreset Amounts:")
        print("1. $1,000")
        print("2. $10,000")
        print("3. $50,000")
        
        choice = input("Choose a preset option (1/2/3) or enter 'custom': ").lower()
        
        if choice in preset_amounts:
            withdrawal_amount = preset_amounts[choice]
        elif choice == "custom":
            withdrawal_amount = int(input("Enter custom withdrawal amount: "))
        else:
            withdrawal_amount = 0
            print("Invalid amount selected.")

        print("\nWe are going to give your card back before your cash.")
        proceed = input("Please confirm to collect your card (yes/no): ").lower()
        
        if proceed == "yes":
            print("Please take your card.")
        else:
            print("Please wait!")

        print("ATM is processing your cash. Please wait...")
        print(f"Dispensing ${withdrawal_amount}...")

        receipt = input("Would you like a printed receipt? (yes/no): ").lower()
        if receipt == "yes":
            print("Please take your receipt.")
        else:
            print("No receipt selected.")

    print("Thank you for using our ATM!")
else:
    print("Card blocked due to multiple incorrect attempts.")
