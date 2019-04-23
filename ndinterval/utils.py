import numpy as np
import logging

def int2binarray(number, n_bits):
    if (2**n_bits) <= number:
        logging.error("not enouhg bits")
    else:
        a = format(number, "#0%db" % (n_bits + 2))[2::]
        binary = np.array([int(x) for x in list(a)])
        return binary
