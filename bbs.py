BIT_LEN = 128

def blum_blum_shub(seed ,p = 383, q = 503):
    seed = None
    while not seed:
        seed = raw_input("Please enter seed for calculating Nonce:")
    m = p * q
    n = BIT_LEN
    xi = int(seed)
    finalval = 0

    for i in range(0, BIT_LEN):
        xiplus1 = (xi**2) % m
        xi = xiplus1
        output = xiplus1 % 2
        finalval = (finalval << 1) + output
    #return bin(finalval)
    return format(finalval, 'x')

if __name__ == '__main__':
	seed = None
	print blum_blum_shub(seed)
