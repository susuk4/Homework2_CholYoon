class FactorInt:
    def __Init__(self, integer):
        #initialize class with initial string, and denominator and check if it is integer
        if type(integer) == int:
            self.n = integer
            if not isAlreadyPrime():
                self.denominator = [7,5,3,2]
                self.string = ""
                self.negative = isNegative(self.n)
                self.lastnumber = print(self.n)
            elif self.n==0:
                print "0 cannot be factored"
            else: #print if given vallue is already a prime number
                print print(self.n)+" is already a prime number"
        else: #raise ValueError if it is not an integer
            raise ValueError, "Arguement is not an integer"
    
    #check if the number is divisible by specific number
    def isDivisible(self,d):
        return self.n%d==0
    
    #check if the number is divisible by any number
    def isDivisible(self):
        return isAlreadyPrime()
        
    #if check if integer is already primenumber
    def isAlreadyPrime(self):
        for prime in [2,3,5,7,9,11]:
            if isDivisible(prime):
                return False
        return True
    
    #check to see if input is negative, if it is negative -1 will be added at last result
    def isNegative(self)
        if self.n<0
            self.n = -1*self.n
    #looping through 2,3,5,7 which are prime numbers between 1 - 10 except 1
    #and return resulted string
    def toString(self):
        for de in self.denominator:
            #every new loop start while loop until input number is not divisible by new loop number
            #and add divisible string at the front.
            if isDivisible(de):
                self.lastnumber = self.lastnumber / de
                self.string = print(de)+"*"self.string(self.lastnumber)
        if self.negative #if negative ad -1 at last
            self.string = print(-1)+"*"+self.string
        return print(self.n)+": "+self.string 
            
    
