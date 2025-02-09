
'''
Input Assignment
Name:"Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''
# Ask the user for their input
Housing = float(input("Enter your housing cost: $"))
Utilities = float(input("Enter your utilities cost: $"))
Groceries = float(input("Enter your groceries cost: $"))
Transportation = float(input("Enter your transportation cost: $"))
HealthCare = float(input("Enter your healthcare cost: $"))
PersonalCare = float(input("Enter your personal care cost: $"))
Clothing = float(input("Enter your clothing cost: $"))
Debt = float(input("Enter your debt cost: $"))

# Add up to get total budget
total_budget = Housing + Utilities + Groceries + Transportation + HealthCare + PersonalCare + Clothing + Debt

# Calculate the percentage of the total budget 
housing_percentage = (Housing / total_budget) * 100
utilities_percentage = (Utilities / total_budget) * 100
groceries_percentage = (Groceries / total_budget) * 100
transportation_percentage = (Transportation / total_budget) * 100
healthcare_percentage = (HealthCare / total_budget) * 100
personalCare_percentage = (PersonalCare / total_budget) * 100
clothing_percentage = (Clothing / total_budget) * 100
debt_percentage = (Debt / total_budget) * 100

# PRint the total budget brake down
print(f"\nTotal Budget: ${total_budget:.2f}")
print("Budget Breakdown:")
print(f"Housing: ${Housing:.2f} ({housing_percentage:.2f}%)")
print(f"Utilities: ${Utilities:.2f} ({utilities_percentage:.2f}%)")
print(f"Groceries: ${Groceries:.2f} ({groceries_percentage:.2f}%)")
print(f"Transportation: ${Transportation:.2f} ({transportation_percentage:.2f}%)")
print(f"Health Care: ${HealthCare:.2f} ({healthcare_percentage:.2f}%)")
print(f"Personal Care: ${PersonalCare:.2f} ({personalCare_percentage:.2f}%)")
print(f"Clothing: ${Clothing:.2f} ({clothing_percentage:.2f}%)")
print(f"Debt: ${Debt:.2f} ({debt_percentage:.2f}%)")
