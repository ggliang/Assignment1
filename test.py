from warehouse import Warehouse
from warehouse import Stock
import unittest

class TestStock(unittest.TestCase):
    '''
    Build the first TestCase to test the statability of Stock Class
    '''
    def setUp(self) -> None:
        '''
        SetUp function is to preset the variable that I will use in each test case
        Stock Apple, Banana, and Cherry are created
        '''
        self.apple1 = Stock("Apple",3)
        self.banana1 = Stock("Banana",4)
        self.cherry1 = Stock("Cherry",2)
    
    def test_a_initiate_stock(self):
        '''
        The name and corresponding number of each stock is checked
        '''
        self.assertEqual(self.apple1.name,"Apple")
        self.assertEqual(self.banana1.name,"Banana")
        self.assertEqual(self.cherry1.name,"Cherry")
        self.assertEqual(self.apple1.number,3)
        self.assertEqual(self.banana1.number,4)
        self.assertEqual(self.cherry1.number,2)
    
    
    def test_b_stock_type(self):
        '''
        The function stock_type is able to correctly return the existing type list
        '''
        temp = Stock.stock_type(Stock) #the stock_type might not necessarily in alphabit order so I have to manually sort it
        temp.sort()
        self.assertEqual(temp,["Apple","Banana","Cherry"])
    
    @unittest.expectedFailure
    def test_c_stock_type_private(self):
        '''
        To check whether __stock_type is private or not
        '''
        print(Stock.__stock_type)
    


class TestWarehouse(unittest.TestCase):
    '''
    Build the second TestCase to test the statability of Warehouse Class
    '''
    global w1 #The warehouse instances are unique with ID, so it's impropriate to put them into setUp, otherwise, each test would create two new warehouse object
    global w2
    w1 = Warehouse()
    w2 = Warehouse()
    def setUp(self) -> None:
        '''
        Stock Apple, Banana, and Cherry are created, while apple stock has two objects
        '''
        self.apple1 = Stock("Apple",3)
        self.banana1 = Stock("Banana",4)
        self.apple2 = Stock("Apple",2)
        self.cherry1 = Stock("Cherry",2)
    
    def test_a_initiate_warehouse(self):
        '''
        To check the ids of newly created warehouse objects w1,w2
        '''
        self.assertEqual(w1.id,1)
        self.assertEqual(w2.id,2)

    def test_b_add_stock(self):
        '''
        apple1 and banana1 are added to warehouse 1 while cherry1 is added to warehouse 2
        Then the storages of each warehouse are tested
        '''
        w1.add_stock(self.apple1)
        w1.add_stock(self.banana1)
        w2.add_stock(self.cherry1)
        self.assertEqual(w1.storage,{"Apple":3,"Banana":4,"Cherry":0})
        self.assertEqual(w2.storage,{"Apple":0,"Banana":0,"Cherry":2})
    
    def test_c_remove_stock(self):
        '''
        2 apples are removed from warehouse1, therefore, the apple storage of warehouse 1 decreases by one
        and there is no impact on warehouse2
        '''
        w1.remove_stock(self.apple2)
        self.assertEqual(w1.storage,{"Apple":1,"Banana":4,"Cherry":0})
        self.assertEqual(w2.storage,{"Apple":0,"Banana":0,"Cherry":2})

    @unittest.expectedFailure
    def test_d_remove_stock(self):
        '''
        Current apple stock in warehouse 1 is 1, therefore, it cannot remove 2 more apple, an error would be raise here
        Using expectedFailure would tell the test function we will have an expected error 
        '''
        w1.remove_stock(self.apple2)
        self.assertEqual(w1.storage,{"Apple":-1,"Banana":4,"Cherry":0})

    def test_e_get_num_stock(self):
        '''
        Given the name of the stock, the get_num_stock function shall return the current storage number
        '''
        self.assertEqual(w1.get_num_stock("Apple"),1)
        self.assertEqual(w2.get_num_stock("Cherry"),2)
    
    @unittest.expectedFailure
    def test_f_get_num_stock2(self):
        '''
        "apple" is not in the warehouse since the first letter shall be upper case
        '''
        self.assertEqual(w1.get_num_stock("apple"),1)

    def test_g_get_all_stock_status(self):
        '''
        get_all_stock_status would return the entire storage of each warehouse correctly
        '''
        self.assertEqual(w1.get_all_stock_status(),{"Apple":1,"Banana":4,"Cherry":0})
        self.assertEqual(w2.get_all_stock_status(),{"Apple":0,"Banana":0,"Cherry":2})
    
    def test_h_move_stock_to(self):
        '''
        1 apple is move from warehouse 1 to warehouse 2,
        and 1 cherry is move from warehouse 2 to warehouse 1
        Check whether the entire storage status is robust
        '''
        w1.move_stock_to(w2,Stock("Apple",1))
        w2.move_stock_to(w1,Stock("Cherry",1))
        self.assertEqual(w1.get_all_stock_status(),{"Apple":0,"Banana":4,"Cherry":1})
        self.assertEqual(w2.get_all_stock_status(),{"Apple":1,"Banana":0,"Cherry":1})

if __name__ == "__main__":
    unittest.main() # Inititate the test.py file