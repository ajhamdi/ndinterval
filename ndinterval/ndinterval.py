import numpy as np
from numpy.linalg import inv
from interval import interval
class ndinterval():
    def __init__(self,a,b):
        if len(a) != len(b):
            print("not valid n-dim interval")
        elif "interval" not in sys.modules:
            print("pip install pyinterval module first !!")
        else:
            self.n = len(a)
            self.two_to_n = 2**self.n
            self.mask = np.array([int2binarray(x,n_bits=self.n) for x in range(self.two_to_n) ]).T
            self.mask_c = np.logical_not(self.mask).astype(np.int)
            self.a = np.array(a) ; self.b = np.array(b)
            self.update()
            self.old_a = self.a ; self.old_b = self.b
    def step_size(self):
        return np.sum(self.a - self.old_a) + np.sum(self.b - self.old_b)
    def size(self):
        return np.prod(self.r)
    def update(self):
        self.region = [interval([self.a[ii],self.b[ii]]) for ii in range(self.n)]
        self.r  = np.array([x[0][1] - x[0][0] for x in self.region])
        self.R = inv(np.diag(self.r))
        self.corners_matrix = np.matmul(np.ones([self.two_to_n,1]) , np.expand_dims(self.a,axis=0)) + self.mask.T * np.matmul(np.ones([self.two_to_n,1]) , np.expand_dims(self.r,axis=0))
        self.corners_set = [self.corners_matrix[ii,::] for ii in range(self.two_to_n)]
    def size_normalized(self):
        return self.size() / self.two_to_n
    def __str__(self):
        return str(self.region)
    def __call__(self,a,b):
        self.old_a = self.a.copy() ; self.old_b = self.b.copy()
        self.a = a.copy() ; self.b = b.copy()
        self.update()
    def __and__(self,interval2):
        return [x & y for x,y in zip(self.region,interval2.region)]
    def __or__(self,interval2):
        return [x | y for x,y in zip(self.region,interval2.region)]
