'''
3.5.1.1. OOP Fundamentals: Inheritance
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''


class Employee:
    def __init__(self, name, employee_number):
        self._name = name
        self._employee_number = employee_number

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_employee_number(self):
        return self._employee_number

    def set_employee_number(self, number):
        self._employee_number = number


class ProductionWorker(Employee):
    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(name, employee_number)
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self._shift_number

    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_hourly_pay_rate(self, pay_rate):
        self._hourly_pay_rate = pay_rate

    def get_shift_name(self):
        return "Day" if self._shift_number == 1 else "Night"


def main():
    print("Enter the following details of the Employee")
    print("--------------------------------------------")

    name = input("Enter Employee Name: ")
    emp_number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number (1 for Day, 2 for Night): "))

 
    worker = ProductionWorker(name, emp_number, shift_number, pay_rate)

    print("-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_employee_number()}")
    print(f"Shift: {worker.get_shift_name()}")
    print(f"Pay Rate: {worker.get_hourly_pay_rate():.2f}")


if __name__ == "__main__":
    main()
