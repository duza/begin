class creditOfWorkers:
    
    def __init__(self, money=22000,soname="Mister Anderson",credit=175000,number=12):
        self.moneyPerDay = money
        self.sonameOfWorker = soname
        self.creditOnTransport = credit
        self.numberDays = number

    def getters(self):
        return self.moneyPerDay,self.sonameOfWorker,self.creditOnTransport,self.numberDays

    def setters(self, moneyPerDay,sonameOfWorker,creditOnTransport,numberDays):
        self.moneyPerDay = moneyPerDay
        self.sonameOfWorker = sonameOfWorker
        self.creditOnTransport = creditOnTransport
        self.numberDays = numberDays

    def GetTotal(self):
        self.totalCredit = self.creditOnTransport + self.numberDays * self.moneyPerDay
        return self.totalCredit

    def Show(self):
        print u"money  per day = "+str(self.moneyPerDay)
        print u"soname  of worker = "+str(self.sonameOfWorker)
        print u"credit on transport = "+str(self.creditOnTransport)
        print u"number of days = "+str(self.numberDays)
        print u"total credit = "+str(self.GetTotal())

    def ToString(self):
        print  str(self.moneyPerDay)+";"+str(self.sonameOfWorker)+";"+str(self.creditOnTransport)+";"+str(self.numberDays)+";"+str(self.GetTotal())

arrayOfObjects = [creditOfWorkers(25000,'Alex Markovich',53000,7),creditOfWorkers(27600,'Bob Torton',58000,9),[],creditOfWorkers(15000,'Mihael Shuman',33000,3),creditOfWorkers()]
for i in arrayOfObjects:
    if i != []: i.Show()
arrayOfObjects[-1].creditOnTransport = 190000
duration = arrayOfObjects[0].numberDays + arrayOfObjects[1].numberDays
print u"duration = "+ str(duration)
for i in arrayOfObjects:
    if i != []: i.ToString()