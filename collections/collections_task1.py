# -*- coding: utf-8 -*-
# using python 2.7.3
''' This program describes the storage objects of two classes(the basic 
    class of purchase and a derivative class of discount purchase) in the 
class collection of purchases. The input file in csv format  contains a 
sequence of strings, where each string is attributes of object.'''

import csv, sys, argparse

__metaclass__=type

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

        __eq__(self, object) -> True or False
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

    def ToString(self):
        return "{product};{price};{number};{cost}".format(\
        product=self.productName, price=self.priceBr,
         number=self.numberUnits, cost=self.GetCost())

    def __str__(self):
        return self.ToString()

    def __eq__(self, other):
            if  (self.productName is other.productName) and \
            (self.priceBr is other.priceBr):
                return True
            else:
                return False

    def __cmp__(self, other):
        if self.productName > other.productName:
            return 1
        elif self.productName < other.productName:
            return -1
        else:
            if type(self) == type(other):
                if self.GetCost() > other.GetCost():
                    return 1
                elif self.GetCost() < other.GetCost():
                    return -1
                else:
                    return 0
            elif isinstance(self,BasicPurchase) and isinstance(other, FixDiscountPurchase):
                return -1
            elif isinstance(self,FixDiscountPurchase) and isinstance(other, BasicPurchase):
                return 1
            else:
                return 0

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
        return  (self.priceBr - self.discount) * self.numberUnits

    def ToString(self):
        return "{product};{price};{number};{discount};{cost:.0f}"\
        .format(product=self.productName, price=self.priceBr,
         discount=self.discount, number=self.numberUnits,
         cost=self.GetCost())

class ListPurchases:
    """ ListPurchases(self, file) -> instance
        Class is used to store objects of two classes: a base class 
        BasicPurchase, the derived class FixDiscountPurchase.

        Attribute of class - list, contents instances of classes purchases.  
    """
    CONST_BASIC = 3
    CONST_DISCOUNT = 4
    def __init__(self, filecsv="file"):
        self.__list = []
        try:
            # open file
            with open(filecsv+".csv","rb") as f:
                reader = csv.reader(f, delimiter=";", quoting=csv.QUOTE_NONE)
                try:
                    for row in reader:
                        # Creates purchase from row (list of strings)
                        purchase = self.createPurchase(row,reader.line_num,filecsv)
                        # If creation happened and purchase is not empty
                        if  purchase is not None:
                            self.__list.append(purchase)
                except csv.Error as err:
                    sys.exit('file %s, line %d: %s' % (filecsv, reader.line_num, err))
                except Exception as  errors:
                    print '[Errors!]:{}'.format(errors)
        except IOError as e:
            print "I/O error({0}): {1} '{2}.csv'.".format(e.errno, e.strerror, filecsv)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

    @property
    def list(self):
        return self.__list

    @list.setter
    def list(self, value):
        self.__list = value

    def createPurchase(self, csvString, line_num, filecsv):
        ''' Method creates purchase using data from line 'csvString' 
        number of 'line_num' in the 'filecsv' '''
        try:
            # if number of elements csvString correspondes number
            # of attributes object BasicPurchase
            if len(csvString) == ListPurchases.CONST_BASIC:
                return BasicPurchase(*self.checkCsv(csvString, line_num, filecsv))
            # if number of elements csvString correspondes number
            # of attributes object FixDiscountPurchase
            elif len(csvString) == ListPurchases.CONST_DISCOUNT:
                 return FixDiscountPurchase(*self.checkCsv(csvString, line_num, filecsv))
            else:
                print "Line {0} of file '{1}.csv' isn't correct. Sorry, but reading the line isn't possible.".format(line_num, filecsv)
        except Exception as e:
            print "Line {0} of file '{1}.csv' isn't correct. Sorry, but reading the line isn't possible.".format(line_num, filecsv)
            print e
    
    def checkCsv(self, csvString, line_num, filecsv):
        ''' Method takes an input list of strings, number of line input file 
        and name of input file.'''
        try:
            # try assign if len(csvString) == 3
            name, price, num = csvString
            # if input variablea is correct
            if name and int(price) and int(num):
                return name, int(price), int(num)
            else:
                print "Incorrect data in {0} line of '{1}.csv'!".format(line_num, filecsv)
        except ValueError:
            # try assign if len(csvString) == 4
            name, price, num, discount = csvString
            if name and int(price) and int(num) and int(discount) and int(price) > int(discount):
                return name, int(price), int(num), int(discount)
            else:
                 print "Incorrect data in {0} line of '{1}.csv'!".format(line_num, filecsv)
        except Exception as e:
            print 'Unexpected exception! In checkCsv.',e

    def Insert(self, index, purchase):
        ''' The method makes insert purchases in position index, 
        if index incorrect value, then add the purchase to the end of list'''
        try:
            # if the index is within the list
            if 0<=index<len(self.list):
                self.list.insert(index, purchase)
            else:
                self.list.append(purchase)
        except Exception, e:
            print e
            self.list.append(purchase)

    def Delete(self, index):
        ''' Method returns index removed element or -1 if index of 
        element to be deleted incorrect'''
        try:
            # if the index is within the list
            if 0<=index<len(self.list):
                self.list.pop(index)
                return index
            else:
                return -1 
        except Exception, e:
            print e
            return -1
        
    def TotalCost(self):
        ''' Method calculates and return cost of all purchases in the list '''
        return sum(map(lambda x: x.GetCost(), self.list))

    def Print(self):
        ''' Method output content of list collection in tabular form '''
        print '-'*109
        print "|{0:^25s}|{1:^25s}|{2:^10s}|{3:^25s}|{4:^18s}|".format(
            'Name','Price','Number','Cost','Discount')
        print '-'*109
        for purchase in self.list:
            try:
                # try print if purchase is instance of FixDiscountPurchase
                print '|{0:^25s}|{1:^25}|{2:^10d}|{3:^25.0f}|{4:^18d}|'.format(
                    purchase.productName,purchase.priceBr, 
                    purchase.numberUnits, purchase.GetCost(), 
                    purchase.discount)
                print '-'*109
            except:
                # if purchase is instance of BasicPurchase
                print '|{0:^25s}|{1:^25}|{2:^10d}|{3:^25.0f}|{4:^18s}|'.format(
                    purchase.productName, purchase.priceBr, 
                    purchase.numberUnits, purchase.GetCost(),'')
                print '-'*109
        print "|{0:^25s}|{1:^25s}|{2:^10s}|{3:^25.0f}|{4:^18s}|".format(
            'Total cost','','',self.TotalCost(),'') 
        print '-'*109

    def Sort(self):
        ''' Method of sorting list purchases '''
        self.list = sorted(self.list)


    def BinarySearch(self, element):
        ''' Method looks for an object by its hash and return element and
         index of list, if it was found'''
         # Creates list of hashes elements of collection purchases
        hashlist = map(lambda x: x.__hash__(), self.list)
        # Calculate hash of required element
        hashel = element.__hash__()
        if hashel in hashlist:
            print u'Элемент \n{0}\nнайден на позиции {1}'.format(element, hashlist.index(hashel))
        else:
            print u'Элемент \n{0}\nне найден'.format(element) 
       

def createParser():
    ''' This function creates parser, which reading two optional arguments 
    of console: file and addon.'''
    # Creates instance of ArgumentParser with default settings
    parser = argparse.ArgumentParser()
    # Adds expected optional parametrs on console with help method add_argument
    parser.add_argument('basic_file',nargs='?', default="file")
    # Both of arguments will be considered a positional parametrs
    parser.add_argument('addon_file',nargs='?', default="addon")
    return parser

def check(value, type):
    ''' Function checks the type of the input field of class '''
    if isinstance(value, type):
        return value
    else:
        raise AttributeError("Incorrect {0} field type {1} !".format(value, type))


def main():
    # Creates parser of parametrs our command line
    parser = createParser()
    # Give to method parse_args no arguments = all the parameters of sys.argv
    # except the null, which contains the name of our program
    namespace = parser.parse_args()   
    # Creates object of collection, give it argument - parametr of basic file
    collectionPurchases = ListPurchases(namespace.basic_file)
    print u'После создания:'
    # Output on console collection
    collectionPurchases.Print()
    # Creation object of collection, give it argument - parametr of addon file
    collectionPurchasesTWO = ListPurchases(namespace.addon_file)
    # Insert the last of the second collection to the 0 position of the first collection of purchases
    collectionPurchases.Insert(0,collectionPurchasesTWO.list[-1])
    collectionPurchases.Insert(1000,collectionPurchasesTWO.list[0])
    collectionPurchases.Insert(2,collectionPurchasesTWO.list[2])
    # remove elements through method Delete() index 3, 10 and -5
    collectionPurchases.Delete(3)
    collectionPurchases.Delete(10)
    collectionPurchases.Delete(-5)
    # Output collection
    print u'До сортировки:'
    collectionPurchases.Print()
    # Sorting of collection
    collectionPurchases.Sort()
    # Output after sorting collection
    print u'После сортировки:'
    collectionPurchases.Print()
    print u'Поиск по хэшам:'
    collectionPurchases.BinarySearch(collectionPurchasesTWO.list[0])
    collectionPurchases.BinarySearch(collectionPurchasesTWO.list[3]) 

if __name__ == '__main__':
    main()