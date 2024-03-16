# Define global variables
customer_data = {
}  # Empty dictionary to store customer data (name, account_number, balance)
current_user = None  # Variable to store current user account number
acnt = 10100


# Function to display main menu
def main_menu():
  print("\n--- Bank Management System ---")
  print("1. Create Account")
  print("2. Deposit")
  print("3. Debit")
  print("4. Transfer Funds ")
  print("5. Account holder list")
  print("6. Close Account")
  print("7. Modify Name")
  print("8. Check Balance")
  print("9. Exit")
  choice = int(input("Enter your choice: "))
  return choice


# Function for creating a new account
def create_account():

  name = input("Enter your name: ")
  global acnt
  acnt += 1
  account_number = acnt
  balance = float(input("Enter initial deposit: "))
  # {key: value}

  # {account_num: {name: name, balance: balance}} value is dictionary
  # customer_data[101]['balance']
  customer_data[account_number] = {"name": name, "balance": balance}
  print("Account created successfully. Your account number is: ",
        account_number)

  global current_user
  current_user = account_number


# Function for depositing money
def deposit():
  if not current_user:  # None -> !0 -> 1
    print("Please login to your account.")
    return
  account_number = current_user
  amount = float(input("Enter amount to deposit: "))
  # {acnt num : {name : name, balance : balance}}
  customer_data[account_number]["balance"] += amount
  # f string gives a functionality to embed values inside a string from our local or global variables
  print(
      f"Deposited {amount:.2f}. New balance: {customer_data[account_number]['balance']:.2f}"
  )


# function for debiting money
def debit():
  if not current_user:
    print("Please login to your account.")
    return

  account_number = current_user
  amount = float(input("Enter amount to debit: "))
  available_amt = customer_data[account_number]["balance"]
  if amount > available_amt:
    print("Transaction cannot be processed because of fund unavailability")
    return

  customer_data[account_number]["balance"] -= amount
  print(
      f"Debited {amount:.2f}. New balance: {customer_data[account_number]['balance']:.2f}"
  )


# Function with placeholders for unavailable features
def transfer_funds():
  print("This feature requires verification and is unavailable at this time.")


# funtion for account holder list
def account_holder_list():
  print("Account Holder List".center(70, '-'))
  # {key,val
  # key:val,
  # key:val}
  for acntNum, data in customer_data.items():
    print(acntNum, data['name'], data['balance'])


#function for closing the account
def close_account():
  if not current_user:
    print("Please login to your account.")
    return

  account_number = current_user
  del customer_data[account_number]
  print("Your account closed")


#function for modifying the name
def modify_name():
  if not current_user:
    print("Please login to your account.")
    return

  account_number = current_user
  new_name = input("Enter new name: ")
  customer_data[account_number]['name'] = new_name
  print(f"Name changed to {new_name}")


# Function to check balance
def check_balance():
  if not current_user:
    print("Please login to your account.")
    return
  account_number = current_user
  print(f"Your balance is: {customer_data[account_number]['balance']:.2f}")


# Main loop in which all the function are clled
while True:
  choice = main_menu()

  if choice == 1:
    create_account()
  elif choice == 2:
    deposit()
  elif choice == 3:
    debit()
  elif choice == 4:
    transfer_funds()
  elif choice == 5:
    account_holder_list()
  elif choice == 6:
    close_account()
  elif choice == 7:
    modify_name()
  elif choice == 8:
    check_balance()
  elif choice == 9:
    print("Exiting Bank Management System.")
    break
  else:
    print("Invalid choice. Please try again.")
