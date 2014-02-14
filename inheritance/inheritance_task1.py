# -*- coding: utf-8 -*-
''' It is the program describes purchase of some product'''
from collections import  OrderedDict

__metaclass__ = type

class BasicPurchase:
    """BasicPurchase(str, int, int) -> instance
        Class BasicPurchase describes simple purchases.
        Methods defined here:
        
        __init__(self,product name, price, number of units) -> instance
        with fields __productName, __priceBr, __numberUnits.
        
        Methods getters and setters realize with help decorators and
         fuction property. Example:
        productName -> self. __productName
        productName = x  <=> self.__productName = x

        GetCost(self) -> self.__priceBr * self.__numberUnits
        Method GetCost calculates cost purchase of all number of 
        product and returns it.
    
        ToString(self) -> product;price;number;cost
        Method ToString output values of fields in csv format.

        Equals(self, object) -> True or False
        Method compares two objects: self and object-parametr.
        If the price and name of all products are same return True 
        else return False.     

    """
    def __init__(self, product="potato", price=4200, number=1):
        self.__productName = check(product,str)
        self.__priceBr = check(price,int)
        self.__numberUnits = check(number,int)

    @property
    def productName(self):
        return self.__productName

    @productName.setter
    def productName(self, value):
        self.__productName = check(value,str)

    @property
    def priceBr(self):
        return self.__priceBr

    @priceBr.setter
    def priceBr(self, value):
        self.__priceBr = check(value,int)

    @property
    def numberUnits(self):
        return self.__numberUnits

    @numberUnits.setter
    def numberUnits(self, value):
        self.__numberUnits = check(value,int)

    def GetCost(self):
        return  self.priceBr * self.numberUnits

    # def ToString(self):
    #     return "{product};{price};{number};{cost}".format(\
    #     product=self.productName, price=self.priceBr,
    #      number=self.numberUnits, cost=self.GetCost())

    def ToString(self):
        tut = OrderedDict(sorted(self.__dict__.items(), key=lambda x: x[0][9]))
        return ";".join([str(tut[key]) for key in tut ])
        # return ';'.join([str(self.__dict__[key]) for key in sorted(self.__dict__,reverse=True)])

    def __str__(self):
        return self.ToString()

    def Equals(self, object):
            if  (self.productName is object.productName) and \
            (self.priceBr is object.priceBr):
                return True
            else:
                return False

class FixDiscountPurchase(BasicPurchase):
    """FixDiscountPurchase(str, int, int, int) -> instance
        Class FixDiscountPurchase describes simple purchase with
        discount from price. Class inherits field and methods of class
        BasicPurchase.
    
        Methods defined here:
        
        __init__(self,product name, price, number of units, discount) -> instance
        with fields __productName, __priceBr, __numberUnits, __discount.

        Methods GetCost an ToString are overridden, but the essence is the same.
    """
    def __init__(self, product="potato", price=4200,
     number=1, discount=3):
        super(FixDiscountPurchase, self).__init__(product,
            price, number)
        self.__discount = check(discount,int) 

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = check(value,int)

    def GetCost(self):
        return  self.priceBr * (1- float(self.discount)/100) * self.numberUnits

    # def ToString(self):
    #     return "{product};{price};{number};{discount};{cost:.0f}"\
    #     .format(product=self.productName, price=self.priceBr,
    #      discount=self.discount, number=self.numberUnits,
    #      cost=self.GetCost())

class DiscountPricePurchase(BasicPurchase):
    """DiscountPricePurchase(str, int, int) -> instance
        Class DiscountPricePurchase describes simple purchase with
        discount when purchasing a product more constanst WHOLESALE.
        Class inherits field and methods of class BasicPurchase.
    
        Methods defined here:
        
        __init__(self,product name, price, number of units) -> instance
        with fields __productName, __priceBr, __numberUnits, __discount.

        Methods GetCost an ToString are overridden, but the essence is the same.
    """
    WHOLESALE = 10
    def __init__(self, product="potato", price=4200, number=1,discount=5):
        super(DiscountPricePurchase, self).__init__(product, price,
            number)
        if self.numberUnits >= self.WHOLESALE:
            self.__discount = discount
        else:
            self.__discount = 0

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = check(value,int)

    def GetCost(self):
        return  (1 - float(self.discount)/100)*self.priceBr * self.numberUnits

    # def ToString(self):
    #     return "{product};{price};{number};{discount};{cost:.0f}"\
    #     .format(discount=self.discount, product=self.productName,
    #      price=self.priceBr, number=self.numberUnits, 
    #      cost=self.GetCost())

def check(value, type):
    ''' Function checks the type of the input field of class '''
    if isinstance(value, type):
        return value
    else:
        raise AttributeError("Incorrect {0} field type {1} !".format(value, type))

def main():
    '''
    Function main() describes creation list of purchases belong different classes.
    Implemented output of all elements, finding purchase with maximum cost and
    check : 'are all purchases equal?'
    '''
    try:
        array = [BasicPurchase('bread',7900,2),
    FixDiscountPurchase('beer',14000,4,7),
    DiscountPricePurchase('milk',7500,2),
    BasicPurchase(),
    FixDiscountPurchase('ice-cream',9500,3,3),
    DiscountPricePurchase('chips',10000,21)]
        sample = list()
        sample.append(array[0].Equals(array[1]))
        for index, element in enumerate(array):
            print element, element.__class__.__name__
            if 0 < index < len(array) - 1:
                sample.append(element.Equals(array[index+1]))
        print "Max purchase is",max(array, key=lambda x: x.GetCost())
        print 'Are all purchases equal?',all(sample)

    except Exception as error:
        print "Error {err}".format(err=error) 

if __name__ == '__main__':
    main()        