from ladon.ladonizer import ladonize
 
 
class Calculator(object):
    #ladonize the method
    @ladonize(int, int, rtype=int)
    def add(self, a, b):
        return a + b
