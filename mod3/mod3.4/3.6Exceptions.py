'''
3.6 Exceptions Again
Name: "Travis Routhier"
https://github.com/Tarsum67/Python/tree/main/mod3/mod3.4"
'''
 

class NotNumericError(Exception):
  
    def __init__(self, input_value, message="Input must be a numeric value."):
        self.input_value = input_value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"'{self.input_value}' is an invalid input. {self.message}"


def get_numeric_input():
    while True:
        try:
            user_input = input("Enter a number: ")
            if not user_input.isnumeric():
                raise NotNumericError(user_input)
        except NotNumericError as e:
            print(f"Error: {e} ")
        else:
            print(f"Valid input received: {user_input}")
            break
        finally:
            print("Input checked.\n")


def main():
    print("Enter a number to start program\n")
    get_numeric_input()
    print("Program completed successfully.")


if __name__ == "__main__":
    main()
