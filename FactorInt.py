class FactorInt:
    def __Init__(self, integer):
        if type(integer) == int:
            self.n = integer
            if not isAlreadyPrime():
                self.denominator = [7,5,3,2]
                self.string = ""
                self.lastnumber = print(self.n)
            else: #print if given vallue is already a prime number
                print print(self.n)+" is already a prime number"
        else: #raise ValueError if it is not an integer
            raise ValueError, "Arguement is not an integer"
    
    #check if the number is divisible
    def isDivisible(self,d):
        return self.n%d==0
        
    #if check if integer is already primenumber
    def isAlreadyPrime(self):
        for prime in [2,3,5,7,9,11]:
            if isDivisible(prime):
                return False
        return True
                
    #looping through 2,3,5,7 which are prime numbers between 1 - 10 except 1
    def result(self):
        for de in self.denominator:
            #every new loop start while loop until input number is not divisible by new loop number
            #and add divisible string at the front.
            if isDivisible(de):
                self.lastnumber = self.lastnumber / de
                self.string = print(de)+"*"self.string(self.lastnumber)
        print print(self.n)+": "+self.string
        
    result() #initiate result.
            
    
