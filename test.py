class test:
    count=0
    def __init__(self):
        test.count=test.count+1
    @classmethod
    def noOfObjects(cls):
      print('number of objects created for test class:',cls.count)
t1=test()
t2=test()
test.noOfObjects()
t3=test()
t4=test()
t5=test()
test.noOfObjects() 
