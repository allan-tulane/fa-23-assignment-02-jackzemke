"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time
import matplotlib.pyplot as plt 

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def subquadratic_multiply(x, y):
    return _subquadratic_multiply(x,y).decimal_val
    ###

def _subquadratic_multiply (x,y):
    if type(x) != type(BinaryNumber(5)) or type(y) != type(BinaryNumber(5)):
        xvec = BinaryNumber(x).binary_vec
        yvec = BinaryNumber(y).binary_vec
    else:
        xvec = x.binary_vec
        yvec = y.binary_vec
        x = x.decimal_val
        y = y.decimal_val
    xvec, yvec = pad(xvec,yvec)
    n = len(xvec)
    # print(n)
    if x <= 1 and y <= 1:
        return BinaryNumber(x*y)
    else:
        x_left, x_right = split_number(xvec)
        y_left, y_right = split_number(yvec)
    z0 = _subquadratic_multiply(x_right.decimal_val,y_right.decimal_val)
    z1 = _subquadratic_multiply(x_left.decimal_val+x_right.decimal_val,
                                         y_left.decimal_val+y_right.decimal_val)
    z2 = _subquadratic_multiply(x_left.decimal_val,y_left.decimal_val)
    z2shifted = bit_shift(z2,n)
    z1real = bit_shift(BinaryNumber(z1.decimal_val - z2.decimal_val - z0.decimal_val),n//2)
    return BinaryNumber(z2shifted.decimal_val + z1real.decimal_val + z0.decimal_val)
    # return(BinaryNumber(a.decimal_val+(b.decimal_val-c.decimal_val-a.decimal_val)+c.decimal_val))

