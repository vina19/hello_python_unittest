# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):

        # Raise exception if employee id in a list has the same id 
        for e in self.employees:
            if employee.id == e.id:
                raise PhoneError('Employee ID is taken')
        
        # Add employee to the list if employee is not in the list
        # or raise exception if employee already in the list 
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            raise PhoneError('Employee with the same ID already added')

    def add_phone(self, phone):
        
        # Raise exception if phone id in a list has the same id
        for p in self.phones:
            if phone.id == p.id:
                raise PhoneError('Phone ID is taken')
        
        # Add phone to the list if phone is not in the list
        # or raise exception if phone already in the list 
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            raise PhoneError('Phone with the same ID already added')

    def assign(self, phone_id, employee):

        # Find phone in phones list
        for phone in self.phones:

            # Raise exception if the phone already assigned to the employee.
            if phone.employee_id == employee.id:
                raise PhoneError('Employee already has a phone')
            
            # Raise exception to phone that already assigned to an employee 
            if phone.id == phone_id:
                if (phone.is_assigned() == True):
                    raise PhoneError('Phone is already assigned to an employee')
                else:
                    phone.assign(employee.id)
            

    def un_assign(self, phone_id):

        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):

        # Find phone for employee in phones list
        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

            # Raise an exception if the employee does not exist
            if employee not in self.employees:
                raise PhoneError('The employee does not exist')

        return None # Return None if the employee does not have a phone

    
class PhoneError(Exception):
    pass
