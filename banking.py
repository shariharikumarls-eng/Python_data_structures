# Account Login
username = "Shari"
password = "03061994"

#Get user input for login
user = input("Enter username: ")
pwd = input("Enter password: ")

#validate user credentials
if user == username and pwd == password:
    print("Login Successful!")

    # Initial Balance
    balance = 10000

    # Deposit Cash
    amount = float(input("Enter amount to be deposited: "))

    if amount > 0:
        balance += amount
        print("Deposit Successful")
        print("Current balance:", balance)
    else:
        print("Deposit amount must be greater than zero")

    # Withdrawal
    withdrawal = float(input("Enter withdrawal amount: "))

    if withdrawal > 0 and withdrawal <= balance:
        balance -= withdrawal
        print("Collect your cash")
        print("Current balance:", balance)

    elif withdrawal <= 0:
        print("Withdrawal amount must be greater than zero")

    else:
        print("Withdrawal exceeds available balance")

else:
     print("Invalid username or password.")
     print("Banking operations cannot be performed.")
