'''
4.2 Processing Files
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''



import os


def original_main():

    date_time = input("Enter the current date and time: ")
    entry = input("Enter your diary entry: ")

    try:
        with open("diary.txt", "a") as file:
            file.write(f"{date_time}\n{entry}\n\n")
        print("Diary entry saved successfully.")
    except Exception as e:
        print("An error occurred while writing to the diary:", e)

def main():
    date_time = input("Enter the current date and time: ")
    entry = input("Enter your diary entry: ")

    try:
       
        with open("diary.txt", "a") as file:
            file.write(f"{date_time}\n{entry}\n\n")

        print("Diary entry saved to: diary.txt")
    except Exception as e:
        print("An error occurred while writing to the diary:", e)

if __name__ == "__main__":
    main()







