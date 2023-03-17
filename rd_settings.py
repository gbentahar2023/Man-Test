import numpy as np 
from drs import drs
import random as rd


NUMSIMULATIONS = 10000
LENVECT_V = 10
ERROR = 0.0000001
METHOD ='generated'
#METHOD ='fixed1' 
ERROR_SIM = LENVECT_V/NUMSIMULATIONS
#If input mistake Force the METHOD to be fixed if it is neither fixed or generated
if METHOD not in ['generated','fixed']:
    METHOD = 'fixed'

# The function generating the initial values v and probabilities p for random_gen constructor with the method METHOD
# If METHOD is not generated then these are fixed inputs

def create_v_p(method,v_size=5):
    if method.lower() == 'generated':
        zeros = v_size*[0]
        ones = v_size*[1]
        v =  rd.sample(range(-1, v_size), v_size)
        p = drs(v_size, 1, ones, zeros) # https://pypi.org/project/drs/
    else:
        # Put original values from the test paper can be chosen differently
        v = [-1.00,0.00,1.00,2.00,3.00]
        p = [0.01,0.3,0.58,0.1,0.01]
    return v,p,method

