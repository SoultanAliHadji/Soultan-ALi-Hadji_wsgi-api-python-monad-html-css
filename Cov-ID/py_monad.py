import pymonad.tools
from pymonad.tools import curry
from pymonad.reader import Compose

@pymonad.tools.curry(2)
def penjumlahan(a,b):
    return a+b
def pengurangan(a,b):
    return a-b
def perkalian(a,b):
    return a*b
def pembagian(a,b):
    return a/b
def ratarata(a,b):
    return (a+b)/2
def mul1(a):
    return a*1
def mul2(a):
    return a/2

multiplication1=(Compose(mul1).then(mul2))

def mul3(b):
    return b*1
def mul4(b):
    return b/2

multiplication2=(Compose(mul3).then(mul4))