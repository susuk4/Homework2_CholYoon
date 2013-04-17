Homework2_CholYoon
==================
#0925740
==================

Factoring the integer and return string of equation by toString() def. 
Also, it allows to check if given integer is divisible by some other integer.
Containing method will be isDivisible(), toString(), isAlreadyPrime() which is to check if it is already prime number
It throws ValueError if input is not integer.

Factorint.py = class coded with factoring integer.

README.md = instruction.

Example)
x = Factorint(0)
Value Error

x = Factorint(2.4)
Value Error

x = Factorint(24)
divisibleBy2 = x.isDivisible(2)
divisibleBy2 = True

divisible = x.isDivisible()
divisible = True

printFactor = x.toString()
print printFactor
"24: 2*2*2*3"

y = Factorint(-24)
printFactor = y.toString()
print printFactor
"-24: -1*2*2*2*3"
