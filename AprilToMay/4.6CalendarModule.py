'''
4.6: The Calender Module
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''
import calendar
import datetime

def main():
   
    current_year = datetime.datetime.now().year

    
    try:
        month = int(input("Enter your birth month (1-12): "))

       
        if 1 <= month <= 12:
         
            calendar.setfirstweekday(calendar.SUNDAY)

          
            print(f"\nHere is your birthday month calendar for {current_year}:\n")
            print(calendar.month(current_year, month))
        else:
            print("Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a numeric value between 1 and 12.")


if __name__ == "__main__":
    main()
