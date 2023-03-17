import unittest
from unittest.mock import patch # To be checked further
from random_gen import RandomGen
import rd_settings as ts


class TestRandomGen(unittest.TestCase):
    
    def setUp(self):
        v,p,method = ts.create_v_p(ts.METHOD,ts.LENVECT_V)
        self.rg = RandomGen(v,p)
        self.method = method
    
    def tearDown(self):
        pass

    # Implicitly testing ts.create_v_p 
    def test_sum_probabilities_equal_1(self):
        self.assertAlmostEqual(round(sum(self.rg.probabilities)),1.00,ts.ERROR)
    
    def test_probabilities_not_negative(self):
        neg_test = bool(len([v for v in self.rg.probabilities if v <0])==0)
        self.assertTrue(neg_test)

    def test_probabilities_not_zero(self):
        zero_test = bool(len([v for v in self.rg.probabilities if v == 0])==0)
        self.assertTrue(zero_test)

    # Testing if probabilities are higher than 1 will be captured by the above so no need to include it

    def test_v_p_not_empty(self):
        self.assertTrue(bool(len(self.rg.probabilities)!=0) and bool(len(self.rg.random_nums)!=0))
       
    def test_inputs_in_v_not_repeated(self):
         unique_v = (len(self.rg.random_nums)>len(set(self.rg.random_nums)))
         self.assertFalse(unique_v)
    
    def test_size_v_p_same(self):
        self.assertTrue(len(self.rg.probabilities)==len(self.rg.random_nums))
    

    def test_correct_method_inputed(self):
        self.assertTrue(self.method==ts.METHOD)

    ## Implicitly testing RandomGen 
    # In reference to the comment in the test:
    # When this method is called multiple times over a long period, it should return the numbers roughly with the initialized probabilities. 
    
    def test_convergence_simulation(self):
        self.rg.run_simulation(ts.NUMSIMULATIONS)
        converge_true = bool(self.rg.approximation_error<ts.ERROR_SIM)
        self.assertTrue(converge_true)

# python -m unittest test_random_gen.py if no main
# python test_random_gen.py if main

if __name__ == '__main__':
    unittest.main()




