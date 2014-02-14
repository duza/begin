''' It is the program for description of a good,which it cost some price '''

week = ("Monday", "Tuesday","Wednesday", "Thirsday","Friday",
            "Saturday", "Sunday")

class Purchase:
    ''' Purchase(str, int, int, str) -> object

    Class Purchase describes simple purchases.
    Method __init__ accept four parametrs: name of good, price, number 
    and day of purchase. Methods getters and setters of fields realize with 
    help decorators and fuction property. Method ToString output values 
    of fields in csv format. Method GetCost calculates cost purchase of all
     number goods in this day and return it. Method CompareTo accept one
    parametr(object) and compare two objects: self and object-parametr.     '''

    def __init__(self, name="beer", price=14000, number=7, day="Friday"):

        self.__nameItem = check(name, str)
        self.__priceBrItem = check(price, int)
        self.__numberOfItems = check(number, int)  
        if isinstance(day, str) and (day in week):
            self.__day = day
        else:
            raise AttributeError("Incorrect input field 'day' !")
    
    @property
    def nameItem(self):
        return self.__nameItem

    @property
    def priceBrItem(self):
        return self.__priceBrItem

    @property
    def numberOfItems(self):
        return self.__numberOfItems

    @property 
    def day(self):
        return self.__day

    @nameItem.setter
    def nameItem(self, x):
        self.__nameItem = check(x, str)
        
    @priceBrItem.setter
    def priceBrIterm(self, x):
        self.__priceBrItem = check(x, int)

    @numberOfItems.setter
    def numberOfItems(self, x):
        self.__numberOfItems = check(x, int)        

    @day.setter
    def day(self, x):
        if isinstance(day, str) and (day in week):
            self.__day = x
        else:
            raise AttributeError("Incorrect input field 'day' !")

    def GetCost(self):
        return  self.priceBrItem * self.numberOfItems

    def __str__(self):
        return "%s;%d;%d;%s;%d" %(self.nameItem, self.priceBrItem,
         self.numberOfItems, self.day, self.GetCost())

    def CompareTo(self, object):
        return self.GetCost() - object.GetCost()

def check(val, type):
    if isinstance(val, type):
        return val
    else:
        raise AttributeError("Incorrect input field !")

def main():
    purchases = [ Purchase("shoes", 420000, 2, "Monday"), 
    Purchase('icecream', 20000, 5, "Tuesday"), 
    Purchase('bread', 8000, 3,"Wednesday"), Purchase(), 
    Purchase('fast-food',4200000,2,"Saturday") ]
    sumPurchases = 0
    for each in purchases:
        print each
        sumPurchases += each.GetCost()
    middleCost = sumPurchases / len(purchases)
    print "Middle cost %.0f" % middleCost
    OdayWithMaxCostPurchase = max(purchases, key= lambda x: x.GetCost())
    print "Day with max cost of purchase: %s" % OdayWithMaxCostPurchase.day
    purchases.sort(key=lambda x: x.GetCost())
    for el in purchases: 
        print el   # Output sortting purchases list
    print purchases[0].CompareTo(purchases[4]) # Example of work method CompareTo

if __name__ == '__main__':
    main()
