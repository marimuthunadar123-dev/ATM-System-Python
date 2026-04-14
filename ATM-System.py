# ATM WITHDRAWAL SYSTEM 

correct_pin = "1111"
pin_login = False
max_limit = 3 
balance = 5000
transaction_history = []

# PIN Verification Loop 
for pin_attempt in range(1,max_limit+1) : 
  user_pin = input("\nEnter your PIN: ")
  
  if user_pin == correct_pin :
    pin_login = True
    print("PIN Verified ✅")
    break 
  else :
    remaining_pin_attempt = max_limit - pin_attempt

    if pin_attempt == 2 :
      print("Warning: Suspicious Activity ⚠️")
    else :
      print(f"Invalid Pin ❌  last {remaining_pin_attempt} attempt is left")


if pin_login :
  # ATM Operation Loop 
  while True : 
    print("\n---- 🏪 ATM MENU ----\n")
    print("1️⃣   Check Balance")
    print("2️⃣   Deposit")
    print("3️⃣   Withdraw")
    print("4️⃣   Transaction History")
    print("5️⃣   Exit")
    print("\n----------------------\n")

    user_option = input("Select a option (1/2/3/4/5): ")

    if user_option == "1" :
      print(f"Your Balance is: ₹{balance:,.2f}/-")

    elif user_option == "2" :
      # Deposit Amount Validation Loop 
      deposit_amount_attempt = 0 

      while deposit_amount_attempt < max_limit :
        deposit_amount = float(input("\nEnter your deposit amount: "))

        if deposit_amount <= 0 :
          print("Invalid amount ⚠️  (amount must be > 0)")
          deposit_amount_attempt += 1 
          continue
        else :
          break

      if deposit_amount_attempt >= max_limit :
        print("\nToo many Invalid attempts 🚫")
        print("Process Cancelled ⏩⏩")

      else : 
        # Deposit Confirmation Validation Loop 
        deposit_confirm_attempt = 0 

        while deposit_confirm_attempt < max_limit :
          deposit_confirm = input("Are you sure you want to deposit? (Y/N): ").upper()

          if deposit_confirm == "Y" :
            balance = balance + deposit_amount 
            print(f"\n₹{deposit_amount:,.2f}/- is Credited in your Account ✅")
            print(f"Your Current Balance is: ₹{balance:,.2f}/-")
            transaction_history.append(f"Deposited ₹{deposit_amount:,.2f}")
            break

          elif deposit_confirm == "N" :
            print("\nProcess Cancelled ⏩⏩")
            break 

          else : # deposit_confirm != "Y" and deposit_confirm != "N" :
            deposit_confirm_attempt += 1
            remaining_attempt = max_limit - deposit_confirm_attempt
            
            if remaining_attempt > 0 :
              print("Invalid Input ⚠️  Enter (Y/N)\n")
            print(f"{remaining_attempt} attempt is left")
  
        if deposit_confirm_attempt >= max_limit :
          print("\nToo many Invalid attempts 🚫")
          print("Process Cancelled ⏩⏩")

    elif user_option == "3" :
      # Withdraw Amount Validation Loop 
      withdraw_amount_attempt = 0 

      while withdraw_amount_attempt < max_limit :
        withdraw_amount = float(input("\nEnter your withdrawal amount: "))

        if withdraw_amount > balance :
          print(f"\nInsufficient Balance 😕")
          print(f"Your current balance is: ₹{balance:,.2f}/-")

        elif withdraw_amount <= 0 :
          print("Invalid Amount ⚠️  (amount must be > 0 and <= balance)")

        else :
          break

        withdraw_amount_attempt += 1

      if withdraw_amount_attempt >= max_limit :
        print("\nToo many Invalid Inputs 🚫")
        print("Process Cancelled ⏩⏩")
        
      else :
        # Withdraw Confirmation Validation Loop 
        withdraw_confirm_attempt = 0 

        while withdraw_confirm_attempt < max_limit :
          confirm = input("Are you sure you want to Withdraw? (Y/N): ").upper()

          if confirm == "Y" :
            balance = balance - withdraw_amount 
            
            print(f"\n₹{withdraw_amount:,.2f}/- is Debited from your Account")
            print(f"Your remaining balance is: ₹{balance:,.2f}/-")
            transaction_history.append(f"Withdrew ₹{withdraw_amount:,.2f}")
            break 

          elif confirm == "N" :
            print("\nProcess Cancelled ⏩⏩")
            break 
          
          else :
            withdraw_confirm_attempt += 1 
            remaining = max_limit - withdraw_confirm_attempt

            if remaining > 0 :
              print("Invalid Input ⚠️  Enter (Y/N)")
        
            print(f"{remaining} attempts is left ⚠️\n")

        if withdraw_confirm_attempt >= max_limit :
          print("\nProcess Cancelled ⏩⏩")
    
    elif user_option == "4" :
      if not transaction_history :
        print("No Transactions Recorded")
        
      else :
        print("\n--- Transaction History ---")
        for i, transactions in enumerate(transaction_history, start = 1) :
          print(f"{i}. {transactions}")
    
    elif user_option == "5" :
      print("Exiting ⏩⏩⏩ Exited ✅")
      print("System Locked 🔒")
      break

    else :
      print("Invalid option ❌  Please enter a option (1/2/3/4/5) 😊")

else :
  print("\nSystem Blocked 🚫🔒")
