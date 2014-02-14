#-*- coding:utf-8 -*-
#using python 2.7.3
''' This program describes the purchase of goods '''

class BasicCommodity:
    """This class describes any goods"""
    def __init__(self, name, price):
        ''' __init__(self, str, int) -> instance BasicCommodity
        Method takes two arguments: name of the commodity and
        its price. '''
        self.__nameCommodity = check(name, str)
        self.__priceBrCommodity = check(price, int)

    @property
    def nameCommodity(self):
        ''' Method getter of the field - name'''
        return self.__nameCommodity

    @nameCommodity.setter
    def nameCommodity(self, value):
        ''' Method setter of the field - name '''
        self.__nameCommodity = check(value, str)

    @property 
    def priceBrCommodity(self):
        ''' Method getter of the field - price '''
        return self.__priceBrCommodity

    @priceBrCommodity.setter
    def priceBrCommodity(self, value):
        '''Method setter of the field - price'''
        self.__priceBrCommodity = check(value, int)

    def  ToString(self):
        ''' Method return all fields instance of the BasicCommodity class
         in csv format '''
        return '{name};{price}'.format(name= self.nameCommodity,
         price=elf.priceBrCommodity)

    # def __str__(self):
    #     return self.ToString()

from abc import ABCMeta, abstractmethod
class AbstractPurchase:
    """It is the abstract basic class - AbstractPurchase"""
    __metaclass__ = ABCMeta

    def __init__(self, commodity, number):
        ''' __init__(self, str, int) -> instance AbstractPurchase
        Method takes two arguments: commodity and the amount. '''
        # super(AbstractPurchase, self).__init__()
        self.__commodity = check(commodity, BasicCommodity)
        self.__number = check(number, int)

    @property 
    def commodity(self):
        ''' Method getter of the field - commodity '''
        return self.__commodity

    @commodity.setter
    def commodity(self, value):
        ''' Method setter of the field (object) - commodity '''    
        self.__commodity = check(value, BasicCommodity)

    @property 
    def number(self):
        ''' Method getter of the field - number pcs '''
        return self.__number

    @number.setter
    def number(self, value):
        ''' Method setter of the field - number'''
        self.__number = check(value, int)

    @abstractmethod
    def getCost(self):
        '''Calculates total cost of purchase'''

    def ToString(self):
        ''' Method return all fields instance of the AbstractPurchase
         class in csv format '''
        return '{name};{price};{number};{cost}'.format(\
            name=self.commodity.nameCommodity, 
            price=self.commodity.priceBrCommodity, 
            cost=self.getCost(), number=self.number)

    def CompareTo(self, object):
        ''' This method compares two object of AbstractPurchase class:
        self instance and object:
        CompareTo(self, object) -> Boolean '''
        if self.getCost() > object.getCost():
            return True
        else:
            return False

    def __str__(self):
        return self.ToString()

class FixDiscountPurchase(AbstractPurchase):
    """ This is class of purchases with discount. It inherits 
    attributes of the AbstractPurchase class. Methods getCost and 
    ToString are overridden, but the essence is the same. """
    def __init__(self, commodity, number, discount):
        super(FixDiscountPurchase, self).__init__(commodity, number)
        self.__discount = check(discount, int)

    @property 
    def discount(self):
        ''' Method getter of the field - discount '''
        return self.__discount

    @discount.setter
    def discount(self, value):
        ''' Method setter of the field - discount '''
        self.__discount = check(value, int)
    
    def getCost(self):
        ''' This method calculates total cost of the purchase with discount'''
        return self.commodity.priceBrCommodity * \
        (1- float(self.discount)/100) * self.number

    def ToString(self):
        return '{name};{price};{number};{discount};{cost:.0f}'.format(\
            name=self.commodity.nameCommodity, 
            price=self.commodity.priceBrCommodity, 
            cost=self.getCost(), number=self.number, 
            discount=self.discount)

class DiscountNumberPurchase(AbstractPurchase):
    """ This is class of purchases with discount on the amount of commodity
    (if the amount more constant WHOLESALE). It inherits attributes of the 
    AbstractPurchase class. Methods getCost and ToString are overridden,
     but the essence is the same. """
    
    WHOLESALE = 10
    def __init__(self, commodity, number, discount):
        super(DiscountNumberPurchase, self).__init__(commodity, number)
        if self.number > self.WHOLESALE:
            self.__discount = check(discount, int)
        else:
            self.__discount = 0

    @property 
    def discount(self):
        ''' Method getter of the field - discount '''
        return self.__discount

    @discount.setter
    def discount(self, value):
        ''' Method setter of the field - discount '''
        self.__discount = check(value, int)
    
    def getCost(self):
        return self.commodity.priceBrCommodity *\
         (1- float(self.discount)/100) * self.number

    def ToString(self):
        ''' Method return all fields instance of the
         BasicCommodity class in csv format '''
        return '{name};{price};{number};{discount};{cost:.0f}'.format(\
            name=self.commodity.nameCommodity, 
            price=self.commodity.priceBrCommodity, 
            cost=self.getCost(), number=self.number, 
            discount=self.discount)

class WithShippingPurchase(AbstractPurchase):
    """ This is class of purchases with shipping cost. It inherits 
    attributes of the AbstractPurchase class. Methods getCost 
    and ToString are overridden, but the essence is the same. """
    def __init__(self, commodity, number, shippingCost):
        super(WithShippingPurchase, self).__init__(commodity, number)
        self.__shippingCost = shippingCost

    @property 
    def shippingCost(self):
        ''' Method getter of the field - shipping cost '''
        return self.__shippingCost

    @shippingCost.setter
    def shippingCost(self, value):
        ''' Method setter of the field - shipping cost '''
        self.__shippingCost = value

    def getCost(self):
        ''' This method calculates total cost of the purchase
         with discount'''
        return self.commodity.priceBrCommodity *\
         self.number - self.shippingCost

    def ToString(self):
        ''' Method return all fields instance of the BasicCommodity
         class in csv format '''
        return '{name};{price};{number};{shipping};{cost:.0f}'.format(\
            name=self.commodity.nameCommodity, 
            price=self.commodity.priceBrCommodity, 
            cost=self.getCost(), number=self.number, 
            shipping=self.shippingCost)

def check(value, type):
    ''' Function checks the type of the input field of class '''
    if isinstance(value, type):
        return value
    else:
        raise AttributeError("Incorrect {0} field type {1} !"\
            .format(value, type))

def userSort(arrayObj):
    ''' User's method sorting '''
    n =1 
    while n < len(arrayObj) :
        for index, element in enumerate(arrayObj):
            if index < len(arrayObj) - n and \
            not element.CompareTo(arrayObj[index+1]):
                arrayObj[index], arrayObj[index+1] =\
                 arrayObj[index+1], arrayObj[index]
        n+=1
    return arrayObj

def main():
    try:
        array = [
        FixDiscountPurchase(BasicCommodity('milk',7200),12,5), 
        DiscountNumberPurchase(BasicCommodity('bread',8600),22,3), 
        WithShippingPurchase(BasicCommodity('ice-cream',11000),5,5000), 
        FixDiscountPurchase(BasicCommodity('chocolate',12000),3,2), 
        DiscountNumberPurchase(BasicCommodity('juice',7900),4,1), 
        WithShippingPurchase(BasicCommodity('coffee',11900),2,10000)]
    except (TypeError, ValueError, AttributeError) as exc:
        print exc
    for element in array:
        print element, element.__class__.__name__
    # array.sort(key=lambda x: x.getCost() , reverse=True)
    # print '\n','-*-'*16, '\nAfter sorting with method sort():'
    print '\n','-*-'*16,"\nAfter sorting with user's method CompareTo():\n"
    for element in userSort(array):
        print element, element.__class__.__name__

if __name__ == '__main__':
    main()