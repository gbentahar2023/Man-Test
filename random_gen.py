from dataclasses import dataclass
from operator import sub
import random  as rd
import numpy as np
from rd_settings import create_v_p


@dataclass(frozen=False, order = True) 
class RandomGen(object):     
    _random_nums : list # Values that may be returned by next_num()
    _probabilities : list # Probability of the occurence of random_nums 
    
    @property
    def random_nums(self):
        return self._random_nums

    @property
    def probabilities(self):
        return self._probabilities

    def initiate(self):
        setattr(self,'cum_probabilities_targets', dict(zip(self._random_nums, np.cumsum(self._probabilities))))
        setattr(self,'generated_numbers_state', dict(zip(self._random_nums, len(self._random_nums)*[0])))
        setattr(self,'generated_probabilities_state', dict(zip(self._random_nums, len(self._random_nums)*[0])))
        setattr(self,'generated_states', 0)
        setattr(self,'approximation_error', 0)

    # Update generated_numbers_state and generated_proabilities_state values with the selected element 

    def update_element(self,element):
        self.generated_numbers_state[element] +=  1
        self.generated_probabilities_state = {k:v/self.generated_states for k,v in self.generated_numbers_state.items()}
        # revisit this for the right assessement of error measurement
        self.approximation_error = sum([x*x for x in list(map(sub, list(self.generated_probabilities_state.values()), self._probabilities))])
        
    # Function asked for this exercice
    def next_num(self):
        if not hasattr(self, 'generated_states'):
            self.initiate()
        # This is more adapted to non int numbers for inputed _random_nums
        u = rd.uniform(0, 1) # Draw from a uniform distribution and locate in the cumulative probability vector with n_num
        p_l = [v-u for v in self.cum_probabilities_targets.values()]
        n_num = min([i for i,p_cum in enumerate(p_l) if p_cum>0]) # Choose index of first positive number as the draw
        element = self._random_nums[n_num]
        self.generated_states = self.generated_states + 1        
        self.update_element(element)

    # run next_num multiple times
    def run_simulation(self, simulations):
        for i in range(0,simulations):
            self.next_num()
        print(self.generated_numbers_state)
        print(self.generated_probabilities_state)
        print(self.generated_states)
        print(self.approximation_error)
     
# if __name__ == '__main__':
#     v = [-1,0,1,2,3]
#     p = [0.01,0.3,0.58,0.1,0.01]
#     simulations = 10000
#     rg = RandomGen(v,p)
#     rg.run_simulation(simulations)




    

    

    
    