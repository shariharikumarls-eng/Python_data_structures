#Account Login
username = 'Shari'
password = '03061994' 


user = input ("Enter username: ")
pwd = input ("Enter password: ")

#Sucessful login
if user == username and pwd == password:
    print ("Login Sucessful!")

else: 
    print ("Enter valid credential")

#Deposit cash
#initial balance
balance = 10000

#enter amt to be deposited
amount = float(input("Enter amount to be deposited: "))

#check deposit amt greater than zero
if amount > 0:
   balance += amount
   print("Deposit sucessful")
   print("Current balance:", balance)
else:
   print("Deposit amount must be greater than zero")

#check amount withdrawal
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal > 0 and withdrawal <= balance:
     balance -= withdrawal 
     print ("Collect your cash")
     print ("Current balance:", balance)

elif withdrawal <= 0:
    print("withdrawal amt must be greater than zero")
else:
    print("withdrawal exeeds available balance")
