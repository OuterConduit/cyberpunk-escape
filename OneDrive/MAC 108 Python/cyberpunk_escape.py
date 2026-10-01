print("=== MAINFRAME INFILTRATION ===")
print("ALERT: Security lockdown triggered. Drones are approaching.")
hacker_alias = input("Enter your Hacker Alias: ")
print(f"\nAlright, {hacker_alias}, we need to get you out of here.")
print("You reach a locked blast door with two override terminals: RED and BLUE.")
terminal_choice = input("Which terminal do you plug into? (red/blue): ").lower()
if terminal_choice == "red":
    print(f"\n{hacker_alias}, the RED terminal requires a numeric security code to proceed.")
    print("HINT: It's the standard web error code for 'Not Found'.")
passcode = int(input("Enter the 3-digit numeric passcode: "))
if passcode == 404:
        print(f"\nACCESS GRANTED. The blast door opens! {hacker_alias} successfully escapes into the neon night!")
elif passcode != 404:
        print(f"\nACCESS DENIED. Incorrect code. The security drones have caught {hacker_alias}!")
elif terminal_choice == "blue":
    print(f"\n{hacker_alias} plugs into the BLUE terminal... It's a trap!")
    print("The system overloads your cyber-deck. The security drones have caught you!")
else:
    print(f"\nCommand not recognized. While {hacker_alias} hesitated, the security drones arrived. You are captured!")
