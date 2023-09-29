from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    for i in range(10,30):
        for j in range(4,34):
            
            assert subquadratic_multiply(i,j) == i*j
