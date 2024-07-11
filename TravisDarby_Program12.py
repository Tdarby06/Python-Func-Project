#***************************************************************
#
#  Developer:         Travis Darby
#
#  Program #:         12
#
#  File Name:         TravisDarby_Program12.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Course Synonym:    1336-032
#
#  Due Date:          12/6/2020
#
#  Instructor:        Sajjad Mohsin
#
#  Chapter:           <Chapter #5, 6, 7, 8, 9, 10>
#
#  Description:
#     Creates a class called Employee and methods that return attributes such
#     as the employee's name, pay_rate, hours worked, that are then divided
#     into regular and overtime by methods written in the class. There is
#     another method that caluclates the pay, taxes based on gross pay then
#     finds net pay. A __str__ method is also available to print the state of
#     the object. a seperate loop runs the program until the user ends it.
#
#***************************************************************
class Employee:
    #initializes object with the below attributes. Most is undefined until user
    #inputs name, pay_rate, and __hours_by_week. Others are assigned from methods
    def __init__(self):
        self.__name = ''
        self.__pay_rate = 7.25
        self.__monthly_regular_hours = 0.0
        self.__monthly_overtime_hours = 0.0
        self.total_hours_worked = 0.0
        self.__hours_by_week = ''
        self.monthly_regular_pay = 0.0
        self.monthly_overtime_pay = 0.0
        self.monthly_gross_pay = 0.0
        self.monthly_tax_rate = 0.0
        self.monthly_taxes = 0.0
        self.monthly_net_pay = 0.0
    #method to have user input name, pay_rate and hours by week for the employee
    def set_employee_data(self):
        name = input("Enter Employee Name: ")
        pay_rate = float(input("Enter Employee Pay Rate: "))
        weekly_hours_worked = input("Enter Hours Weekly Hours Worked: ")
        #above user input is assigned to below class attributes
        self.__name = name
        self.__pay_rate = pay_rate
        self.__hours_by_week = weekly_hours_worked
    #class method to seperate regular hours and pay and overtime hours and pay
    def set_employee_hours_and_pay(self):
        #constant varaible
        OVERTIME_RATE = 1.5
        #calls seperatley written hour_seperator function to seperate string of
        #hours entered by user into total_hours, regular_hours, and overtime_hours
        total_hours, regular_hours, overtime_hours = hour_seperator(self.__hours_by_week)
        #assigns hours respectively to class related class attributes
        self.total_hours_worked = total_hours
        self.__monthly_regular_hours = regular_hours
        self.__monthly_overtime_hours = overtime_hours
        #uses hours and __pay_rate to establish pay amounts for class attributes
        self.monthly_regular_pay = self.__pay_rate * self.__monthly_regular_hours
        self.monthly_overtime_pay = (self.__pay_rate * OVERTIME_RATE) * self.__monthly_overtime_hours
        self.monthly_gross_pay = self.monthly_regular_pay + self.monthly_overtime_pay
    #method to determine monthly taxes and net_pay for the employee
    def set_taxes_and_netpay(self):
        #constant tax rates
        _10_PERCENT_TAX = .1
        _15_PERCENT_TAX = .15
        _28_PERCENT_TAX = .28
        _31_PERCENT_TAX = .31
        _36_PERCENT_TAX = .36
        #gross pay more than 0 and less than 2,000 taxes = 10%
        if self.monthly_gross_pay > 0 and self.monthly_gross_pay < 2000:
            self.monthly_tax_rate = _10_PERCENT_TAX
        #gross pay more than 2,000 and less than 3,500 taxes = 15%
        elif self.monthly_gross_pay < 3500:
            self.monthly_tax_rate = _15_PERCENT_TAX
        #gross pay more than 2,000 and less than 6,000 taxes = 28%
        elif self.monthly_gross_pay < 6000:
            self.monthly_tax_rate = _28_PERCENT_TAX
        #gross pay more than 6,000 and less than 10,000 taxes = 31%
        elif self.monthly_gross_pay < 10000:
            self.monthly_tax_rate = _31_PERCENT_TAX
        #gross pay more than more than 10,000 taxes = 36%
        else:
            self.monthly_tax_rate = _36_PERCENT_TAX
        #assigns amount to monthly taxes
        self.monthly_taxes = self.monthly_gross_pay * self.monthly_tax_rate
        #assigns amount to monthly net pay
        self.monthly_net_pay = self.monthly_gross_pay - self.monthly_taxes

    #method to return employee name
    def get_employee_name(self):
        return self.__name

    #return method for all of the employee data
    def get_employee_data(self):
        print("Employee Name: \t\t\t", self.__name)
        print("Employee Hourly Pay Rate: \t", '$', format(self.__pay_rate, ',.2f'), sep='')
        print("Employee Regular Hours Worked: ", self.__monthly_regular_hours)
        print("Employee Overtime Hours Worked: ", self.__monthly_overtime_hours)

    #method to return amoutnof monthly_regular_pay for the employee
    def get_employee_monthly_regular_pay(self):
        return self.monthly_regular_pay

    #method to return amount of monthly_overtime_pay for the employee
    def get_employee_monthly_overtime_pay(self):
        return self.monthly_overtime_pay

    #method to return the pay_rate of the employee
    def get_employee_pay_rate(self):
        return self.__pay_rate

    #method to return number of regular hours worked by employee
    def get_employee_regular_hours_worked(self):
        return self.__regular_hours_worked

    #__str__ method to print the state of the object
    def __str__(self):
        return "Employee Name: \t\t" + self.__name + \
                "\nRegular Hours Worked: \t" + str(self.__monthly_regular_hours) + \
                "\nOvertime Hours Worked: \t" + str(self.__monthly_overtime_hours) + \
                "\nTotal Hours Worked: \t" + str(self.total_hours_worked) + \
                "\nHourly Rate: \t\t" + "$" + str(format(self.__pay_rate, ',.2f')) + \
                "\nMonthly Regular Pay: \t" + "$" + str(format(self.monthly_regular_pay, ',.2f')) + \
                "\nMonthly Overtime Pay: \t" + "$" + str(format(self.monthly_overtime_pay, ',.2f')) + \
                "\nMonthly Gross Pay: \t" + "$" + str(format(self.monthly_gross_pay, ',.2f')) + \
                "\nMonthly Taxes: \t\t" + "$" + str(format(self.monthly_taxes, ',.2f')) + \
                "\nMonthly Net Pay: \t" + "$" + str(format(self.monthly_net_pay, ',.2f'))

#***************************************************************
#
#  Function:     hour_seperator
#
#  Description:  function that splits the string of weekly hours entered by the user
#                into total hours, regular hours, and overtime hours
#
#  Parameters:   None
#
#  Returns:     total_hours, regular_hours, overtime_hours
#
#**************************************************************
def hour_seperator(hours_list):
    BASE_HOURS = 40
    total_hours = 0
    regular_hours = 0
    overtime_hours = 0

    for n in hours_list.split():
        total_hours += float(n)
        if float(n) > BASE_HOURS:
            regular_hours += BASE_HOURS
            overtime_hours += float(n) - BASE_HOURS
        else:
            regular_hours += float(n)
    return total_hours, regular_hours, overtime_hours
    #end of hour_seperator function

#***************************************************************
#
#  Function:     program_loop
#
#  Description:  while loop that runs so long as the user enters y. Inside,
#                assigns class to object, runs necessary methods to assign
#                values to all attributes, prints getter methods, and asks
#                user if there is more employee data to enter. function could
#                save employee_obj to dictionary should it be uncommented and
#                asked for.
#
#  Parameters:   None
#
#  Returns:      Nothing
#
#**************************************************************

def program_loop():
    print("Enter employee data? (y/n)", end='')
    user_input = input(": ")

    # employee_dict = {}
    while user_input.lower() == 'y':
        #assigns Employee class to employee_obj variable
        employee_obj = Employee()
        #calls set_employee_data method from class to have user fill in data
        employee_obj.set_employee_data()
        #calls set_employee_hours_and_pay method from class seperate regular and
        #overtime hours and
        employee_obj.set_employee_hours_and_pay()

        employee_obj.set_taxes_and_netpay()

        employee_obj.get_employee_data()
        print()

        print("Employee Monthly Regular Pay: ", employee_obj.get_employee_monthly_regular_pay())
        print()

        print("Employee Monthly Regular Pay: ", employee_obj.get_employee_monthly_overtime_pay())

        print()
        #prints employee object utilizing the __str__ method from the class
        print(employee_obj)

        # name = employee_obj.get_employee_name()
        #
        # employee_dict[str(name)] = employee_obj

        print("Enter employee data? (y/n)", end='')
        user_input = input(": ")

    # return employee_dict
    #end of program_loop function

#***************************************************************
#
#  Function:     main
#
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing
#
#**************************************************************
def main():

    program_loop()

    #end of main function

main()
