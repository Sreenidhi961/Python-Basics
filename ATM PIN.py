correct_pin=4321
attempts=0
while attempts<3:
    pin = int(input("Enter your4-digit PIN:"))
    if pin == correct_pin:
        print("Access Granted.")
        break
    else:
        attempts += 1
        print(f"Wrong PIN. {3-attempts} attempt(s) left.")
else:
    print("Account Blocked. Too many mismatch")
