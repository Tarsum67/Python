
'''
Input Assignment
Name:"Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''
# Ask the user for their total budget
total_budget = float(input("Enter your total monthly budget: $"))

# Create an empty dictionary
categories = {}

# List of spending categories
category_names = ["Housing", "Utilities", "Groceries", "Transportation", "Health Care", "Personal Care", "Clothing", "Debt"]

# Loops through each category 
for category in category_names:
    amount = float(input(f"Enter amount spent on {category}: $"))
    categories[category] = amount  

# Print the budget breakdown
print("\nBUDGET BREAKDOWN:")
print(f"Total Budget: ${total_budget}\n")

for category, amount in categories.items():
    percentage = (amount / total_budget) * 100 if total_budget > 0 else 0
    print(f"{category}: ${amount} ({percentage}%)")