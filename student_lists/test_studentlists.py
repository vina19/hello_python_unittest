'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, and asserts the student is removed. Use assertNotIn

    ''' Test if the student is removed from the list by adding the students, remove them, and check that they are not in the list '''
    def test_add_student_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')

        test_class.add_student('Another Test Student')
        test_class.remove_student('Another Test Student')

        self.assertNotIn('Test Student', test_class.class_list)
        self.assertNotIn('Another Test Student', test_class.class_list)


    ## TODO write a test that adds some example students, then removes a student not in the list, and asserts a StudentError is raised

    ''' Test if the student that the user is trying to remove is not in the list '''
    def test_add_student_removed_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Katy Perry')
        test_class.add_student('Adele')
        with self.assertRaises(StudentError):
            test_class.remove_student('Rihanna')

    ## TODO write a test that removes a student from an empty list, and asserts a StudentError is raised

    ''' Test to raised error if the user trying to remove a student from an empty list '''
    def test_remove_student_from_empty_list(self):
        test_class = ClassList(0)
        with self.assertRaises(StudentError):
            test_class.remove_student('Rihanna')
            

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. use assertFalse to verify is_enrolled returns false.

    ''' Test the student that is trying to be enrolled is not in the enrolled student list '''
    def test_student_not_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Adele')
        test_class.add_student('Katy Perry')
        self.assertFalse(test_class.is_enrolled('Rihanna'))
        

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


    ## However, it would be useful to check that index_of_student returns None if a student isn't present.
    ## TODO write a test for index_of_student to assert it returns None if the student is not in the list if the list is empty. use assertIsNone.
    ## TODO write another test when the list is not empty but does not contain the student name, assert that the correct index is returned.
    
    ''' Test for index_of_student return None if the list is empty and the student is not in the list  '''
    def test_index_of_student_none_in_list_or_empty_list(self):
        test_class = ClassList(0)
        self.assertIsNone(test_class.index_of_student('Rihanna'))

    ''' Test for index_of_student return None if the student is not in the list and the list is not empty '''
    def test_list_not_empty_but_does_not_contain_student_name(self):
        test_class = ClassList(2)
        test_class.add_student('Adele')
        test_class.add_student('Rihanna')

        self.assertIsNone(test_class.index_of_student('Emanuel'))


    ## TODO write a test for your new is_class_full method when the class is full. use assertTrue
    ## TODO write a test for your new is_class_full method for when is empty, and when it is not full. Use assertFalse

    ''' Test if the class is full then it is true '''
    def test_is_class_full(self):
        test_class = ClassList(3)
        test_class.add_student('Adele')
        test_class.add_student('Rihanna')
        test_class.add_student('Jacob')
        self.assertTrue(test_class.is_class_full(3))
    
    ''' Test the class is not full or empty '''
    def test_class_not_full(self):
        test_class = ClassList(3)
        self.assertFalse(test_class.is_class_full(0))
        self.assertFalse(test_class.is_class_full(2))
