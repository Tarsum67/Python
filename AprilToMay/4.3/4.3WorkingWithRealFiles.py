'''
 4.3 Working With Real Files 
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''
def main():
    total = 0.0
    count = 0

    try:
        with open('sales_totals.txt', 'r') as file:
            for line in file:
                try:
                   
                    number = float(line.strip())
                    print(f"{number:,.2f}")  
                    total += number
                    count += 1
                except ValueError:
                    print("Invalid line skipped:", line.strip())

        if count > 0:
            average = total / count
            print(f"\nTotal: {total:,.2f}")
            print(f"Number of entries: {count}")
            print(f"Average: {average:,.2f}")
        else:
            print("No valid numbers found in the file.")

    except IOError:
        print("An Error has occurred. Could not open 'sales_totals.txt'.")


if __name__ == "__main__":
    main()
