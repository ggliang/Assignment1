
class Stock:
    __stock_type = []
    def __init__(self,name:str,number:int = 0) -> None:
        self.name = name
        self.number = number
        self.__stock_type.append(name)
    
    def stock_type(self) -> list:
        return self.__stock_type

class Warehouse(Stock):
    global __existed_default_id
    __existed_default_id = []

    def __init__(self) -> None:
        self.id = self.generate_default_id()
        self.storage = {}
        print(f"Warehouse {self.id} is successfully initiated!")

    def generate_default_id(self) -> int:
        if not __existed_default_id:
            __existed_default_id.append(1)
            return __existed_default_id[-1]
        else:
            __existed_default_id.append(__existed_default_id[-1]+1)
            return __existed_default_id[-1]
    
    def update_stock_type(self,stock:Stock) -> None:
        for type in stock.stock_type():
            if type not in self.storage.keys():
                self.storage[type] = 0
    
    def add_stock(self,stock:Stock) -> None:
        self.update_stock_type(stock)
        self.storage[stock.name] += stock.number

    def remove_stock(self,stock:Stock) -> None:
        self.update_stock_type(stock)
        assert stock.number>0, f"Only positive number allowed"
        assert stock.number<=self.storage[stock.name], f"The storage is not enough, current available {stock.name} is {self.storage[stock.name]}"
        self.storage[stock.name] -= stock.number
    
    def get_num_stock(self,name) -> int:
        print("The number of",name,"in Warehouse",self.id,"is",self.storage[name])
        return self.storage[name]
    
    def get_all_stock_status(self) -> dict:
        print("Warehouse",self.id,self.storage)
        return self.storage
    
    def move_stock_to(self,warehouse2,stock:Stock) -> None:
        temp_stock = stock
        self.remove_stock(stock)
        warehouse2.add_stock(stock)
        print("Stock",stock.name,"of",stock.number,"successfully move from warehouse",self.id
        ,"to warehouse",warehouse2.id)

if __name__ == "__main__":
    w1 = Warehouse()
    apple = Stock("Apple",4)
    banana = Stock("Banana",5)
    w1.add_stock(apple)
    w1.add_stock(banana)
    w1.remove_stock(Stock("Apple",1))
    w1.get_num_stock('Apple')
    w1.get_all_stock_status()
    w2 = Warehouse()
    w1.move_stock_to(w2,Stock("Banana",3))
    w1.get_all_stock_status()
    w2.get_all_stock_status()