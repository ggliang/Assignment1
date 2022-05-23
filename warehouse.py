
class Stock:
    '''
    Create the Stock class
    '''
    __stock_type = [] # Create an empty list to record all the types that have been created
    def __init__(self,name:str,number:int = 0) -> None:
        '''
        Initiate function
        '''
        self.name = name # The name of the stock, in str format
        self.number = number # The number of the stock, in int format, by default equals to 0
        self.__stock_type.append(name) # Add the name of the stock to stock_type list
    
    def stock_type(self) -> list:
        '''
        As __stock_type list is private but I need to pass the value to Warehouse class,
        the function is created to ruturn the value of __stock_type, and protect the list
        from outside modification
        '''
        return list(set(self.__stock_type)) # To eliminate repulicated records, transform it into set then list again

class Warehouse(Stock):
    '''
    Create the Warehouse class, and Stock class is inherited
    '''
    __existed_default_id = [] # Create a list to record the id assigning to each warehouse and avoid replicas

    def __init__(self) -> None:
        '''
        Initiate function
        '''
        self.id = self.generate_default_id() # Generate id for each initiated warehouse by using self-defined function generate_default_id
        self.storage = {} # The attribute storage is to record real time storage in dictionary key-value pairs
        print(f"Warehouse {self.id} is successfully initiated!")

    def generate_default_id(self) -> int:
        '''
        Create the function to generate id for each warehouse
        if there is no instance created, then the first warehouse's id will be label 1
        following by 2, 3, 4, and etc.
        '''
        if not self.__existed_default_id:
            self.__existed_default_id.append(1)
            return self.__existed_default_id[-1]
        else:
            self.__existed_default_id.append(self.__existed_default_id[-1]+1)
            return self.__existed_default_id[-1]
    
    def update_stock_type(self) -> None:
        '''
        Each time a stock instance is created, new type of stock might be created as well
        In order to make sure that the warehouse storage dictionary is up-to-date, which means
        having all the stock names as keys, while the number is set to 0
        '''
        for type in Stock.stock_type(Stock):
            if type not in self.storage.keys():
                self.storage[type] = 0 # if the new type doesn't exist in the warehouse, then set the number to 0
    
    def add_stock(self,stock:Stock) -> None:
        '''
        Add stock to current warehouse storage
        '''
        assert stock.number>0, f"Only positive number allowed" #Adding zero or negative number of stocks is meaningless
        self.update_stock_type() # update the stock type make sure that the dictionary keys contain all possible name so no key error would be raised
        self.storage[stock.name] += stock.number # the lastest storage is directly added to previous storage

    def remove_stock(self,stock:Stock) -> None:
        '''
        Remove stock from current warehouse storage
        '''
        self.update_stock_type() # update the stock type make sure that the dictionary keys contain all possible name so no key error would be raised
        assert stock.number>0, f"Only positive number allowed" #Removing zero or negative number of stocks is meaningless
        assert stock.number<=self.storage[stock.name], f"The storage is not enough, current available {stock.name} is {self.storage[stock.name]}"
        self.storage[stock.name] -= stock.number
    
    def get_num_stock(self,name) -> int:
        '''
        Given the name that we want to look for, the function will return the current storage for that cargo in int format
        '''
        self.update_stock_type() # update the stock type make sure that the dictionary keys contain all possible name so no key error would be raised
        print("The number of",name,"in Warehouse",self.id,"is",self.storage[name])
        return self.storage[name]
    
    def get_all_stock_status(self) -> dict:
        '''
        Print the storage dictionary for the entire warehouse
        '''
        self.update_stock_type() # update the stock type make sure that the dictionary keys contain all possible name so no key error would be raised
        print("Warehouse",self.id,self.storage)
        return self.storage
    
    def move_stock_to(self,warehouse2,stock:Stock) -> None:
        '''
        The function is to move stock from one warehouse to another instance warehouse2
        And the stock is a Stock class object, telling what and how much cargo are moving
        the movement can seem as remove stoct from one warehouse then add back to the targeted warehouse
        '''
        self.update_stock_type()# update the stock type make sure that the dictionary keys contain all possible name so no key error would be raised
        self.remove_stock(stock)
        warehouse2.add_stock(stock)
        print("Stock",stock.name,"of",stock.number,"successfully move from warehouse",self.id
        ,"to warehouse",warehouse2.id)

