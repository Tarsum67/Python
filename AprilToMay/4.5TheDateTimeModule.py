'''
4.5: The DateTime Module
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''
# age_calculator.py

from datetime import datetime, timedelta

def main():
    try:
        
        year = int(input("What year were you born? "))
        month = int(input("What month were you born (as a number)? "))
        day = int(input("What day of the month were you born? "))

       
        birthday = datetime(year, month, day)
        print(f"\nYour birthday is: {birthday.date()}")

       
        now = datetime.now()

      
        age_difference = now - birthday

        
        print(f"Difference is {age_difference.days} days")

      
        years = age_difference.days / 365.25
        print(f"You are {years:.1f} years old")

       
        months = years * 12
        print(f"That's approximately {int(months)} months")

      
        weeks = age_difference.days // 7
        print(f"Or {weeks} weeks")

       
        hours = age_difference.total_seconds() // 3600
        print(f"Or {int(hours)} hours")

       
        minutes = age_difference.total_seconds() // 60
        print(f"Or {int(minutes)} minutes")

    except ValueError:
        print("Invalid input! Please enter numbers only for the year, month, and day.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
