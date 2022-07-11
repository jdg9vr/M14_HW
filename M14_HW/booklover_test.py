import pandas as pd
import numpy as np
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        me = BookLover("Josh", "jdg9vr@virginia.edu", "Mystery")
        me.add_book("Death on the Nile", 4)
        print(me.book_list)
        
        expected = "Death on the Nile"
        self.assertEqual(me.book_list['book_name'].values, expected)
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        me = BookLover("Josh", "jdg9vr@virginia.edu", "Mystery")
        me.add_book("Death on the Nile", 4)
        me.add_book("Death on the Nile", 4)
        print(me.book_list)
        
        expected = "Death on the Nile"
        self.assertEqual(me.book_list['book_name'].values, expected)
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        me = BookLover("Josh", "jdg9vr@virginia.edu", "Mystery")
        me.add_book("Death on the Nile", 4)
        print(me.has_read("Death on the Nile"))
        
        self.assertTrue(me.has_read("Death on the Nile"))
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        me = BookLover("Josh", "jdg9vr@virginia.edu", "Mystery")
        me.add_book("Death on the Nile", 4)
        print(me.has_read("And Then There Were None"))
        
        self.assertFalse(me.has_read("And Then There Were None"))
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        me = BookLover("Josh", "jdg9vr@virginia.edu", "Mystery")
        me.add_book("Death on the Nile", 4)
        me.add_book("And Then There Were None", 3)
        me.add_book("Murder on the Orient Express", 5)
        print(me.num_books)
        
        expected = 3        
        self.assertEqual(me.num_books, expected)
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        me = BookLover("Josh", "jdg9vr@virginia.edu", "Mystery")
        me.add_book("Death on the Nile", 2)
        me.add_book("And Then There Were None", 4)
        me.add_book("Murder on the Orient Express", 5)
        print(me.fav_books())
        
        self.assertEqual(sum(me.fav_books()['book_rating'].values>3), 2)
        
if __name__ == '__main__':

    unittest.main(verbosity=3)
