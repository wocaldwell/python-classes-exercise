class Employee():
    '''
    This is an employee in a company.
    '''

    def __init__(self, name, job, title, start_date):
        self.name = name
        self.job = job
        self.title = title
        self.start_date = start_date

    def get_employee_name(self):
        '''
        Returns the name of the employee.
        '''

        return self.name

    def get_employee_job(self):
        '''
        Returns the job of the employee.
        '''

        return self.job

    def get_employee_title(self):
        '''
        Returns the title of the employee.
        '''

        return self.title

    def get_employee_start_date(self):
        '''
        Returns the start date of the employee.
        '''

        return self.start_date

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name):
        self.name = name

        self.company_employees = []

    def get_name(self):
        """Returns the name of the company"""

        return self.name

    def get_employees(self):
        '''
        Returns the employee set
        '''
        return self.company_employees




# a company
jobsite = Company('Jobsite')

# some employees
jimmy = Employee('Jimmy', 'Therapist', 'Doctor', '01/22/2000')
johnny = Employee('Johnny', 'Mechanic', 'Senior Technician', '01/23/2000')
jerry = Employee('Jerry', 'Comedian', 'Stand-up', '01/26/2000')

# add the employees to the company
jobsite.company_employees.append(jimmy)
jobsite.company_employees.append(johnny)
jobsite.company_employees.append(jerry)


jobsite_employees = jobsite.get_employees()

for employee in jobsite_employees:
    print(employee.get_employee_name() + ' is an employee at ' + jobsite.get_name())
    print('Their role is ' + employee.get_employee_job() + ' with a title of ' + employee.get_employee_title() + '.')
    print('they started on ' + employee.get_employee_start_date() + '.')
    print('-----------------------------------')
