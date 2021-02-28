# Get bill amount from user
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
# Get tip amount
tip = float(
    input("What percentage tip would you like to give? 15, 20, or 25? "))/100 + 1
# Get number of diners
diners = int(input("How many people to split the bill? "))
# Calculate and display each person's total
total_per_person = bill * tip / diners
print(f"Each person should pay ${total_per_person:.2f}")
