from main import *

def _quadratic_multiply(x, y):
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
    # print(xvec)
    # print(yvec)
    # print(y_left.binary_vec,y_right.binary_vec)
    a = bit_shift(_quadratic_multiply(x_left.decimal_val,y_left.decimal_val),n)
    b1 = _quadratic_multiply(x_left.decimal_val,y_right.decimal_val)
    b2 = _quadratic_multiply(x_right.decimal_val,y_left.decimal_val)
    bs = BinaryNumber(b1.decimal_val+b2.decimal_val)
    b = bit_shift(bs,n//2)
    c = _quadratic_multiply(x_right.decimal_val,y_right.decimal_val)
    # print(a)
    return(BinaryNumber(a.decimal_val+b.decimal_val+c.decimal_val))
    # return bit_shift(quadratic_multiply(x_left,x_right), n) + bit_shift((quadratic_multiply(x_left,y_right)) + (quadratic_multiply(x_right*y_left)), n/2) + (quadratic_multiply(x_right, y_right))
    # pass
    ###

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val


# for i in range(10,30):
#     for j in range(4,34):
#         t = subquadratic_multiply(i,j)
#         print(f'{t} = {i}*{j} = {i*j}')
#         assert t == i*j

def time_multiply(x, y, f):
    start = time.time()
    f(x,y)
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000


def graph():
    n = []
    t = []
    l = []
    for i in range(2,13):
        n.append(i+1)
        # l.append(2**i)
        t.append(time_multiply((2**i),(2**i),subquadratic_multiply))
        l.append(time_multiply((2**i),(2**i),quadratic_multiply))
    # print(l)
    # print(n)
    # print(t)
    plt.plot(n,t, label = 'Sub-Quadratic')
    plt.plot(n,l, label = 'Quadratic')
    plt.legend()
    plt.title('Time to execute Sub-Quadratic vs Quadratic multiply')
    plt.xlabel('Number of bits')
    plt.ylabel('Time required to execute')
    plt.show()


graph()
    
