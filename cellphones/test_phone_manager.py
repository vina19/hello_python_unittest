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
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')
        testPhone3 = Phone(1, 'Apple', 'iPhone 7')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
            
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)
            testAssignmentMgr.add_phone(testPhone3)


    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        testEmployee1 = Employee(1, 'Marissa')
        testEmployee2 = Employee(2, 'Christine')

        testEmployess = [ testEmployee1, testEmployee2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

        self.assertCountEqual(testEmployess, testAssignmentMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        testEmployee1 = Employee(1, 'Marissa')
        testEmployee2 = Employee(1, 'Christine')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmployee2)


    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments
        testEmployee1 = Employee(1, 'Marissa')
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)

        self.assertEqual(testEmployee1.id, testPhone1.employee_id)
        

    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.
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
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.
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
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        testEmployee1 = Employee(1, 'Marissa')

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)
        self.assertTrue(testEmployee1.id, testPhone1.employee_id)


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        testEmployee1 = Employee(1, 'Marissa')
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)
        testAssignmentMgr.un_assign(testPhone1.id)

        self.assertEqual(None, testAssignmentMgr.phone_info(testEmployee1))


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist
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

        self.assertEqual(None, testAssignmentMgr.phone_info(testEmployee3))

        with self.assertRaises(PhoneError):
            testAssignmentMgr.phone_info(testEmployee4)

        
