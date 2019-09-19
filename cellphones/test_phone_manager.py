import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        
        # Test raise PhoneError for adding the same phone ID
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')
        testPhone3 = Phone(1, 'Apple', 'iPhone 7')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
            
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)
            testAssignmentMgr.add_phone(testPhone3)


    def test_create_and_add_new_employee(self):
        
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        testEmployee1 = Employee(1, 'Marissa')
        testEmployee2 = Employee(2, 'Christine')

        testEmployess = [ testEmployee1, testEmployee2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

        self.assertCountEqual(testEmployess, testAssignmentMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        
        # Test raise PhoneError for adding the same employee ID
        testEmployee1 = Employee(1, 'Marissa')
        testEmployee2 = Employee(1, 'Christine')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmployee2)


    def test_assign_phone_to_employee(self):
        
        # Test employee assigned to the phone correctly
        testEmployee1 = Employee(1, 'Marissa')
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)

        self.assertEqual(testEmployee1.id, testPhone1.employee_id) # Check that employee id is equal to phone employee id.
        

    def test_assign_phone_that_has_already_been_assigned_to_employee(self):

        # Throws an exception if the phone is alreaady assigned.
        testEmployee1 = Employee(1, 'Marissa')
        testEmployee2 = Employee(2, 'Christine')

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone1.id, testEmployee2)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        
        # Raises a PhoneError if employee who already has a phone get assigned to a different phone
        testEmployee1 = Employee(1, 'Marissa')

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone2.id, testEmployee1)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        
        # Test it is true that the employee assigned to current phone they assigned to
        testEmployee1 = Employee(1, 'Marissa')

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)
        self.assertTrue(testEmployee1.id, testPhone1.employee_id)


    def test_un_assign_phone(self):
        
        # Test unassign employee equal to None
        testEmployee1 = Employee(1, 'Marissa')
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)
        testAssignmentMgr.un_assign(testPhone1.id)

        self.assertEqual(None, testAssignmentMgr.phone_info(testEmployee1))


    def test_get_phone_info_for_employee(self):

        # Test if correct phone info is returned
        testEmployee1 = Employee(1, 'Marissa')
        testEmployee2 = Employee(2, 'Christine')
        testEmployee3 = Employee(3, 'Kimarlee')
        testEmployee4 = Employee(4, 'Jennifer')

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)
        testAssignmentMgr.add_employee(testEmployee3)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)
        testAssignmentMgr.assign(testPhone2.id, testEmployee2)

        self.assertTrue(testPhone1.id, testAssignmentMgr.phone_info(testEmployee1))
        self.assertTrue(testPhone2.id, testAssignmentMgr.phone_info(testEmployee2))

        # Return None for testEmployee3 who does not have a phone
        self.assertEqual(None, testAssignmentMgr.phone_info(testEmployee3))

        # Raises PhoneError for testEmployee4 who has not been added 
        with self.assertRaises(PhoneError):
            testAssignmentMgr.phone_info(testEmployee4)

        
