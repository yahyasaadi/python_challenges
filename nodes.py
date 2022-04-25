class Daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

d1 = Daynames('Mon')
d2 = Daynames('Wed')
d3 = Daynames('Tue')
d4 = Daynames('Thu')


d1.nextval = d3
d3.nextval = d2
d2.nextval = d4

currentval = d1

while currentval:
    print(currentval.dataval)
    currentval = currentval.nextval